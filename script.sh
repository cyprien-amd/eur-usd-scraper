#!/bin/bash

# Dossier de travail
cd /home/ubuntu/eur-usd-scraper

# Fichier de sortie
CSV_FILE="eur_usd_data.csv"

# Timestamp actuel
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Télécharger le HTML depuis Business Insider
HTML=$(curl -s "https://markets.businessinsider.com/currencies/eur-usd")

# Extraire le prix EUR/USD avec une regex
PRICE=$(echo "$HTML" | grep -oP '<span class="price-section__current-value">\K[0-9]+\.[0-9]+')

# Créer le fichier s’il n’existe pas
if [ ! -f "$CSV_FILE" ]; then
    echo "timestamp,eur_usd" > "$CSV_FILE"
fi

# Ajouter la ligne si extraction réussie
if [ -n "$PRICE" ]; then
    echo "$TIMESTAMP,$PRICE" >> "$CSV_FILE"
    echo " $TIMESTAMP - EUR/USD: $PRICE" >> bash_scraper.log
else
    echo " $TIMESTAMP - Price not found" >> bash_scraper.log
fi
