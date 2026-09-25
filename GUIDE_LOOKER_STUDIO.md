# 📊 Guide Looker Studio — Émissions de CO₂ mondiales

---

## Colonnes du CSV

Le fichier `emissions_looker.csv` est au grain **pays × année**.

| Colonne | Type | Description |
|---------|------|-------------|
| `Pays` | Texte | Nom du pays |
| `Code_ISO` | Texte | Code ISO 3 lettres (FRA, USA, CHN...) |
| `Annee` | Nombre | Année |
| `Population` | Nombre | Population |
| `PIB` | Nombre | PIB en $ internationaux 2011 |
| `CO2_Total_Mt` | Nombre | Émissions totales (mégatonnes) |
| `CO2_Par_Habitant` | Nombre | Émissions par habitant (tonnes) |
| `Intensite_Carbone` | Nombre | CO₂ par unité de PIB (kg/$) |
| `Part_Mondiale_Pct` | Nombre | Part des émissions mondiales (%) |
| `CO2_Charbon` | Nombre | Émissions dues au charbon (Mt) |
| `CO2_Petrole` | Nombre | Émissions dues au pétrole (Mt) |
| `CO2_Gaz` | Nombre | Émissions dues au gaz (Mt) |
| `CO2_Ciment` | Nombre | Émissions dues au ciment (Mt) |
| `Energie_Par_Habitant` | Nombre | Énergie par habitant (kWh) |

---

## 1. Import dans Google Sheets

1. Google Drive → Nouveau → Google Sheets
2. Fichier → Importer → Upload → `emissions_looker.csv`
3. Vérifications :

| Colonne | Format |
|---------|--------|
| `Annee` | Nombre |
| `Pays`, `Code_ISO` | Texte |
| Toutes les colonnes numériques | Nombre |

---

## 2. Créer le rapport

1. **https://lookerstudio.google.com** → Créer → Rapport
2. Ajouter des données → Google Sheets → ton fichier
3. **Ressource → Gérer les sources → Modifier** → vérifier les types :

| Champ | Type |
|-------|------|
| `Pays` | Texte |
| `Code_ISO` | Texte (ou Géo → Pays si besoin pour la carte) |
| `Annee` | Nombre |
| Toutes les métriques | Nombre |

---

## 3. Champs calculés

**Ressource → Gérer les sources → Modifier → Ajouter un champ calculé**

### Métriques

```
Nom : Total_CO2
Formule : SUM(CO2_Total_Mt)
```

```
Nom : Moy_CO2_Par_Hab
Formule : SUM(CO2_Total_Mt) * 1000000 / SUM(Population)
Note : approximation — utiliser directement AVG(CO2_Par_Habitant) si plus simple
```

```
Nom : CO2_Fossiles
Formule : SUM(CO2_Charbon) + SUM(CO2_Petrole) + SUM(CO2_Gaz)
```

```
Nom : Pct_Charbon
Formule : SUM(CO2_Charbon) / (SUM(CO2_Charbon) + SUM(CO2_Petrole) + SUM(CO2_Gaz))
Type : Pourcentage
```

```
Nom : Pct_Petrole
Formule : SUM(CO2_Petrole) / (SUM(CO2_Charbon) + SUM(CO2_Petrole) + SUM(CO2_Gaz))
Type : Pourcentage
```

```
Nom : Pct_Gaz
Formule : SUM(CO2_Gaz) / (SUM(CO2_Charbon) + SUM(CO2_Petrole) + SUM(CO2_Gaz))
Type : Pourcentage
```

---

## 4. Palette de couleurs

| Usage | Hex |
|-------|-----|
| Accent principal | `#1B5E20` (vert foncé — thème environnement) |
| Accent secondaire | `#43A047` (vert moyen) |
| Alerte / CO₂ élevé | `#D64045` (rouge) |
| Charbon | `#2D3436` (noir) |
| Pétrole | `#D64045` (rouge) |
| Gaz | `#3B7DD8` (bleu) |
| Ciment | `#E8913A` (orange) |
| Fond de page | `#F5F6FA` |
| Texte | `#2D3436` |

Appliquer via **Thème → Personnaliser → Couleurs du rapport**.

---

## 5. Page 1 — Vue d'ensemble mondiale

### Layout

```
┌─────────────────────────────────────────────────────┐
│  🌍 ÉMISSIONS DE CO₂ MONDIALES                       │
├───────────┬───────────┬───────────┬─────────────────┤
│ PAYS      │ CO₂ TOTAL │ CO₂/HAB   │ DERNIÈRE ANNÉE  │
│ ANALYSÉS  │ (Mt)      │ MOY (t)   │                 │
├───────────┴───────────┴───────────┴─────────────────┤
│                                                     │
│  [Graphique lignes : Évolution mondiale]             │
│  Dim = Annee | Métrique = SUM(CO2_Total_Mt)          │
│  Filtré sur Pays = un seul pays global ou somme      │
│                                                     │
├────────────────────────┬────────────────────────────┤
│  [Barres H :           │  [Camembert :              │
│   Top 10 émetteurs]    │   Part mondiale]           │
│  Dim = Pays            │  Dim = Pays                │
│  Métrique = SUM(CO2)   │  Métrique = Part_Mondiale  │
│  Nb barres = 10        │  Top 10                    │
├────────────────────────┴────────────────────────────┤
│ [Filtre] Annee ▼     [Filtre] Pays ▼                │
└─────────────────────────────────────────────────────┘
```

### Visuels

**3 Tableaux-fiches** (Insérer → Tableau, sans dimension, 1 métrique)

| Fiche | Métrique | Détail |
|-------|----------|--------|
| Pays analysés | `COUNT_DISTINCT(Pays)` | Couleur `#1B5E20` |
| CO₂ total | `SUM(CO2_Total_Mt)` | Couleur `#D64045` |
| CO₂/hab moyen | `AVG(CO2_Par_Habitant)` | Couleur `#2D3436` |

Pense à **filtrer chaque fiche sur la dernière année** si tu veux un snapshot :
→ Ajouter un filtre → Inclure `Annee` = 2023 (ou la dernière dispo)

**Graphique lignes — Évolution mondiale**
- Insérer → **Graphique de série temporelle**
- Dimension : `Annee`
- Métrique : `SUM(CO2_Total_Mt)`
- Tri : `Annee` croissant
- Couleur : `#D64045`
- Titre : "Émissions mondiales de CO₂ (Mt)"
- Note : ici on somme tous les pays. Si tu veux juste le "World", filtre sur un pays spécifique ou laisse tous les pays (la somme = le total mondial)

**Top 10 émetteurs**
- Insérer → **Barres horizontales**
- Dimension : `Pays`
- Métrique : `SUM(CO2_Total_Mt)`
- Tri : décroissant
- Style → Nombre de barres : **10**
- Couleur : `#D64045`
- Ajouter un **filtre** : `Annee` = dernière année disponible
- Titre : "Top 10 émetteurs"

**Camembert — Part mondiale**
- Insérer → **Graphique à secteurs**
- Dimension : `Pays`
- Métrique : `SUM(Part_Mondiale_Pct)` ou `SUM(CO2_Total_Mt)`
- Filtre : `Annee` = dernière année
- Style → Nombre de tranches : **10**
- Titre : "Part des émissions mondiales"

**Filtres**
- Contrôle liste déroulante : `Annee`
- Contrôle liste déroulante : `Pays` (sélection multiple)
- Portée → **Rapport** (pour filtrer toutes les pages)

---

## 6. Page 2 — Trajectoires par pays

### Layout

```
┌─────────────────────────────────────────────────────┐
│  📈 TRAJECTOIRES PAR PAYS                            │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [Graphique lignes : CO₂ total multi-pays]           │
│  Dim = Annee | Répartition = Pays                    │
│  Métrique = SUM(CO2_Total_Mt)                        │
│                                                     │
├────────────────────────┬────────────────────────────┤
│  [Lignes : CO₂/hab     │  [Lignes : Intensité       │
│   multi-pays]           │   carbone multi-pays]      │
│  Métrique =             │  Métrique =                │
│  AVG(CO2_Par_Habitant)  │  AVG(Intensite_Carbone)    │
├────────────────────────┴────────────────────────────┤
│  [Tableau : Comparaison chiffrée]                    │
│  Dim = Pays | Métriques = CO2, CO2/hab, Int. carb.  │
├─────────────────────────────────────────────────────┤
│  [Filtre] Pays ▼ (sélection multiple)               │
└─────────────────────────────────────────────────────┘
```

### Visuels

**Graphique lignes — CO₂ total multi-pays**
- Insérer → **Graphique de série temporelle**
- Dimension temporelle : `Annee`
- Dimension de répartition : `Pays`
- Métrique : `SUM(CO2_Total_Mt)`
- Titre : "Émissions CO₂ totales — Comparaison"
- Le visiteur utilise le filtre `Pays` pour choisir quels pays comparer

**Graphique lignes — CO₂ par habitant**
- Même structure
- Métrique : `AVG(CO2_Par_Habitant)`
- Titre : "CO₂ par habitant — Comparaison"

**Graphique lignes — Intensité carbone**
- Même structure
- Métrique : `AVG(Intensite_Carbone)`
- Titre : "Intensité carbone (CO₂/PIB) — Comparaison"

**Tableau comparatif**
- Insérer → **Tableau**
- Dimension : `Pays`
- Métriques :
  - `SUM(CO2_Total_Mt)` — renommer "CO₂ total (Mt)"
  - `AVG(CO2_Par_Habitant)` — renommer "CO₂/hab (t)"
  - `AVG(Intensite_Carbone)` — renommer "CO₂/PIB (kg/$)"
  - `SUM(Population)` — renommer "Population"
- Filtre : dernière année
- Style → Heatmap sur la colonne CO₂ total
- Titre : "Comparaison chiffrée"

**Filtre clé de cette page**
- Contrôle liste déroulante : `Pays` → **sélection multiple activée**
- Pré-sélectionner 5-6 pays par défaut (France, Allemagne, USA, Chine, Inde, Brésil)
- Ce filtre rend la page interactive : le visiteur compose sa propre comparaison

---

## 7. Page 3 — Corrélations économiques

### Layout

```
┌─────────────────────────────────────────────────────┐
│  💰 CORRÉLATIONS ÉCONOMIQUES                         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [Scatter : PIB vs. CO₂/hab]                         │
│  X = PIB | Y = CO2_Par_Habitant                      │
│  Taille = Population | Couleur = CO2_Par_Habitant    │
│                                                     │
├────────────────────────┬────────────────────────────┤
│  [Lignes : Évolution   │  [Barres H :              │
│   intensité carbone]   │   Top 15 CO₂/hab]         │
│  Dim = Annee           │  Dim = Pays               │
│  Répartition = Pays    │  Métrique = CO2_Par_Hab   │
├────────────────────────┴────────────────────────────┤
│  [Tableau : Pays à forte intensité carbone]          │
│  Dim = Pays | Métriques = CO2, PIB, Intensité       │
└─────────────────────────────────────────────────────┘
```

### Visuels

**Scatter — PIB vs. CO₂ par habitant**
- Insérer → **Graphique à nuage de points**
- Dimension : `Pays`
- Métrique X : `SUM(PIB)` ou `AVG(PIB)`
- Métrique Y : `AVG(CO2_Par_Habitant)`
- Métrique taille (bulle) : `SUM(Population)`
- Filtre : dernière année + `Population` > 1 000 000
- Titre : "PIB vs. CO₂ par habitant"
- Astuce : dans Style → cocher **Afficher les libellés** pour voir les noms de pays

**Lignes — Intensité carbone multi-pays**
- Insérer → **Graphique de série temporelle**
- Dimension : `Annee`
- Répartition : `Pays`
- Métrique : `AVG(Intensite_Carbone)`
- Titre : "Évolution de l'intensité carbone"

**Barres H — Top 15 CO₂ par habitant**
- Insérer → **Barres horizontales**
- Dimension : `Pays`
- Métrique : `AVG(CO2_Par_Habitant)`
- Tri : décroissant
- Nombre de barres : **15**
- Filtre : dernière année + `Population` > 1 000 000
- Couleur : dégradé `#43A047` → `#D64045`
- Titre : "Top 15 — CO₂ par habitant"

**Tableau — Détail intensité**
- Insérer → **Tableau**
- Dimension : `Pays`
- Métriques : `AVG(CO2_Par_Habitant)`, `AVG(Intensite_Carbone)`, `SUM(CO2_Total_Mt)`, `SUM(PIB)`
- Filtre : dernière année
- Tri : `AVG(Intensite_Carbone)` décroissant
- Style → Heatmap sur Intensité carbone
- Titre : "Pays à forte intensité carbone"

---

## 8. Page 4 — Sources d'énergie

### Layout

```
┌─────────────────────────────────────────────────────┐
│  ⛽ DÉCOMPOSITION PAR SOURCE D'ÉNERGIE               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [Barres empilées : Sources par année]               │
│  Dim = Annee                                         │
│  Métriques = CO2_Charbon, CO2_Petrole, CO2_Gaz,     │
│              CO2_Ciment                               │
│                                                     │
├────────────────────────┬────────────────────────────┤
│  [Camembert :           │  [Barres empilées :        │
│   Répartition sources]  │   Sources par pays]        │
│  Dernière année         │  Dim = Pays | Top 10       │
│  Monde entier           │  Répartition = sources     │
├────────────────────────┴────────────────────────────┤
│                                                     │
│  [Tableau : Détail par pays et source]               │
│  Dim = Pays                                          │
│  Métriques = Charbon, Pétrole, Gaz, Ciment, Total   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Visuels

**Barres empilées — Sources par année (monde)**
- Insérer → **Graphique à barres verticales empilées**
- Dimension : `Annee`
- Métriques (dans cet ordre) :
  - `SUM(CO2_Charbon)` → couleur `#2D3436` (noir)
  - `SUM(CO2_Petrole)` → couleur `#D64045` (rouge)
  - `SUM(CO2_Gaz)` → couleur `#3B7DD8` (bleu)
  - `SUM(CO2_Ciment)` → couleur `#E8913A` (orange)
- Titre : "Émissions mondiales par source d'énergie"
- Insight : le charbon domine encore, mais le gaz progresse

**Camembert — Répartition sources (dernière année)**
- Insérer → **Graphique à secteurs**
- Créer **4 métriques** :
  - `SUM(CO2_Charbon)`, `SUM(CO2_Petrole)`, `SUM(CO2_Gaz)`, `SUM(CO2_Ciment)`
- Filtre : dernière année
- Couleurs : noir, rouge, bleu, orange
- Titre : "Répartition par source"

Note : Looker Studio ne fait pas facilement un camembert avec plusieurs métriques.
Alternative : créer un **tableau** avec une seule ligne (pas de dimension) et les 4 métriques,
puis activer le **graphique en anneau** via un champ calculé ou simplement utiliser un
graphique à barres horizontales empilé à 100%.

**Barres empilées — Top 10 pays par source**
- Insérer → **Barres horizontales empilées**
- Dimension : `Pays`
- Métriques : `SUM(CO2_Charbon)`, `SUM(CO2_Petrole)`, `SUM(CO2_Gaz)`, `SUM(CO2_Ciment)`
- Tri : `SUM(CO2_Total_Mt)` décroissant
- Nombre de barres : **10**
- Filtre : dernière année
- Titre : "Top 10 émetteurs — par source d'énergie"
- Insight : la Chine est dominée par le charbon, les USA par le pétrole

**Tableau détaillé**
- Insérer → **Tableau**
- Dimension : `Pays`
- Métriques :
  - `SUM(CO2_Charbon)` → "Charbon (Mt)"
  - `SUM(CO2_Petrole)` → "Pétrole (Mt)"
  - `SUM(CO2_Gaz)` → "Gaz (Mt)"
  - `SUM(CO2_Ciment)` → "Ciment (Mt)"
  - `SUM(CO2_Total_Mt)` → "Total (Mt)"
- Filtre : dernière année
- Tri : Total décroissant
- Style → Heatmap sur chaque colonne
- Titre : "Détail par pays et source"

---

## 9. Touches finales

### Thème
- Police : **Roboto**
- Fond : `#F5F6FA`
- Bande de titre : rectangle `#1B5E20` (vert foncé) + texte blanc

### Filtres globaux
- Vérifier que `Annee` et `Pays` sont en portée **Rapport**
- Le filtre `Pays` en sélection multiple est la clé de ce dashboard

### Partage
1. Bouton **Partager** → "Obtenir le lien"
2. "Toute personne disposant du lien peut consulter"
3. Copier le lien → portfolio

### Captures d'écran
Sauvegarder dans `assets/` :
- `dashboard_page1_overview.png`
- `dashboard_page2_trajectoires.png`
- `dashboard_page3_correlations.png`
- `dashboard_page4_sources.png`

---

## 10. Checklist

```
□ 4 pages créées avec titres cohérents
□ Fiches de score sur la page d'accueil
□ Filtres Annee et Pays fonctionnels et en portée Rapport
□ Palette vert/rouge cohérente
□ Tri correct (Annee croissant, barres décroissantes)
□ Scatter PIB vs CO₂ lisible (libellés activés)
□ Barres empilées avec les bonnes couleurs par source
□ Lien de partage public
□ Captures dans assets/
□ Lien dans le README
```
