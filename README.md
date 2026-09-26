🇫🇷 [Version française](README_FR.md)

# 🌍 Global CO₂ Emissions — Trends, Disparities & Correlations

> Analyzing 60 years of emissions to understand which countries, sectors, and economic factors weigh the most.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas&logoColor=white)
![Looker Studio](https://img.shields.io/badge/Looker%20Studio-Dashboard-4285F4?logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Context

Climate change is at the heart of contemporary challenges, but emission dynamics vary drastically from one country and sector to another. This project goes beyond global figures to highlight country-level trajectories, correlations with economic development (GDP, population, carbon intensity), and historical tipping points.

## 🎯 Objectives

- Analyze emission trends over 60 years by major geographic blocs
- Identify historical turning points (oil crises, Kyoto Protocol, COVID-19)
- Study GDP × emissions correlations and decoupling in developed countries
- Build an interactive Looker Studio dashboard with a country comparator

## 🔧 Tech Stack

| Tool | Usage |
|------|-------|
| **Python 3.10+** | Main language |
| **Pandas** | Data manipulation |
| **Plotly / Seaborn** | Exploratory visualizations |
| **Looker Studio** | Final interactive dashboard |

## 📁 Project Structure

```
02-emissions-co2/
├── README.md                          ← This file
├── README_FR.md                       ← French version
├── requirements.txt
├── .gitignore
├── LICENSE
├── data/
│   ├── README.md
│   ├── download_data.py
│   ├── raw/                           ← Gitignored
│   ├── processed/                     ← Gitignored
│   └── sample/
├── notebooks/
│   └── 01_eda_emissions.ipynb
├── assets/
└── scripts/
    └── security_check.sh
```

## 🚀 Quick Start

```bash
git clone https://github.com/DiogoA78/02-emissions-co2.git
cd 02-emissions-co2
pip install -r requirements.txt
python data/download_data.py
jupyter notebook notebooks/01_eda_emissions.ipynb
```

## 📊 Interactive Dashboard

> [🔗 View the dashboard on Looker Studio](https://datastudio.google.com/reporting/70699da7-6fab-4258-ac49-fd838de70b95)

The dashboard allows data exploration through 4 pages:
- **Overview** — Global KPIs, overall trends, top emitters
- **Country Trajectories** — Multi-country comparator over 60 years
- **Economic Correlations** — GDP vs. emissions, carbon intensity
- **Sector Breakdown** — energy, transport, industry, agriculture

## 📄 Data Source

- **Our World in Data — CO₂ and Greenhouse Gas Emissions**
- Maintainer: Our World in Data / University of Oxford
- License: Creative Commons BY
- URL: [github.com/owid/co2-data](https://github.com/owid/co2-data)
- Supplementary data: World Bank (GDP, population)

## 📜 License

MIT — see [LICENSE](LICENSE).
