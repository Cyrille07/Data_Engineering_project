import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import src.pages.visualisation as visualisation 
import src.pages.home as home 
import src.pages.about as about 
import src.pages.recherche as recherche

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Mise en page principale
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
])

# Callback pour afficher la page en fonction de l'URL
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/about":
        return about.AboutPage()
    elif pathname == "/home" or pathname == "/":  # Inclure "/" comme accueil par défaut
        return home.HomePage()
    elif pathname == "/visualisation":
        return visualisation.VisuPage()  # Appel à la page de visualisation
    elif pathname == "/search":
        return recherche.SearchPage()
    else:
        return home.HomePage()  # Page d'accueil par défaut

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
