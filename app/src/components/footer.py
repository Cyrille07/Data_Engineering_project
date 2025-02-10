from dash import html


def Footer():
    return html.Footer([
        html.P("Encadré par M. Courivaud", style={'textAlign': 'center', 'fontSize': '14px', 'marginTop': '20px'}),
        html.P("Contact : email1@example.com, email2@example.com", style={'textAlign': 'center', 'fontSize': '14px', 'marginTop': '5px'}),
    ], style={'position': 'relative', 'bottom': '0', 'width': '100%', 'padding': '10px', 'backgroundColor': '#f1f1f1'},
    className="footer")