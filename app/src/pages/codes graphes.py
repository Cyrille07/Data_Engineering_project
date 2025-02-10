from matplotlib import pyplot as plt
# from wordcloud import WordCloud
from pymongo import MongoClient
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import mpld3
import os


#connexion à mongo DB
client = MongoClient()
db_uniqlo = client.uniqlo
db_uniqlo_clothes = db_uniqlo["Clothes"]



# Extraction des données
data_sun_hist = list(db_uniqlo_clothes.find())
# Conversion en DataFrame
df_sun_hist = pd.DataFrame(data_sun_hist)

# Filtrer les données pour les catégories et les sexes nécessaires
categories = ['sweater', 'outwear', 'bottom']
df_filtered = df_sun_hist[df_sun_hist['type'].isin(categories) & df_sun_hist['sexe'].isin(['men', 'women'])]

# Calculer le nombre d'articles par catégorie et sexe
category_counts = df_filtered.groupby(['sexe', 'type']).size().unstack(fill_value=0)


# sunburst
data_sunburst=dict( 
    labels = ["men", "women", "Bottom", "Outwear", "Sweater", "bottom","outwear","sweater"],
    parent = ["","", "men", "men", "men", "women", "women", "women"],
    value = [156, 173, 72, 60, 24, 72, 51, 50]  ) 
fig = px.sunburst(
    data_sunburst,
    names='labels',
    parents='parent',
    values='value',
)
fig.update_layout(
    title={
        'text': "Distribution des articles par sexe et catégorie",
        'y':0.95,  # Augmenter légèrement la position du titre
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    margin=dict(t=100, l=0, r=0, b=0)  # Augmenter la marge supérieure pour le titre
)
# Réduire la taille du sunburst pour éviter le chevauchement
fig.update_traces(
    marker=dict(line=dict(width=1)),
    insidetextorientation='radial'
)

fig.write_html("app/assets/graphes_html/sunburst_chart.html")


#Histogramme 

data_histo = {
    "Sexe": ["men", "men", "men", "women", "women", "women"],
    "Catégorie": ["bottom", "outwear", "sweater", "bottom", "outwear", "sweater"],
    "Nombre d'articles": [72, 60, 24, 72, 51, 50]
}
fig = px.bar(
    data_histo,
    x="Sexe",
    y="Nombre d'articles",
    color="Catégorie",
    title="Nombre d'articles par Catégorie et Sexe",
    labels={"Sexe": "Gender", "Nombre d'articles": "Number of Items", "Catégorie": "Category"},
    text_auto=True
)
fig.write_html("app/assets/graphes_html/stacked_bar_chart.html")


#-----------------------------------------------
#GRAPHE SUR LES PRIX

    #Homme
# Filtrer les données pour "men" et les catégories "bottom", "sweater", "outwear"
query = {"sexe": "men", "type": {"$in": ["bottom", "sweater", "outwear"]}}
projection = {"_id": 0, "type": 1, "price": 1}  

data_men_violin = list(db_uniqlo_clothes.find(query, projection))
df_men_violin = pd.DataFrame(data_men_violin)

#violin plot
fig = px.violin(
    df_men_violin,
    x="type",  
    y="price",  
    title="Distribution des prix des articles pour 'men'",
    labels={"type": "Category", "price": "Price"},
    box=True,  
    points="all"  
)
fig.write_html("app/assets/graphes_html/violin_plot_men.html")

    
    
    #FEMME
# Filtrer les données pour "women" et les catégories "bottom", "sweater", "outwear"
query = {"sexe": "women", "type": {"$in": ["bottom", "sweater", "outwear"]}}
projection = {"_id": 0, "type": 1, "price": 1}  

data_women_violin = list(db_uniqlo_clothes.find(query, projection))
df_women_violin = pd.DataFrame(data_women_violin)

#violin plot
fig = px.violin(
    df_women_violin,
    x="type",  
    y="price",  
    title="Distribution des prix des articles pour 'women'",
    labels={"type": "Category", "price": "Price"},
    box=True,  
    points="all",  
    color_discrete_sequence=["red"]
)
fig.write_html("app/assets/graphes_html/violin_plot_women.html")


    #Combiné
query_men = {"sexe": "men", "type": {"$in": ["bottom", "sweater", "outwear"]}}
projection = {"_id": 0, "type": 1, "price": 1, "sexe": 1}
data_men = list(db_uniqlo_clothes.find(query_men, projection))

query_women = {"sexe": "women", "type": {"$in": ["bottom", "sweater", "outwear"]}}
data_women = list(db_uniqlo_clothes.find(query_women, projection))

df_combined = pd.DataFrame(data_men + data_women)

#violin plot combiné
fig = px.violin(
    df_combined,
    x="type",  
    y="price",  
    color="sexe",  
    title="Distribution des prix des articles pour hommes et femmes",
    labels={"type": "Category", "price": "Price", "sexe": "Gender"},
    box=True,   
    color_discrete_map={"men": "blue", "women": "red"},  
    points="all",  
    violinmode="group"  
)
fig.update_traces(width=0.6)
fig.write_html("app/assets/graphes_html/violin_plot_combined.html")



#--------------------------------------------------
# GRAPHE 1 : Nuage de points (Prix vs Notes)

# Filtrer les données pour les catégories et les évaluations
query = {"type": {"$in": ["bottom", "sweater", "outwear"]}, "rate": {"$exists": True}}
projection = {"_id": 0, "type": 1, "price": 1, "rate": 1, "sexe": 1}

data_scatter = list(db_uniqlo_clothes.find(query, projection))
df_scatter = pd.DataFrame(data_scatter)

# Créer un nuage de points
fig = px.scatter(
    df_scatter,
    x="price",
    y="rate",
    color="sexe",
    title="Relation entre Prix et rate par Sexe",
    labels={"price": "Prix", "rate": "rate", "sexe": "Sex"},
    hover_data=["type"],
    color_discrete_map={"men": "blue", "women": "red"}
)
fig.update_traces(marker=dict(size=8))
fig.write_html("app/assets/graphes_html/scatter_price_vs_rating.html")

#--------------------------------------------------
# GRAPHE 2 : Bar Chart (Moyennes des Notes)
# Calculer les moyennes des évaluations par catégorie et par sexe

query = {"type": {"$in": ["bottom", "sweater", "outwear"]}, "rate": {"$exists": True}}
data_bar = list(db_uniqlo_clothes.find(query, projection))
df_bar = pd.DataFrame(data_bar)

# Grouper les données pour calculer les moyennes
mean_ratings = df_bar.groupby(["sexe", "type"])["rate"].mean().reset_index()
mean_ratings.rename(columns={"rate": "Évaluation Moyenne"}, inplace=True)

# Créer le graphique en barres
fig = px.bar(
    mean_ratings,
    x="type",
    y="Évaluation Moyenne",
    color="sexe",
    barmode="group",
    title="Moyennes des Évaluations par Catégorie et Sexe",
    labels={"type": "Catégorie", "Évaluation Moyenne": "Évaluation Moyenne", "sexe": "Sexe"},
    color_discrete_map={"men": "blue", "women": "red"},
    text_auto=True
)
fig.write_html("app/assets/graphes_html/bar_chart_average_ratings.html")


""""
#Nuage de mots, articles attrayants, WORDCLOUD


# Répertoire de sortie
output_dir = "app/graphes_html/"
os.makedirs(output_dir, exist_ok=True)

# Fonction pour créer un nuage de mots et sauvegarder en HTML
def generate_wordcloud_html(dataframe, title, output_file, colormap):
    text = " ".join(dataframe['name'])
    
    # Générer le nuage de mots
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap=colormap
    ).generate(text)
    
    # Matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    
    # Supprimer les axes, les ticks et les spines
    ax.axis("off")
    ax.set_title(title, fontsize=20, fontweight="bold", color="black", pad=20)

    
    # Sauvegarde en HTML
    mpld3.save_html(fig, output_file)
    plt.close(fig)
    print(f"Nuage de mots sauvegardé en HTML : {output_file}")

# Générer le nuage de mots pour les femmes
def process_women_wordcloud():
    query_women = {
        "sexe": "women", 
        "rate": {"$gte": 4.5},  # Notes maximales
        "price": {"$lt": 50}    # Prix attractifs
    }
    data_women = list(db_uniqlo_clothes.find(query_women, {"_id": 0, "name": 1}))
    df_women = pd.DataFrame(data_women)

    if not df_women.empty:
        generate_wordcloud_html(
            df_women,
            "Articles Populaires pour Femmes",
            os.path.join(output_dir, "wordcloud_women.html"),
            colormap="Reds"
        )
    else:
        print("Aucun article populaire pour les femmes.")

# Générer le nuage de mots pour les hommes
def process_men_wordcloud():
    query_men = {
        "sexe": "men", 
        "rate": {"$gte": 4.5},  # Notes maximales
        "price": {"$lt": 50}    # Prix attractifs
    }
    data_men = list(db_uniqlo_clothes.find(query_men, {"_id": 0, "name": 1}))
    df_men = pd.DataFrame(data_men)

    if not df_men.empty:
        generate_wordcloud_html(
            df_men,
            "Articles Populaires pour Hommes",
            os.path.join(output_dir, "wordcloud_men.html"),
            colormap="Blues"
        )
    else:
        print("Aucun article populaire pour les hommes.")

# Exécution des nuages de mots
process_women_wordcloud()
process_men_wordcloud()

"""
#-----------------
import folium

magasins = ["UNIQLO ITALIE 2", "UNIQLO MONTPARNASSE", "UNIQLO SAINT-GERMAIN-DES-PRÉS",
            "UNIQLO RIVOLI", "UNIQLO LE MARAIS", "UNIQLO PRINTEMPS NATION", "UNIQLO PARIS OPÉRA",
            "UNIQLO BEAUGRENELLE", "UNIQLO PASSY PLAZA", "UNIQLO SO OUEST", "UNIQLO LA DÉFENSE"]

latitudes = [48.82, 48.84, 48.85, 48.8592, 48.857, 48.857, 48.873, 48.849, 48.857, 48.892, 48.892]
longitudes = [2.35, 2.32, 2.33, 2.34, 2.36, 2.401, 2.330, 2.282, 2.279, 2.296, 2.238]

# Création de la carte centrée sur Paris
map_paris = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Ajout des marqueurs pour chaque magasin
for magasin, lat, lon in zip(magasins, latitudes, longitudes):
    folium.Marker(
        location=[lat, lon],
        popup=magasin,
        icon=folium.Icon(color="red", icon="shopping-cart", prefix="fa")
    ).add_to(map_paris)

# Sauvegarde et affichage de la carte
map_paris.save("app/assets/graphes_html/map_uniqlo.html")

# Fermer la connexion MongoDB

