# Projet individuel - Etape III : Chaîne des géotraitements

## Objectif
Construire une chaine de géotraitement développée en double dans QGIS et en Python permettant de répondre à ta question de recherche. Cette étape ne comporte pas de rendu intermédiaire obligatoire, mais les éléments produits alimentent directement le rendu final.

## Volet QGIS

### 1. Structurer la geodatabase
Utilise une seule geodatabase au format **GeoPackage (.gpkg)** avec des couches préfixées selon leur rôle :
- `src_` : données sources intactes avant traitement (p. ex. src_communes);
- `tmp_` : résultats intermédiaires et versions de travail (p. ex. tmp_communes_clip);
- `hab_` : données finales utilisées pour l'habillage cartographique  (p. ex. hab_communes);
- `ana_` : résultats finaux résultant de l’analyse (p. ex. ana_wui).

Conserve les rasters (MNT, orthophotos, etc.) comme fichiers (GeoTIFF) à côté du GeoPackage et ajoute les lors de l’empaquetage.

### 2. Construire la chaîne de géotraitement
Automatise les géotraitements avec le **Modeleur graphique QGIS** (fichier `.model3`).

La chaîne doit inclure au minimum 5 géotraitements:
1. Outils de préparation, de sélection et de réduction de l’information (clip, sélection spatiale ou par expression,
jointure, reclasser, merge, dissolve, etc.).
2. Outils de combinaison de plusieurs couches (intersect, différence, union, statistiques zonales, extraction de
valeurs vers des points, etc.).
3. Outils d’analyse spatiale, dans la boîte à outils QGIS (algorithmes natifs, SAGA ou GRASS) : interpolation
IDW ou TIN, analyse de surface (pente, exposition, ombrage), calculatrice raster, distance, densité de noyau,
hydrologie, etc.


### 3. Tester les résultats
Vérifie bien que :
- chaque traitement fonctionne ;
- les données intermédiaires sont correctement enregistrées ;
- la chaîne est logique et reproductible ;
- les résultats répondent progressivement à la question de recherche.

## Volet Python

Crée un **notebook maître `.ipynb`** :
- exécutable de bout en bout ;
- documenté ;
- incluant des étapes de chargement, traitement et visualisation similaires à celles du volet QGIS.
- incluant une composante statistique ou de modélisation  (régression, classification — cf. TPs Python 2–4)
- Qui quantifie les incertitudes
- Intégré au site web du projet (portfolio)

Dans ton notebook, utilise des librairies tels que:
- geopandas ;
- shapely ;
- rasterio ;
- numpy ;
- matplotlib.