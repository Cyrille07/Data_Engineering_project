from dash import html, dcc

def HomePage():
    return html.Div(
        style={
            "backgroundColor": "#f4f4f4",  # Couleur de fond inspirée
            "height": "100vh",
            "fontFamily": "Arial, sans-serif"
        },
        children=[
            # Navbar
            html.Div(
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "space-between",
                    "padding": "10px 20px",
                    "backgroundColor": "#ffffff",
                    "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.1)"
                },
                children=[
                    # Logos
                    html.Div(
                        style={
                            "display": "flex",
                            "alignItems": "center",
                            "gap": "10px"  # Espacement entre les deux logos
                        },
                        children=[
                            html.Img(
                                src="assets/logo-uniqlo1.png", 
                                style={"height": "65px"}  # Taille du premier logo
                            ),
                            html.Img(
                                src="assets/logo-uniqlo.png",  
                                style={"height": "65px"}  # Taille du deuxième logo
                            )
                        ]
                    ),
                    # Liens de navigation
                    html.Div(
                        style={
                            "display": "flex",
                            "gap": "30px",
                            "fontSize": "20px",
                            "fontWeight": "bold",
                            "justifyContent": "center",
                            "flexGrow": "1"
                        },
                        children=[
                            dcc.Link("Accueil", href="/home", style={"textDecoration": "none", "color": "#333"}),
                            dcc.Link("Visualisation", href="/visualisation", style={"textDecoration": "none", "color": "#333"}),
                            dcc.Link("À propos", href="/about", style={"textDecoration": "none", "color": "#333"}),
                            dcc.Link("Module de Recherche", href="/search", style={"textDecoration": "none", "color": "#333"})
                        ]
                    ),
                ]
            ),
            
            # Message central
            html.Div(
                style={
                    "textAlign": "center",
                    "marginTop": "100px",
                    "padding": "20px"
                },
                children=[
                    html.H1(
                        "Bienvenue sur notre Dashboard Uniqlo",
                        style={
                            "fontSize": "48px",
                            "color": "#333"
                        }
                    ),
                    html.P(
                        "Analyse des prix et avis en un clic !",
                        style={
                            "fontSize": "25px",
                            "marginTop": "10px",
                            "color": "#e60012",  # Rouge Uniqlo
                            "fontWeight": "bold"
                        }
                    ),
                ]
            ),
            
            # Footer
            html.Footer(
                style={
                    "position": "absolute",  # Fixe le footer en bas
                    "bottom": "0",
                    "width": "100%",
                    "backgroundColor": "#ffffff",
                    "padding": "10px 20px",
                    "textAlign": "center",
                    "boxShadow": "0px -2px 5px rgba(0, 0, 0, 0.1)"
                },
                children=[
                    # Logo ESIEE dans le footer
                    html.Div(
                        style={"marginBottom": "10px"},
                        children=[
                            html.Img(
                                src="assets/logo_Esiee.jpg",
                                style={"height": "55px"}
                            )
                        ]
                    ),
                    # Mention de l'encadrant
                    html.P(
                        "Encadré par M. Jeremy SURGET",
                        style={"fontSize": "14px", "color": "#777", "marginBottom": "5px"}
                    ),
                    # Contacts
                    html.P(
                        "Contact : ahmed.diakite@edu.esiee.fr, bio.kouma@edu.esiee.fr",
                        style={"fontSize": "14px", "color": "#777"}
                    )
                ]
            ),
        ]
    )
