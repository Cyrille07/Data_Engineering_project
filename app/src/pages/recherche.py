import requests
from dash import html, dcc, Input, Output, State, callback
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

from src.components.navbar import Navbar


# Configuration Elasticsearch
es_client = Elasticsearch("http://localhost:9200")
index = "clothes"

# Fonction pour la page Recherche
def SearchPage():
    return html.Div(
        style={
            "backgroundColor": "#f4f4f4",
            "padding": "20px",
            "fontFamily": "Arial, sans-serif",
        },
        children=[

            # Navbar ajoutée
            Navbar(),

            # Titre
            html.H2("Recherche de vêtements", style={"textAlign": "center"}),

            # Filtres
            html.Div(
                style={"margin": "20px 0", "display": "flex", "gap": "20px", "justifyContent": "center"},
                children=[
                    # Filtre pour le sexe
                    html.Div(
                        children=[
                            html.Label("Sexe"),
                            dcc.Dropdown(
                                id="filter-sexe",
                                options=[
                                    {"label": "Men", "value": "men"},
                                    {"label": "Women", "value": "women"},
                                    {"label": "Both", "value": "both"},
                                ],
                                value="both",  # Valeur par défaut
                                style={"width": "200px"},
                            ),
                        ]
                    ),
                    # Filtre pour le type de vêtement
                    html.Div(
                        children=[
                            html.Label("Type de vêtement"),
                            dcc.Dropdown(
                                id="filter-type",
                                options=[
                                    {"label": "Bottom", "value": "bottom"},
                                    {"label": "Outwear", "value": "outwear"},
                                    {"label": "Sweater", "value": "sweater"},
                                    {"label": "All", "value": "all"},
                                ],
                                value="all",  # Valeur par défaut
                                style={"width": "200px"},
                            ),
                        ]
                    ),
                    # Filtre pour la note
                    html.Div(
                        children=[
                            html.Label("Note (intervalle)"),
                            dcc.RangeSlider(
                                id="filter-rate",
                                min=0,
                                max=5,
                                step=0.1,
                                marks={i: str(i) for i in range(6)},
                                value=[0, 5],  # Valeur par défaut
                                tooltip={"placement": "bottom", "always_visible": True},
                            ),
                        ]
                    ),
                    # Filtre pour le prix
                    html.Div(
                        children=[
                            html.Label("Prix (intervalle)"),
                            dcc.RangeSlider(
                                id="filter-price",
                                min=0,
                                max=160,
                                step=1,
                                marks={i: str(i) for i in range(0, 161, 20)},
                                value=[0, 160],  # Valeur par défaut
                                tooltip={"placement": "bottom", "always_visible": True},
                            ),
                        ]
                    ),
                ]
            ),

            # Bouton de recherche
            html.Div(
                children=[
                    html.Button(
                        "Rechercher",
                        id="search-button",
                        n_clicks=0,
                        style={
                            "backgroundColor": "#007BFF",
                            "color": "#FFF",
                            "border": "none",
                            "padding": "10px 20px",
                            "fontSize": "16px",
                            "borderRadius": "5px",
                            "cursor": "pointer",
                        },
                    )
                ],
                style={"textAlign": "center", "marginBottom": "20px"},
            ),

            # Conteneur pour afficher les résultats
            html.Div(id="search-results", style={"display": "flex", "flexWrap": "wrap", "gap": "20px", "justifyContent": "center"}),
        ]
    )


# Callback pour interagir avec Elasticsearch
@callback(
    Output("search-results", "children"),
    [Input("search-button", "n_clicks")],
    [
        State("filter-sexe", "value"),
        State("filter-type", "value"),
        State("filter-rate", "value"),
        State("filter-price", "value"),
    ],
)
def perform_search(n_clicks, sexe, type_, rate, price):
    if n_clicks == 0:
        return []  # Ne rien afficher tant que le bouton n'est pas cliqué

    # Construire la requête Elasticsearch
    query = {
        "query": {
            "bool": {
                "must": [
                    {"range": {"rate": {"gte": rate[0], "lte": rate[1]}}},  # Filtre pour les notes
                    {"range": {"price": {"gte": price[0], "lte": price[1]}}},  # Filtre pour les prix
                ],
                "filter": [],
            }
        }
    }

    # Ajouter les filtres pour le sexe
    if sexe and sexe != "both":
        query["query"]["bool"]["filter"].append({"term": {"sexe.keyword": sexe}})

    # Ajouter les filtres pour le type de vêtement
    if type_ and type_ != "all":
        query["query"]["bool"]["filter"].append({"term": {"type.keyword": type_}})

    try:
        # Effectuer la recherche dans Elasticsearch
        response = es_client.search(index=index, body=query,size=100)

        # Extraire les résultats
        hits = response["hits"]["hits"]

        # Générer les résultats pour l'affichage
        results = []
        for hit in hits:
            source = hit["_source"]
            results.append(
                html.Div(
                    style={
                        "width": "200px",
                        "border": "1px solid #ddd",
                        "borderRadius": "5px",
                        "padding": "10px",
                        "textAlign": "center",
                        "backgroundColor": "#FFF",
                    },
                    children=[
                        html.Img(
                            src=source["image"][0] if isinstance(source["image"], list) else source["image"],
                            style={"width": "100%", "height": "auto", "marginBottom": "10px"},
                        ),
                        html.Div(
                            source["name"][0] if isinstance(source["name"], list) else source["name"],
                            style={"fontWeight": "bold", "marginBottom": "5px"},
                        ),
                        html.Div(f"Prix : {source['price'] if isinstance(source['price'], (int, float)) else source['price'][0]} €"),
                        html.Div(f"Note : {source['rate'] if isinstance(source['rate'], (int, float)) else source['rate'][0]}"),
                        html.A(
                            "Voir le produit",
                            href=f"https://www.uniqlo.com{source['link'][0] if isinstance(source['link'], list) else source['link']}",
                            target="_blank",
                            style={"color": "#007BFF"},
                        ),
                    ],
                )
            )

        return results

    except Exception as e:
        return [
            html.Div(
                f"Erreur lors de la recherche : {str(e)}",
                style={"color": "red", "textAlign": "center"},
            )
        ]