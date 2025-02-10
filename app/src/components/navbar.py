from dash import html, dcc

 # Barre de navigation
def Navbar():
    return html.Div([
        dcc.Link('Accueil', href='/'),
        dcc.Link('Visualisation', href='/visualisation', style={'marginLeft': '20px'}),
        dcc.Link('À propos', href='/about', style={'marginLeft': '20px'}),
        dcc.Link('Module de Recherche', href='/Search', style={'marginLeft': '20px'})
    ], style={'textAlign': 'center', 'marginTop': '20px', 'fontSize': '18px'}, className="navbar")