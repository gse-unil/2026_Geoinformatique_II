# Projet individuel - Etape III : Pré-traitements et modélisation des données

## Objectif
1) Implémente le prétraitement de tes données (sur QGIS ou en Python).

2) Utilise ces données pour ton modèle de régression ou de classification. Enregistre les résultats, puis rédige ton **notebook maître** Python. Cette étape ne comporte pas de rendu intermédiaire ; si nécessaire, elle peut être terminée en semaines 13–14. Le notebook maître est intégré à ton site web et fait partie du rendu final.

## 1. Créer et structurer ton GeoPackage

Structure les couches de données dans **une seule geodatabase (GeoPackage, `.gpkg`)**, avec des couches triées dans différents dossiers. Pour cela, tu peux utiliser l'icone `Add Group` <img src="img/icon_group.png" alt="alt text" width="20">. Les dossiers qui doivent être contenu dans ton projet sont les suivants :
- `source` : données sources intactes avant traitement (p. ex. `communes`) ;
- `temp` : résultats intermédiaires et versions de travail (p. ex. `communes_clip`) ;
- `input` : données utilisées comme entrée de la régression ou de la classification, résultant de la chaîne de pré-traitements (p. ex. `votations`) ;
- `results` : données finales résultant de l'analyse et utilisées pour l'habillage de la carte (p. ex. `temperature`).

Les **rasters** (MNT, orthophotos, etc.) sont conservés comme fichiers GeoTIFF à côté du GeoPackage, et zippés lors de l'empaquetage ([étape IV](etape4.md)).

Pour rappel, il est nécessaire de documenter dans le rapport final chaque donnée source du projet avec :
- le nom de la couche de données ;
- son fournisseur ;
- son type (vecteur, raster ou table) et sa primitive géographique si applicable (points, lignes, polygones) ;
- son lien public de téléchargement (URL) ;
- la date de téléchargement ;
- son système de coordonnées 
- sa résolution ou son échelle (si applicable);
- son rôle dans l'analyse (variable d'entrée, variable à expliquer, variable explicative, habillage de la carte).


## 2. Construire ta chaîne de pré-traitements

La chaîne de pré-traitements passe des données brutes au **tableau d'analyse** : une ligne par observation, une colonne par variable (la variable à expliquer et les variables explicatives). Elle doit inclure au minimum **trois traitements**, couvrant au moins **deux** catégories d'outils (voir l'[étape I](etape1.md)), et être automatisée, au choix :
- dans QGIS, avec le **Modeleur graphique** (fichier `.model3`) ;
- en Python, dans la première partie de ton notebook maître (voir l'[étape III](etape3.md)).

Vérifie bien que :
- chaque traitement fonctionne ;
- les données intermédiaires sont enregistrées dans le GeoPackage (couches `temp`), et le tableau d'analyse dans une couche `input` ;
- la chaîne est logique, justifiée et reproductible.

Une chaîne courte mais justifiée et documentée vaut mieux qu'une chaîne longue et fragile.

## 3. Modélisation

La modélisation doit se faire sur un Notebook Python, et doit contenir les éléments suivants :
- **Analyse exploratoire** : présentation des données brutes à l'aide de cartes, de distributions statistiques et/ou de corrélations entre variables.
- **Modèle** : ajustement d'au moins un modèle de régression ou de classification tel que vu dans les travaux pratiques en Python. Le modèle doit être évalué sur des données non utilisées pour l'entrainement, la validation ou la calibration (échantillon de test) avec des métriques adaptées (R², RMSE, MAE, etc. pour une régression ; exactide, precision, sensibilité, FF1 score etc. pour une classification). 
- **Analyse des résidus** : analyse des résidus du modèle retenu, y compris leur répartition spatiale (carte des résidus).
- **Prédictions et incertitudes** : cartographie des prédictions du modèle et quantification des incertitudes (intervalles de confiance ou de prédiction, avec justification).
- **Export** : enregistrement du tableau d'analyse (dossier `input`) et des résultats (dossiers `results`) dans ton GeoPackage.

## 4. Le notebook maître
Le notebook maître rassemble toute la partie Python de ton projet. Il doit être **documenté** et **exécutable de bout en bout** après « Restart & Run All », sur une autre machine, à partir du `README` et du fichier d'environnement. L'[exemple de projet](../tps/python/project_example_landslides.ipynb) suit la structure ci-dessous :

| Section | Contenu |
|---|---|
| En-tête | question de recherche, hypothèses, variables, tableau des données (source et lien de téléchargement, licence, date de téléchargement, résolution), organisation du GeoPackage, instructions pour reproduire le notebook |
| 1. Configuration | imports, chemins relatifs, graine aléatoire |
| 2. Données sources | chargement des couches `source` |
| 3. Analyse exploratoire | cartes, distributions, corrélations |
| 4. Chaîne de pré-traitements | si elle est réalisée en Python : des données sources au tableau d'analyse ; sinon, chargement de la couche `input` produite avec le Modeleur graphique |
| 5. Modélisation | échantillon de test, ajustement, métriques, choix du modèle |
| 6. Résidus | analyse et carte des résidus |
| 7. Prédictions et incertitudes | carte des prédictions, intervalles de confiance ou de prédiction |
| 8. Export | couches `input` et `results` dans le GeoPackage |
| 9. Conclusion | réponse à la question de recherche, limites |

Dans ton notebook, utilise des librairies telles que geopandas, shapely, rasterio, numpy, pandas, matplotlib, scikit-learn ou statsmodels.

## 5. Reproductibilité
Ton projet tient dans un **dossier unique**, qui contient :
- un `README` : description du projet, sources des données, instructions d'exécution ;
- un fichier d'environnement (`environment.yml` ou `requirements.txt`) qui fige les versions des librairies, par exemple produit avec `conda env export > environment.yml` ou `pip freeze > requirements.txt` ;
- le notebook maître, qui n'utilise que des **chemins relatifs** (p. ex. `'projet.gpkg'` plutôt que `'C:/Users/.../projet.gpkg'`) et fixe la **graine aléatoire** (`random_state=...`, `np.random.default_rng(...)`), pour que les résultats soient identiques à chaque exécution.

Avant de rendre, vérifie que « Restart & Run All » exécute ton notebook sans erreur.
