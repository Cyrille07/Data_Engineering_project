from dash import html

def Header():
    return html.Div(
        children=[
            html.H1("Tableau de Bord Cartographique"),
            html.Hr()
        ],
        className="header"
    )
