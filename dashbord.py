



import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import json
from datetime import datetime
import plotly.express as px

# Charger les données
df = pd.read_csv("eur_usd_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Charger les données du rapport journalier
try:
    with open("report.json") as f:
        report = json.load(f)
except:
    report = {
        "date": "N/A", "open": "N/A", "close": "N/A",
        "variation": "N/A", "min": "N/A", "max": "N/A",
        "mean": "N/A", "volatility": "N/A", "count": "N/A"
    }

# App
app = dash.Dash(_name_)
server = app.server

# Couleur marché ouvert/fermé
now = datetime.now()
market_open = now.hour >= 9 and now.hour < 17
market_status_color = "green" if market_open else "red"
market_status_text = "Marché ouvert" if market_open else "Marché fermé"

# Graphique
fig = px.line(df, x="timestamp", y="eur_usd", title="EUR/USD Live Tracker")

# Layout
app.layout = html.Div(style={"backgroundColor": "#f7f9fc", "padding": "30px"}, children=[
    html.H1("EUR/USD Dashboard", style={"textAlign": "center", "color": "#000"}),
    html.H4(f"Heure actuelle : {now.strftime('%Y-%m-%d %H:%M:%S')}", style={"textAlign": "center"}),
    html.Div([
        html.Span("●", style={"color": market_status_color, "fontSize": "24px", "paddingRight": "5px"}),
        html.Span(market_status_text, style={"fontSize": "20px", "color": market_status_color})
    ], style={"textAlign": "center", "marginBottom": "20px"}),

    html.Div([
        html.Button("🔄 Rafraîchir les données", id="refresh-btn", n_clicks=0)
    ], style={"textAlign": "center", "marginBottom": "20px"}),

    dcc.Graph(figure=fig),

    html.Div([
        html.H2("📊 Rapport du jour", style={"textAlign": "center", "marginTop": "30px"}),

        html.Div([
            html.Div([
                html.H4("Open"), html.P(report["open"])
            ], className="metric"),
            html.Div([
                html.H4("Close"), html.P(report["close"])
            ], className="metric"),
            html.Div([
                html.H4("Variation"), html.P(report["variation"])
            ], className="metric"),
            html.Div([
                html.H4("Min"), html.P(report["min"])
            ], className="metric"),
            html.Div([
                html.H4("Max"), html.P(report["max"])
            ], className="metric"),
            html.Div([
                html.H4("Moyenne"), html.P(report["mean"])
            ], className="metric"),
            html.Div([
                html.H4("Volatility"), html.P(report["volatility"])
            ], className="metric"),
            html.Div([
                html.H4("N obs"), html.P(report["count"])
            ], className="metric"),
        ], style={"display": "flex", "flexWrap": "wrap", "justifyContent": "center", "gap": "20px",
                  "marginTop": "20px"}),

        html.P("Cyprien Amadieu Carl Aitkaci - IF1", style={"textAlign": "center", "marginTop": "40px", "color": "#00bfff"})
    ])
])

# CSS pour les blocs
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>EUR/USD Dashboard</title>
        {%favicon%}
        {%css%}
        <style>
            .metric {
                background-color: #e6f0ff;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                min-width: 120px;
            }
            .metric h4 {
                margin: 5px;
                font-size: 18px;
                color: #003366;
            }
            .metric p {
                margin: 0;
                font-weight: bold;
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if _name_ == '_main_':
    app.run(debug=False, port=8050, host="0.0.0.0")
