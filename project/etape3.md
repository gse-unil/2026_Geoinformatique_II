# Projet individuel - Etape III : Modélisation et notebook maître

## Objectif
Implémente ton modèle de régression ou de classification, teste-le et enregistre les résultats, puis rédige ton **notebook maître** Python (semaine 9). Cette étape ne comporte pas de rendu intermédiaire ; si nécessaire, elle peut être terminée en semaines 13–14. Le notebook maître est intégré à ton site web et fait partie du rendu final.

## 1. Modélisation
- **Analyse exploratoire** : présente les données brutes à l'aide de cartes, de distributions statistiques et/ou de corrélations entre variables.
- **Modèle** : ajuste au moins un modèle de régression ou de classification tel que vu dans les travaux pratiques en Python, et évalue-le sur des données non utilisées pour l'ajustement (échantillon de test) avec des métriques adaptées (R², RMSE, MAE, etc. ; exactitude ou AUC pour une classification). Compare les modèles envisagés à l'étape I et justifie le choix du modèle retenu.
- **Résidus** : analyse les résidus du modèle retenu, y compris leur répartition spatiale (carte des résidus).
- **Prédictions et incertitudes** : cartographie les prédictions du modèle et quantifie les incertitudes (intervalles de confiance ou de prédiction, avec justification ; cf. TP Python et introduction à la régression).
- **Export** : enregistre le tableau d'analyse (couche `input_`) et les résultats (couches `results_`) dans ton GeoPackage.

## 2. Le notebook maître
Le notebook maître rassemble toute la partie Python de ton projet. Il doit être **documenté** et **exécutable de bout en bout** après « Restart & Run All », sur une autre machine, à partir du `README` et du fichier d'environnement. L'[exemple de projet](../tps/python/project_example_landslides.ipynb) suit la structure ci-dessous :

| Section | Contenu |
|---|---|
| En-tête | question de recherche, hypothèses, variables, tableau des données (source et lien de téléchargement, licence, date de téléchargement, résolution), organisation du GeoPackage, instructions pour reproduire le notebook |
| 1. Configuration | imports, chemins relatifs, graine aléatoire |
| 2. Données sources | chargement des couches `source_` |
| 3. Analyse exploratoire | cartes, distributions, corrélations |
| 4. Chaîne de pré-traitements | si elle est réalisée en Python : des données sources au tableau d'analyse ; sinon, chargement de la couche `input_` produite avec le Modeleur graphique |
| 5. Modélisation | échantillon de test, ajustement, métriques, choix du modèle |
| 6. Résidus | analyse et carte des résidus |
| 7. Prédictions et incertitudes | carte des prédictions, intervalles de confiance ou de prédiction |
| 8. Export | couches `input_` et `results_` dans le GeoPackage |
| 9. Conclusion | réponse à la question de recherche, limites |

Dans ton notebook, utilise des librairies telles que geopandas, shapely, rasterio, numpy, pandas, matplotlib, scikit-learn ou statsmodels.

## 3. Reproductibilité
Ton projet tient dans un **dossier unique**, qui contient :
- un `README` : description du projet, sources des données, instructions d'exécution ;
- un fichier d'environnement (`environment.yml` ou `requirements.txt`) qui fige les versions des librairies, par exemple produit avec `conda env export > environment.yml` ou `pip freeze > requirements.txt` ;
- le notebook maître, qui n'utilise que des **chemins relatifs** (p. ex. `'projet.gpkg'` plutôt que `'C:/Users/.../projet.gpkg'`) et fixe la **graine aléatoire** (`random_state=...`, `np.random.default_rng(...)`), pour que les résultats soient identiques à chaque exécution.

Avant de rendre, vérifie que « Restart & Run All » exécute ton notebook sans erreur.
