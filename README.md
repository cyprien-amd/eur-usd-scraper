# EUR/USD Live Dashboard Project

## Introduction
This project was created as part of a coursework assignment at ESILV. The objective was to develop a complete data pipeline that scrapes live financial data, stores it, and displays it on a professional-looking dashboard accessible via a public URL.

We decided to focus on the EUR/USD exchange rate, using a custom Python script and deploying the entire project on an AWS EC2 instance.

## Project Overview
The dashboard collects and displays EUR/USD price data scraped from [Business Insider](https://markets.businessinsider.com/currencies/eur-usd). It stores the data in a CSV file, automatically updates every 5 minutes using `cron`, and generates a daily financial summary report at 8pm. The report includes key metrics such as opening/closing prices, volatility, return, and more.

## Technologies Used
- Python 3
- Dash (Plotly)
- pandas
- AWS EC2 (Ubuntu 24.04)
- GitHub for version control
- Cron (for scheduling scripts)

## Architecture
- **script.sh**: Scrapes the current EUR/USD rate and appends it to a CSV file.
- **daily_report.py**: Generates a summary of the day's data (volatility, return, etc.) in `report.json`.
- **dashboard.py**: Displays a live dashboard with the price chart, current market status, and daily metrics.
- **cron jobs**:
  - Every 5 minutes: run `script.sh`
  - Every day at 20:00: run `daily_report.py`

## How to Set It Up
### 1. Launch AWS Instance
- Use Ubuntu 24.04 on a t3.micro instance
- Open port 8050 in your security group

### 2. SSH into the instance
```bash
ssh -i key2.pem ubuntu@<YOUR_PUBLIC_IP>
```

### 3. Install requirements
```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install dash pandas
```

### 4. Clone the repo and make the files executable
```bash
git clone https://github.com/cyprien-amd/eur-usd-scraper.git
cd eur-usd-scraper
chmod +x script.sh
```

### 5. Setup cron jobs
Run:
```bash
crontab -e
```
And add:
```bash
*/5 * * * * /home/ubuntu/eur-usd-scraper/script.sh
0 20 * * * python3 /home/ubuntu/eur-usd-scraper/daily_report.py
```

### 6. Run the dashboard
```bash
nohup python3 dashboard.py > dashboard.log 2>&1 &
```
Then visit:
```
http://<YOUR_PUBLIC_IP>:8050
```

## Features
- Live data tracking every 5 minutes
- Interactive line graph
- Real-time clock and market status
- One-click manual refresh
- Daily report section with:
  - Open & Close prices
  - High & Low
  - Mean price
  - Volatility
  - Return (percentage)
  - Observation count

## Author Info
Created by Cyprien Amadieu Carl Aitkaci (IF1) at ESILV as part of the Python / Git / Linux project.

## Future Improvements
- Add more currency pairs (e.g., USD/GBP, USD/JPY)
- Make dashboard mobile-friendly
- Use a database instead of a CSV
- Auto-restart scripts after reboot

---
*Thanks for reading! Feel free to check out the [GitHub repo](https://github.com/cyprien-amd/eur-usd-scraper) for the source code.*

