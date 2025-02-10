import os
import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output


# Fonction pour la page de visualisation avec onglets
def VisuPage():
    return html.Div([
        # Bouton de retour vers la page d'accueil
        html.Div(
            dcc.Link(
                html.Button("Accueil", style={'margin': '10px', 'padding': '10px', 'font-size': '16px'}),
                href="/home"
            ),
            style={'position': 'absolute', 'top': '0', 'left': '0'}
        ),
        
        html.H2("Visualisation des données", style={'textAlign': 'center'}),

        # Onglets
        dcc.Tabs(id='tabs-example', value='tab-1', children=[
            dcc.Tab(label='Distribution des échantillons', value='tab-1'),
            dcc.Tab(label='Statistiques', value='tab-2'),
            dcc.Tab(label='Cartographie', value='tab-3'),
        ]),

        html.Div(id='tabs-content-example')
    ])

# Callback pour afficher le contenu en fonction de l'onglet sélectionné
@callback(
    Output('tabs-content-example', 'children'),
    [Input('tabs-example', 'value')]
)
def render_content(tab):
    if tab == 'tab-1':
        return distribution_content()
    elif tab == 'tab-2':
        return statistics_content()
    elif tab == 'tab-3':
        return cartography_content()


#------------------------------------------
# Contenu pour le premier onglet "Distribution des échantillons"
def distribution_content():
    return html.Div([
        html.H3("Distribution des échantillons", style={'textAlign': 'center', 'margin-top': '20px'}),
        html.Div([
            # Histogramme
            html.Div([
                html.Iframe(
                    id="stacked-bar-chart",
                    src="/assets/graphes_html/stacked_bar_chart.html",
                    style={
                        "width": "100%",
                        "height": "470px",
                        "border": "1px solid #ddd"
                    }
                )
            ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top', 'padding': '10px'}),

            # Sunburst
            html.Div([
                html.Iframe(
                    id="sunburst-chart",
                    src="/assets/graphes_html/sunburst_chart.html",
                    style={
                        "width": "108%",
                        "height": "470px",
                        "border": "1px solid #ddd"
                    }
                )
            ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top', 'padding': '10px'}),
        ], style={'display': 'flex', 'justify-content': 'space-around', 'align-items': 'center'}),
    ])

#------------------------------------------
# Contenu pour l'onglet "Statistiques" avec dropdown
def statistics_content():
    return html.Div([
        html.H3(style={'textAlign': 'center', 'margin-top': '01px'}),

        # Dropdown pour sélectionner l'analyse
        html.Div([
            html.Label("Choisissez une analyse :", style={'textAlign': 'center', 'margin-right': '10px'}),
            dcc.Dropdown(
                id='statistics-dropdown',
                options=[
                    {'label': 'Analyse des Prix', 'value': 'price'},
                    {'label': 'Analyse des Notes', 'value': 'rating'}
                ],
                value='price',  # Valeur par défaut
                style={'width': '50%', 'margin': '0 auto'}
            )
        ], style={'textAlign': 'center', 'margin-bottom': '20px'}),

        # Conteneur pour afficher le contenu sélectionné
        html.Div(id='statistics-content-container', style={'textAlign': 'center'})
    ])

# Callback pour afficher le contenu basé sur le dropdown sélectionné
@callback(
    Output('statistics-content-container', 'children'),
    [Input('statistics-dropdown', 'value')]
)
def update_statistics_content(selected_value):
    if selected_value == 'price':
        return price_content()  # Afficher l'analyse des prix
    elif selected_value == 'rating':
        return rating_content()  # Afficher l'analyse des notes
    return html.Div("Sélectionnez une analyse pour afficher les données.")

#------------------------------------------
# Contenu pour l'analyse des Prix
def price_content():
    return html.Div([
        html.H4( style={'textAlign': 'center', 'margin-top': '20px'}),
        html.Div([
            html.Label("Filtrer par genre :", style={'textAlign': 'center', 'margin-right': '10px'}),
            dcc.Dropdown(
                id='price-filter',
                options=[
                    {'label': 'Hommes', 'value': 'men'},
                    {'label': 'Femmes', 'value': 'women'},
                    {'label': 'Les deux', 'value': 'both'}
                ],
                value='both',  # Valeur par défaut
                style={'width': '50%', 'margin': '0 auto'}
            )
        ], style={'textAlign': 'center', 'margin-bottom': '20px'}),
        html.Div(id='price-graph-container', style={'textAlign': 'center'})
    ])

# Callback pour mettre à jour le graphique des prix en fonction du filtre
@callback(
    Output('price-graph-container', 'children'),
    [Input('price-filter', 'value')]
)
def update_price_graph(filter_value):
    if filter_value == 'men':
        return html.Iframe(
            src="/assets/graphes_html/violin_plot_men.html",
            style={"width": "100%", "height": "500px", "border": "1px solid #ddd"}
        )
    elif filter_value == 'women':
        return html.Iframe(
            src="/assets/graphes_html/violin_plot_women.html",
            style={"width": "100%", "height": "500px", "border": "1px solid #ddd"}
        )
    else:
        return html.Iframe(
            src="/assets/graphes_html/violin_plot_combined.html",
            style={"width": "100%", "height": "500px", "border": "1px solid #ddd"}
        )

#------------------------------------------
# Contenu pour l'analyse des Notes des Articles
def rating_content():
    return html.Div([
        html.H4("Sélectionnez une visualisation.", style={'textAlign': 'center', 'margin-top': '20px'}),
        
        # Boutons pour choisir la visualisation
        html.Div([
            html.Button("Nuages de mots", id='btn-wordcloud', n_clicks=0, 
                        style={'margin': '5px', 'padding': '10px', 'font-size': '14px'}),
            html.Button("Relation Prix vs Notes", id='btn-scatter', n_clicks=0, 
                        style={'margin': '5px', 'padding': '10px', 'font-size': '14px'}),
        ], style={'textAlign': 'center', 'margin-bottom': '20px'}),
        
        # Conteneur pour afficher la visualisation sélectionnée
        html.Div(id='rating-visualization-container', style={'textAlign': 'center'})
    ])


@callback(
    Output('rating-visualization-container', 'children'),
    [Input('btn-wordcloud', 'n_clicks'),
     Input('btn-scatter', 'n_clicks')]
)
def update_rating_visualization(btn_wordcloud, btn_scatter):
    # Déterminer quel bouton a été cliqué
    ctx = dash.callback_context

    if not ctx.triggered:
        return html.Div("")  # Par défaut

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'btn-wordcloud':
        # Afficher les deux nuages de mots sous forme d'images
        return html.Div([
            html.Img(
                src="/assets/wordcloud_men.png",
                style={"width": "48%", "margin-right": "10px"}
            ),
            html.Img(
                src="/assets/wordcloud_women.png",
                style={"width": "48%"}
            )
        ], style={'display': 'flex', 'justify-content': 'space-between'})
    elif button_id == 'btn-scatter':
        # Afficher le graphique de relation prix vs notes
        return html.Iframe(
            src="/assets/graphes_html/scatter_price_vs_rating.html",
            style={"width": "100%", "height": "500px", "border": "none"}
        )
    return html.Div("Aucune visualisation sélectionnée.")

#------------------------------------------

# Fonction pour afficher la carte dans Dash
def cartography_content():
    return html.Div([
        html.H3("Cartographie des Magasins UNIQLO à Paris", style={'textAlign': 'center'}),
        html.Iframe(
            src="assets/graphes_html/map_uniqlo.html",  # Chemin de la carte générée
            style={"width": "100%", "height": "600px", "border": "none"}
        )
    ])



