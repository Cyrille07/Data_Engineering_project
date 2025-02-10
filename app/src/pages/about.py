from dash import html, dcc
def AboutPage():
    return html.Div(
        style={
            "backgroundColor": "#f4f4f4",
            "height": "100vh",
            "fontFamily": "Arial, sans-serif",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "space-between",
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
                    "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.1)",
                },
                children=[
                    # Logos
                    html.Div(
                        style={
                            "display": "flex",
                            "alignItems": "center",
                            "gap": "10px",
                        },
                        children=[
                            html.Img(
                                src="assets/logo-uniqlo1.png",
                                style={"height": "65px"},
                            ),
                            html.Img(
                                src="assets/logo-uniqlo.png",
                                style={"height": "65px"},
                            ),
                        ],
                    ),
                    # Liens de navigation
                    html.Div(
                        style={
                            "display": "flex",
                            "gap": "30px",
                            "fontSize": "20px",
                            "fontWeight": "bold",
                            "justifyContent": "center",
                            "flexGrow": "1",
                        },
                        children=[
                            dcc.Link(
                                "Accueil",
                                href="/home",
                                style={"textDecoration": "none", "color": "#333"},
                            ),
                            dcc.Link(
                                "Visualisation",
                                href="/visualisation",
                                style={"textDecoration": "none", "color": "#333"},
                            ),
                            dcc.Link(
                                "À propos",
                                href="/about",
                                style={
                                    "textDecoration": "none",
                                    "color": "#333",
                                    "fontWeight": "bold",
                                },
                            ),
                        ],
                    ),
                ],
            ),
            # Texte principal
            html.Div(
                style={
                    "margin": "50px auto",
                    "width": "80%",
                    "textAlign": "justify",
                    "lineHeight": "1.8",
                    "color": "#333",
                    "backgroundColor": "#ffffff",
                    "padding": "20px",
                    "borderRadius": "10px",
                    "boxShadow": "0px 2px 10px rgba(0, 0, 0, 0.1)",
                },
                children=[
                    html.H2(
                        "À propos du projet",
                        style={
                            "textAlign": "center",
                            "marginBottom": "20px",
                            "color": "#444",
                        },
                    ),
                    dcc.Markdown(
                        """
                        Ce projet a été réalisé dans le cadre de nos études afin de combiner théorie et **pratique** dans un domaine en pleine évolution : 
                        le **Data Engineering**. En concevant une **application web interactive**, notre objectif était de créer un outil pratique 
                        pour visualiser et analyser les **produits populaires** chez Uniqlo, tout en explorant les **tendances de consommation** par genre.
                        
                        Cette plateforme repose sur des technologies modernes telles que **Dash** et **MongoDB**, et permet de comprendre de manière simple 
                        et intuitive comment les utilisateurs perçoivent les produits en fonction de leurs **notes** et **catégories**.
                        
                        Ce projet a été développé par **Ahmed DIAKITE** et **Bio Anicet Cyrille KOUMA**, sous l’encadrement de Monsieur **Jeremy SURGET** 
                        et son équipe pédagogique.
                        
                        Nous espérons que ce projet sera une source d'inspiration pour d'autres étudiants et professionnels dans le domaine de la 
                        **science des données**. 
                        """,
                        style={"fontSize": "16px", "lineHeight": "1.8"},
                    ),
                ],
            ),
            # Footer
            html.Div(
                style={
                    "backgroundColor": "#ffffff",
                    "padding": "20px 0",
                    "textAlign": "center",
                    "boxShadow": "0px -2px 5px rgba(0, 0, 0, 0.1)",
                },
                children=[
                    html.Div(
                        style={
                            "display": "flex",
                            "flexDirection": "column",
                            "alignItems": "center",
                            "justifyContent": "center",
                        },
                        children=[
                            html.Img(
                                src="assets/logo_Esiee.jpg",
                                style={"height": "60px", "marginBottom": "10px"},
                            ),
                            html.Span(
                                "Encadré par Monsieur Jeremy SURGET et son équipe - ESIEE Paris",
                                style={"fontSize": "14px", "color": "#666"},
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
