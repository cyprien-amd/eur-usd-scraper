import pandas as pd
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
from datetime import datetime
import pytz

# Créer l'app
app = Dash(_name_)
app.title = "EUR/USD Dashboard"

# Fonction pour recharger les données CSV
def load_data():
    try:
        df = pd.read_csv("eur_usd_data.csv")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except:
        return pd.DataFrame(columns=["timestamp", "eur_usd"])

# Fonction pour savoir si le marché est ouvert
def is_market_open():
    paris = pytz.timezone("Europe/Paris")
    now = datetime.now(paris)
    if now.weekday() == 5 or now.weekday() == 6:  # Samedi ou dimanche
        return False
    if now.weekday() == 4 and now.hour >= 22:
        return False
    if now.weekday() == 6 and now.hour < 23:
        return False
    return True

# Layout
app.layout = html.Div(
    style={"backgroundColor": "#f7f9fc", "color": "#111", "textAlign": "center", "padding": "20px"},
    children=[
        html.H1("EUR/USD Dashboard", style={"marginBottom": "10px"}),

        html.Div(id="live-clock", style={"fontSize": "22px", "marginBottom": "10px"}),

        html.Div(id="market-status", style={"fontSize": "20px", "marginBottom": "20px"}),

        html.Button("🔄 Rafraîchir les données", id="refresh-btn", n_clicks=0),

        dcc.Graph(id="eur-usd-graph"),

        dcc.Interval(id="interval-component", interval=1*1000, n_intervals=0),

        html.Br(),
        html.Div("Cyprien Amadieu Carl Aitkaci - IF1", style={"fontSize": "18px", "color": "#00bfff"})
    ]
)

# Callback : horloge
@app.callback(
    Output("live-clock", "children"),
    Input("interval-component", "n_intervals")
)
def update_clock(n):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Heure actuelle : {now}"

# Callback : statut du marché
@app.callback(
    Output("market-status", "children"),
    Input("interval-component", "n_intervals")
)
def update_market_status(n):
    status = "🟢 Marché ouvert" if is_market_open() else "🔴 Marché fermé"
    return status

# Callback : bouton de rafraîchissement
@app.callback(
    Output("eur-usd-graph", "figure"),
    Input("refresh-btn", "n_clicks")
)
def refresh_graph(n):
    df = load_data()
    if df.empty:
        fig = px.line(title="Aucune donnée")
    else:
        fig = px.line(df, x="timestamp", y="eur_usd", title="EUR/USD Live Tracker")
    return fig

# Lancer l'app
if _name_ == '_main_':
    app.run(host="0.0.0.0", port=8050, debug=False)
