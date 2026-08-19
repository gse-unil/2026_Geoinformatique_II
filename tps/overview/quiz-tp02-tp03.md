# Quiz CodeRunner — TP2 & TP3 Python (Géoinformatique II)

Questions de code à soumettre dans Moodle CodeRunner.  
Chaque question indique : l'énoncé, le code de départ fourni à l'étudiant·e,
la réponse attendue, et les cas de test automatiques.

> **Convention** : les questions sont indépendantes sauf mention contraire.
> Toutes les données proviennent de `tp1.gpkg` (TP2) ou de rasters synthétiques (TP3).

---

## Partie A — TP2 : Sélections, Jointures et Requêtes spatiales

---

### Q1 — Filtrage booléen simple

**Difficulté** : ★☆☆  
**Concept** : sélection par attribut

**Énoncé**

La variable `towns` est un GeoDataFrame chargé depuis `tp1.gpkg` (couche `Towns`).
Elle contient les colonnes `ID1` (nom de la ville) et `Population` (nombre d'habitants).

Complète le code ci-dessous pour créer la variable `grandes_villes` contenant
uniquement les villes dont la population dépasse **100 000 habitants**.

**Code de départ (fourni à l'étudiant·e)**

```python
import geopandas as gpd
towns = gpd.read_file('tp1.gpkg', layer='Towns')

# Complète cette ligne :
grandes_villes = ___
```

**Réponse attendue**

```python
import geopandas as gpd
towns = gpd.read_file('tp1.gpkg', layer='Towns')

grandes_villes = towns[towns['Population'] > 100_000]
```

**Cas de test**

```python
# Test 1 — type correct
assert hasattr(grandes_villes, 'geometry'), "grandes_villes doit être un GeoDataFrame"

# Test 2 — toutes les villes respectent le filtre
assert (grandes_villes['Population'] > 100_000).all(), \
    "Certaines villes ont une population ≤ 100 000"

# Test 3 — aucune ville ≤ 100 000 n'a été incluse
assert len(grandes_villes) == len(towns[towns['Population'] > 100_000]), \
    "Le nombre de villes ne correspond pas"
```

---

### Q2 — Filtrage avec condition multiple et `.isin()`

**Difficulté** : ★★☆  
**Concept** : opérateurs `&`, `|`, `.isin()`

**Énoncé**

À partir du GeoDataFrame `towns` (colonnes : `ID1`, `Population`, `Rank`),
crée une variable `selection` contenant les villes qui satisfont **les deux**
conditions suivantes :

- La population est comprise entre **20 000** et **80 000** habitants inclus.
- Le nom de la ville (`ID1`) figure dans la liste `['Biel/Bienne', 'Thun', 'Köniz', 'Winterthur', 'St. Gallen']`.

**Code de départ**

```python
import geopandas as gpd
towns = gpd.read_file('tp1.gpkg', layer='Towns')
noms_cibles = ['Biel/Bienne', 'Thun', 'Köniz', 'Winterthur', 'St. Gallen']

# Complète :
selection = ___
```

**Réponse attendue**

```python
import geopandas as gpd
towns = gpd.read_file('tp1.gpkg', layer='Towns')
noms_cibles = ['Biel/Bienne', 'Thun', 'Köniz', 'Winterthur', 'St. Gallen']

selection = towns[
    (towns['Population'] >= 20_000) &
    (towns['Population'] <= 80_000) &
    towns['ID1'].isin(noms_cibles)
]
```

**Cas de test**

```python
# Test 1 — toutes les villes sont dans la liste cible
assert set(selection['ID1']).issubset(set(noms_cibles))

# Test 2 — toutes les villes respectent le filtre de population
assert (selection['Population'] >= 20_000).all()
assert (selection['Population'] <= 80_000).all()

# Test 3 — résultat attendu
expected = towns[
    (towns['Population'] >= 20_000) &
    (towns['Population'] <= 80_000) &
    towns['ID1'].isin(noms_cibles)
]
assert len(selection) == len(expected)
```

---

### Q3 — Calculs géométriques : superficie et classement

**Difficulté** : ★★☆  
**Concept** : `.geometry.area`, `.nlargest()`

**Énoncé**

Le GeoDataFrame `cantons` est chargé depuis `tp1.gpkg` (couche `Cantons`,
CRS EPSG:21781 — coordonnées en mètres).

1. Ajoute une colonne `superficie_km2` égale à la superficie de chaque canton
   exprimée en **km²** (1 km² = 1 000 000 m²).
2. Stocke dans la variable `top5` les 5 cantons ayant la plus grande superficie,
   en ordre décroissant.

**Code de départ**

```python
import geopandas as gpd
cantons = gpd.read_file('tp1.gpkg', layer='Cantons')

# Étape 1 — ajoute la colonne superficie_km2 :
cantons['superficie_km2'] = ___

# Étape 2 — crée top5 :
top5 = ___
```

**Réponse attendue**

```python
import geopandas as gpd
cantons = gpd.read_file('tp1.gpkg', layer='Cantons')

cantons['superficie_km2'] = cantons.geometry.area / 1e6
top5 = cantons.nlargest(5, 'superficie_km2')
```

**Cas de test**

```python
# Test 1 — colonne présente
assert 'superficie_km2' in cantons.columns

# Test 2 — valeurs raisonnables (Graubünden ~7 000 km², le plus grand)
assert cantons['superficie_km2'].max() > 5_000, \
    "La superficie maximale semble trop faible"
assert cantons['superficie_km2'].min() > 10, \
    "Certaines superficies semblent trop petites"

# Test 3 — top5 contient exactement 5 lignes
assert len(top5) == 5

# Test 4 — top5 trié correctement
vals = top5['superficie_km2'].tolist()
assert vals == sorted(vals, reverse=True), "top5 n'est pas en ordre décroissant"
```

---

### Q4 — Requête spatiale : prédicat `within`

**Difficulté** : ★★☆  
**Concept** : `.geometry.within()`, filtrage spatial

**Énoncé**

Tu disposes des GeoDataFrames `cantons` et `towns` chargés depuis `tp1.gpkg`.

1. Extrais le **polygone géométrique** du canton de `'Bern'`
   (colonne `NAME`) dans une variable `bern_poly`.
2. Crée `villes_bern`, un GeoDataFrame contenant uniquement les villes
   dont le point est **contenu dans** (`within`) le polygone de Berne.

**Code de départ**

```python
import geopandas as gpd
cantons = gpd.read_file('tp1.gpkg', layer='Cantons')
towns   = gpd.read_file('tp1.gpkg', layer='Towns')

# Étape 1 :
bern_poly = ___

# Étape 2 :
villes_bern = ___
```

**Réponse attendue**

```python
import geopandas as gpd
cantons = gpd.read_file('tp1.gpkg', layer='Cantons')
towns   = gpd.read_file('tp1.gpkg', layer='Towns')

bern_poly   = cantons[cantons['NAME'] == 'Bern'].geometry.values[0]
villes_bern = towns[towns.geometry.within(bern_poly)]
```

**Cas de test**

```python
from shapely.geometry import Point

# Test 1 — bern_poly est un objet géométrique Shapely
assert hasattr(bern_poly, 'contains'), "bern_poly doit être une géométrie Shapely"

# Test 2 — toutes les villes résultantes sont bien dans Berne
assert villes_bern.geometry.within(bern_poly).all(), \
    "Certaines villes ne sont pas dans le canton de Berne"

# Test 3 — Berne (la ville) est dans le résultat
assert 'Bern' in villes_bern['ID1'].values, \
    "La ville de Berne devrait être dans le résultat"
```

---

### Q5 — Jointure attributaire avec `merge()`

**Difficulté** : ★★☆  
**Concept** : `DataFrame.merge()`, LEFT JOIN

**Énoncé**

Tu disposes du GeoDataFrame `cantons` (colonnes : `NAME`, `geometry`)
et d'un DataFrame `pop_data` avec les colonnes `canton` et `population_cantonale`.

Crée `cantons_enrichis` en effectuant une **jointure attributaire** qui ajoute
la colonne `population_cantonale` à chaque canton.
Utilise une jointure `left` (tous les cantons sont conservés).

**Code de départ**

```python
import geopandas as gpd
import pandas as pd

cantons = gpd.read_file('tp1.gpkg', layer='Cantons')

pop_data = pd.DataFrame({
    'canton': ['Zürich', 'Bern', 'Vaud', 'Genf', 'St. Gallen'],
    'population_cantonale': [1_553_423, 1_051_437, 814_762, 504_128, 511_921]
})

# Complète :
cantons_enrichis = ___
```

**Réponse attendue**

```python
import geopandas as gpd
import pandas as pd

cantons = gpd.read_file('tp1.gpkg', layer='Cantons')

pop_data = pd.DataFrame({
    'canton': ['Zürich', 'Bern', 'Vaud', 'Genf', 'St. Gallen'],
    'population_cantonale': [1_553_423, 1_051_437, 814_762, 504_128, 511_921]
})

cantons_enrichis = cantons.merge(
    pop_data,
    left_on='NAME',
    right_on='canton',
    how='left'
)
```

**Cas de test**

```python
# Test 1 — la colonne a bien été ajoutée
assert 'population_cantonale' in cantons_enrichis.columns

# Test 2 — tous les cantons d'origine sont conservés (LEFT JOIN)
assert len(cantons_enrichis) == len(cantons)

# Test 3 — Zürich a la bonne valeur
zurich_pop = cantons_enrichis.loc[
    cantons_enrichis['NAME'] == 'Zürich', 'population_cantonale'
].values[0]
assert zurich_pop == 1_553_423, f"Population de Zürich incorrecte : {zurich_pop}"

# Test 4 — cantons non présents dans pop_data ont NaN
import numpy as np
n_nan = cantons_enrichis['population_cantonale'].isna().sum()
assert n_nan == len(cantons) - len(pop_data), \
    "Les valeurs manquantes ne correspondent pas au nombre de cantons absents"
```

---

### Q6 — Jointure spatiale avec `gpd.sjoin()`

**Difficulté** : ★★★  
**Concept** : `gpd.sjoin()`, `predicate='within'`, agrégation

**Énoncé**

Tu disposes de `cantons` et `towns` chargés depuis `tp1.gpkg`.

1. Effectue une **jointure spatiale** pour associer à chaque ville
   le nom du canton dans lequel elle se trouve (prédicat : `within`).
   Utilise une jointure `left`. Stocke le résultat dans `towns_avec_canton`.
2. À partir de `towns_avec_canton`, crée `nb_villes_par_canton` :
   un DataFrame avec les colonnes `NAME` (nom du canton) et
   `nb_villes` (nombre de villes dans ce canton), **trié par `nb_villes` décroissant**.

**Code de départ**

```python
import geopandas as gpd
cantons = gpd.read_file('tp1.gpkg', layer='Cantons')
towns   = gpd.read_file('tp1.gpkg', layer='Towns')

# Étape 1 :
towns_avec_canton = gpd.sjoin(
    ___,
    ___,
    how=___,
    predicate=___
)

# Étape 2 :
nb_villes_par_canton = ___
```

**Réponse attendue**

```python
import geopandas as gpd
cantons = gpd.read_file('tp1.gpkg', layer='Cantons')
towns   = gpd.read_file('tp1.gpkg', layer='Towns')

towns_avec_canton = gpd.sjoin(
    towns,
    cantons[['NAME', 'geometry']],
    how='left',
    predicate='within'
)

nb_villes_par_canton = (
    towns_avec_canton
    .dropna(subset=['NAME'])
    .groupby('NAME')
    .agg(nb_villes=('ID1', 'count'))
    .reset_index()
    .sort_values('nb_villes', ascending=False)
)
```

**Cas de test**

```python
# Test 1 — towns_avec_canton conserve toutes les villes
assert len(towns_avec_canton) >= len(towns)

# Test 2 — colonne NAME présente
assert 'NAME' in towns_avec_canton.columns

# Test 3 — nb_villes_par_canton est trié correctement
vals = nb_villes_par_canton['nb_villes'].tolist()
assert vals == sorted(vals, reverse=True)

# Test 4 — Zürich (le canton) a au moins 1 ville
assert 'Zürich' in nb_villes_par_canton['NAME'].values
```

---

## Partie B — TP3 : Rasterio & MLP (scikit-learn)

---

### Q7 — Lire les métadonnées d'un raster

**Difficulté** : ★☆☆  
**Concept** : `rasterio.open()`, attributs `.meta`, `.crs`, `.res`

**Énoncé**

Le fichier `mnt_vaud_synth.tif` est un GeoTIFF à 1 bande (altitude en mètres,
float32, EPSG:21781, 200 × 200 pixels).

Complète le code pour afficher :
- Le nombre de **lignes** et de **colonnes** du raster
- Le code **EPSG** du CRS
- La **résolution** (taille d'un pixel) en mètres

Stocke ces valeurs dans les variables `n_lignes`, `n_cols`, `epsg`, `res_x`, `res_y`.

**Code de départ**

```python
import rasterio

with rasterio.open('mnt_vaud_synth.tif') as src:
    n_lignes = ___
    n_cols   = ___
    epsg     = ___
    res_x    = ___   # résolution en x (largeur d'un pixel en mètres)
    res_y    = ___   # résolution en y (hauteur d'un pixel en mètres)
```

**Réponse attendue**

```python
import rasterio

with rasterio.open('mnt_vaud_synth.tif') as src:
    n_lignes = src.height
    n_cols   = src.width
    epsg     = src.crs.to_epsg()
    res_x    = src.res[0]
    res_y    = src.res[1]
```

**Cas de test**

```python
assert n_lignes == 200
assert n_cols   == 200
assert epsg     == 21781
assert abs(res_x - 500.0) < 1.0,  f"res_x attendu ≈ 500 m, obtenu {res_x}"
assert abs(res_y - 300.0) < 1.0,  f"res_y attendu ≈ 300 m, obtenu {res_y}"
```

---

### Q8 — Calcul du NDVI

**Difficulté** : ★★☆  
**Concept** : arithmétique sur bandes raster, gestion de la division par zéro

**Énoncé**

Le fichier `multispectral_synth.tif` est un GeoTIFF à **4 bandes** :
bande 1 = Bleu, bande 2 = Vert, bande 3 = Rouge, bande 4 = NIR.

Calcule le **NDVI** selon la formule :

$$\text{NDVI} = \frac{\text{NIR} - \text{Red}}{\text{NIR} + \text{Red}}$$

Règles :
- Lis les bandes 3 (Rouge) et 4 (NIR) et convertis-les en `float32`.
- Lorsque `NIR + Red == 0`, le résultat doit être `np.nan` (évite la division par zéro).
- Stocke le résultat dans la variable `ndvi` (tableau NumPy 2D).

**Code de départ**

```python
import numpy as np
import rasterio

with rasterio.open('multispectral_synth.tif') as src:
    rouge = src.read(___).astype(np.float32)
    nir   = src.read(___).astype(np.float32)

# Calcule ndvi (protège contre la division par zéro) :
ndvi = ___
```

**Réponse attendue**

```python
import numpy as np
import rasterio

with rasterio.open('multispectral_synth.tif') as src:
    rouge = src.read(3).astype(np.float32)
    nir   = src.read(4).astype(np.float32)

with np.errstate(divide='ignore', invalid='ignore'):
    ndvi = np.where(
        (nir + rouge) == 0,
        np.nan,
        (nir - rouge) / (nir + rouge)
    )
```

**Cas de test**

```python
# Test 1 — shape correcte
assert ndvi.shape == (200, 200), f"Shape attendue (200, 200), obtenu {ndvi.shape}"

# Test 2 — valeurs dans l'intervalle [-1, 1] (hors NaN)
valid = ndvi[~np.isnan(ndvi)]
assert valid.min() >= -1.0 and valid.max() <= 1.0, \
    "Des valeurs NDVI sont hors de l'intervalle [-1, 1]"

# Test 3 — pas de division par zéro (pas d'inf)
assert not np.any(np.isinf(ndvi)), "Des valeurs infinies présentes dans ndvi"
```

---

### Q9 — Préparer les données raster pour scikit-learn

**Difficulté** : ★★☆  
**Concept** : `reshape`, transposition, construction de la matrice de features

**Énoncé**

Tu as un tableau NumPy `bandes` de shape `(4, 200, 200)` représentant
une image multispectrale (4 bandes, 200 × 200 pixels).

Transforme ce tableau en une matrice `X` de shape `(40000, 4)`,
où chaque ligne correspond à un pixel et chaque colonne à une bande spectrale.
(C'est le format attendu par scikit-learn.)

**Code de départ**

```python
import numpy as np
# bandes est disponible — shape : (4, 200, 200)

# Complète :
X = ___

print(X.shape)   # doit afficher (40000, 4)
```

**Réponse attendue**

```python
import numpy as np

n_bandes  = bandes.shape[0]
n_pixels  = bandes.shape[1] * bandes.shape[2]
X = bandes.reshape(n_bandes, n_pixels).T
```

**Cas de test**

```python
assert X.shape == (40_000, 4), f"Shape attendue (40000, 4), obtenu {X.shape}"

# Chaque colonne correspond à une bande
assert np.allclose(X[:, 0], bandes[0].ravel()), \
    "La première colonne doit correspondre à la bande 0"
assert np.allclose(X[:, 3], bandes[3].ravel()), \
    "La quatrième colonne doit correspondre à la bande 3"
```

---

### Q10 — Normalisation avec `StandardScaler`

**Difficulté** : ★★☆  
**Concept** : `StandardScaler`, règle fit/transform

**Énoncé**

On te donne `X_train` et `X_test` (deux tableaux NumPy de features).

Normalise les données avec un `StandardScaler` en respectant la règle
**fit uniquement sur les données d'entraînement** :

1. Crée un `StandardScaler`, ajuste-le (`fit`) sur `X_train`, et transforme `X_train` → `X_train_sc`.
2. Transforme `X_test` avec le **même** scaler (sans ré-ajuster) → `X_test_sc`.

**Code de départ**

```python
from sklearn.preprocessing import StandardScaler

# X_train et X_test sont disponibles

scaler = ___
X_train_sc = ___
X_test_sc  = ___
```

**Réponse attendue**

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)
```

**Cas de test**

```python
import numpy as np

# Test 1 — moyennes ≈ 0 sur l'entraînement
assert np.allclose(X_train_sc.mean(axis=0), 0, atol=1e-6), \
    "Les moyennes de X_train_sc devraient être ≈ 0"

# Test 2 — écarts-types ≈ 1 sur l'entraînement
assert np.allclose(X_train_sc.std(axis=0), 1, atol=1e-4), \
    "Les écarts-types de X_train_sc devraient être ≈ 1"

# Test 3 — X_test_sc utilise les paramètres de X_train (pas recentré sur X_test)
from sklearn.preprocessing import StandardScaler
sc_ref = StandardScaler().fit(X_train)
assert np.allclose(scaler.mean_, sc_ref.mean_), \
    "Le scaler a été ajusté sur les mauvaises données"
```

---

### Q11 — Entraîner un MLPClassifier

**Difficulté** : ★★★  
**Concept** : `MLPClassifier`, paramètres de base, `fit`, `score`

**Énoncé**

Tu as à ta disposition :
- `X_train_sc`, `y_train` — données d'entraînement (normalisées)
- `X_test_sc`,  `y_test`  — données de test (normalisées)

Crée et entraîne un `MLPClassifier` avec les paramètres suivants :
- 2 couches cachées : 64 neurones puis 32 neurones
- Fonction d'activation : `'relu'`
- Graine aléatoire (`random_state`) : `42`

Stocke le modèle dans `clf`, puis calcule la précision sur les données de test
dans la variable `test_acc`.

**Code de départ**

```python
from sklearn.neural_network import MLPClassifier

# Crée et entraîne le modèle :
clf = ___
clf.fit(___, ___)

# Calcule la précision sur le test :
test_acc = ___
print(f"Précision test : {test_acc:.4f}")
```

**Réponse attendue**

```python
from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    activation='relu',
    random_state=42,
)
clf.fit(X_train_sc, y_train)

test_acc = clf.score(X_test_sc, y_test)
print(f"Précision test : {test_acc:.4f}")
```

**Cas de test**

```python
# Test 1 — architecture correcte
assert clf.hidden_layer_sizes == (64, 32), \
    f"hidden_layer_sizes attendu (64, 32), obtenu {clf.hidden_layer_sizes}"

# Test 2 — modèle entraîné
assert hasattr(clf, 'coefs_'), "Le modèle n'a pas été entraîné (appelle .fit())"

# Test 3 — précision raisonnable (> 70 % sur données synthétiques)
assert test_acc > 0.70, \
    f"Précision trop faible : {test_acc:.4f} (attendu > 0.70)"

# Test 4 — test_acc est bien calculé sur les données de TEST (pas d'entraînement)
assert isinstance(test_acc, float)
```

---

### Q12 — Produire une carte de classification

**Difficulté** : ★★★  
**Concept** : `predict` sur l'image entière, `reshape`

**Énoncé**

Tu as à ta disposition :
- `clf` — un `MLPClassifier` déjà entraîné
- `scaler` — un `StandardScaler` déjà ajusté
- `bandes` — tableau NumPy de shape `(4, 200, 200)`

Produis la carte de classification `carte` de shape `(200, 200)` en :
1. Transformant `bandes` en matrice `X_full` de shape `(40000, 4)`.
2. Normalisant `X_full` avec `scaler` (sans ré-ajuster).
3. Prédisant les classes pour chaque pixel avec `clf`.
4. Remettant en forme en `(200, 200)`.

**Code de départ**

```python
import numpy as np

# Étape 1 — aplatir bandes
X_full = ___

# Étape 2 — normaliser
X_full_sc = ___

# Étape 3 — prédire
y_pred_full = ___

# Étape 4 — remettre en forme
carte = ___

print(carte.shape)   # doit afficher (200, 200)
```

**Réponse attendue**

```python
import numpy as np

X_full    = bandes.reshape(bandes.shape[0], -1).T
X_full_sc = scaler.transform(X_full)
y_pred_full = clf.predict(X_full_sc)
carte = y_pred_full.reshape(200, 200)

print(carte.shape)
```

**Cas de test**

```python
# Test 1 — shape correcte
assert carte.shape == (200, 200), f"Shape attendue (200, 200), obtenu {carte.shape}"

# Test 2 — classes valides uniquement (0, 1, 2, 3)
classes_presentes = set(carte.ravel().tolist())
assert classes_presentes.issubset({0, 1, 2, 3}), \
    f"Classes inattendues dans la carte : {classes_presentes - {0,1,2,3}}"

# Test 3 — au moins 3 classes représentées (image variée)
assert len(classes_presentes) >= 3, \
    "Trop peu de classes représentées — vérifier la normalisation"
```

---

## Tableau récapitulatif des questions

| # | TP | Concept clé | Difficulté |
|---|---|---|---|
| Q1 | TP2 | Filtrage booléen simple | ★☆☆ |
| Q2 | TP2 | Filtrage multiple + `.isin()` | ★★☆ |
| Q3 | TP2 | Calcul de superficie + classement | ★★☆ |
| Q4 | TP2 | Requête spatiale `within` | ★★☆ |
| Q5 | TP2 | Jointure attributaire `merge()` | ★★☆ |
| Q6 | TP2 | Jointure spatiale `sjoin()` + agrégation | ★★★ |
| Q7 | TP3 | Métadonnées raster avec rasterio | ★☆☆ |
| Q8 | TP3 | Calcul NDVI sur bandes raster | ★★☆ |
| Q9 | TP3 | Reshape raster → matrice scikit-learn | ★★☆ |
| Q10 | TP3 | Normalisation `StandardScaler` | ★★☆ |
| Q11 | TP3 | Entraîner `MLPClassifier` | ★★★ |
| Q12 | TP3 | Carte de classification complète | ★★★ |
