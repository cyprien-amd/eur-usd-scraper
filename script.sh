#!/bin/bash

# Dossier de travail
cd /home/ubuntu

# Fichier de sortie
OUTPUT_FILE="eur_usd_data.csv"

# Timestamp actuel
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Télécharger le HTML
HTML=$(curl -s "https://markets.businessinsider.com/currencies/eur-usd")

# Extraire le prix EUR/USD
PRICE=$(echo "$HTML" | grep -oP '(?<=<span class="price-section__current-value">)[^<]+')

# Créer le fichier si inexistant
if [ ! -f "$OUTPUT_FILE" ]; then
    echo "timestamp,eur_usd" > "$OUTPUT_FILE"
fi

# Ajouter la donnée
if [ -n "$PRICE" ]; then
    echo "$TIMESTAMP,$PRICE" >> "$OUTPUT_FILE"
fi
