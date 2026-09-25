# 🌍 Émissions de CO₂ mondiales — Tendances, disparités & corrélations

> Analyser 60 ans d'émissions pour comprendre quels pays, quels secteurs et quels facteurs économiques pèsent le plus.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas&logoColor=white)
![Looker Studio](https://img.shields.io/badge/Looker%20Studio-Dashboard-4285F4?logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Contexte

Le changement climatique est au cœur des enjeux contemporains, mais les dynamiques d'émission varient radicalement d'un pays et d'un secteur à l'autre. Ce projet va au-delà des chiffres globaux pour mettre en lumière les trajectoires par pays, les corrélations avec le développement économique (PIB, population, intensité carbone) et les points de bascule historiques.

## 🎯 Objectifs

- Analyser les tendances d'émission sur 60 ans par grands blocs géographiques
- Identifier les ruptures historiques (chocs pétroliers, protocole de Kyoto, COVID-19)
- Étudier les corrélations PIB × émissions et le découplage dans les pays développés
- Construire un dashboard Looker Studio interactif avec comparateur de pays

## 🔧 Stack technique

| Outil | Usage |
|-------|-------|
| **Python 3.10+** | Langage principal |
| **Pandas** | Manipulation des données |
| **Plotly / Seaborn** | Visualisations exploratoires |
| **Looker Studio** | Dashboard interactif final |

## 📁 Structure du projet

```
02-emissions-co2/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── data/
│   ├── README.md
│   ├── download_data.py
│   ├── raw/                        ← Gitignored
│   ├── processed/                  ← Gitignored
│   └── sample/
├── notebooks/
│   └── 01_eda_emissions.ipynb
├── assets/
└── scripts/
    └── security_check.sh
```

## 🚀 Démarrage rapide

```bash
git clone https://github.com/DiogoA78/02-emissions-co2.git
cd 02-emissions-co2
pip install -r requirements.txt
python data/download_data.py
jupyter notebook notebooks/01_eda_emissions.ipynb
```

## 📊 Dashboard interactif

> [🔗 Voir le dashboard sur Looker Studio](https://datastudio.google.com/reporting/70699da7-6fab-4258-ac49-fd838de70b95)

Le dashboard permet d'explorer les données via 4 pages :
- **Vue d'ensemble** — KPIs mondiaux, évolution globale, top émetteurs
- **Trajectoires par pays** — comparateur multi-pays sur 60 ans
- **Corrélations économiques** — PIB vs. émissions, intensité carbone
- **Décomposition sectorielle** — énergie, transport, industrie, agriculture

## 📄 Source des données

- **Our World in Data — CO₂ and Greenhouse Gas Emissions**
- Mainteneur : Our World in Data / University of Oxford
- Licence : Creative Commons BY
- URL : [github.com/owid/co2-data](https://github.com/owid/co2-data)
- Données complémentaires : Banque Mondiale (PIB, population)

## 📜 Licence

MIT — voir [LICENSE](LICENSE).
