



import pandas as pd
import json
from datetime import datetime

# Charger les donn\u00e9es
df = pd.read_csv("eur_usd_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

# Filtrer les donn\u00e9es du jour
today = datetime.now().date()
df = df[df["timestamp"].dt.date == today]

# Calculs
open_price = df["eur_usd"].iloc[0]
close_price = df["eur_usd"].iloc[-1]
variation = close_price - open_price
min_price = df["eur_usd"].min()
max_price = df["eur_usd"].max()
mean_price = df["eur_usd"].mean()
volatility = df["eur_usd"].std()
count = df.shape[0]

# Cr\u00e9er un dictionnaire
report = {
    "date": str(today),
    "open": round(open_price, 4),
    "close": round(close_price, 4),
    "variation": round(variation, 4),
    "min": round(min_price, 4),
    "max": round(max_price, 4),
    "mean": round(mean_price, 4),
    "volatility": round(volatility, 6),
    "count": count
}

# Sauvegarder en JSON
with open("report.json", "w") as f:
    json.dump(report, f, indent=4)

print("✅ Rapport journalier g\u00e9n\u00e9r\u00e9 avec succ\u00e8s.")
