# 📊 Données — CO₂ and Greenhouse Gas Emissions

## Source

- **Éditeur :** Our World in Data / University of Oxford
- **Licence :** Creative Commons BY
- **URL :** [github.com/owid/co2-data](https://github.com/owid/co2-data)

## Téléchargement automatique

```bash
python data/download_data.py
```

## Fichiers

| Fichier | Description | Volume |
|---------|-------------|--------|
| `owid-co2-data.csv` | Dataset principal — émissions par pays et par an | ~50 000 lignes |
| `owid-co2-codebook.csv` | Description de chaque variable | ~80 lignes |

## Variables clés

| Variable | Description |
|----------|-------------|
| `country` | Nom du pays |
| `year` | Année |
| `co2` | Émissions CO₂ totales (Mt) |
| `co2_per_capita` | Émissions par habitant (t) |
| `co2_per_gdp` | Intensité carbone (kg/$ PIB) |
| `population` | Population |
| `gdp` | PIB ($ internationaux 2011) |
| `coal_co2`, `oil_co2`, `gas_co2` | Émissions par source d'énergie |
| `cement_co2`, `flaring_co2` | Émissions industrielles |
| `share_global_co2` | Part des émissions mondiales (%) |

## Structure attendue

```
data/
├── raw/                    ← Gitignored
│   ├── owid-co2-data.csv
│   └── owid-co2-codebook.csv
├── processed/              ← Gitignored
│   └── emissions_looker.csv
└── sample/                 ← Versionné
    └── sample_500.csv
```
