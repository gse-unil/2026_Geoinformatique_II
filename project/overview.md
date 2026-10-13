# Projet individuel

Le projet personnel de Géoinformatique II a pour objectif de répondre à une question de recherche spécifique à l'aide de géodonnées, à travers les procédés suivants : **préparer des données spatiales, construire des variables explicatives et modéliser un phénomène par régression**, puis communiquer les résultats. Le projet *individuel* est réalisé en **4 étapes** au cours du semestre, avec **2 rendus** (étape I et rendu final), qui comptent pour 50 % de la note finale. Le calendrier et les modalités d'évaluation se trouvent aussi sur **[Moodle]({{ MOODLE_URL }})**.

Les pré-traitements peuvent être réalisés dans **QGIS** ou en **Python**. La modélisation est réalisée en Python dans un **notebook maître**. L'[exemple de projet](../tps/python/project_example_landslides.ipynb) (`project_example_landslides.ipynb`) illustre l'enchaînement attendu : chargement des données, analyse statistique, modélisation avec quantification de l'erreur, export des résultats.

L'accent est mis sur la pertinence de la démarche et la **reproductibilité** plutôt que sur le nombre d'opérations : une chaîne courte mais justifiée et documentée vaut mieux qu'une chaîne longue et fragile.

## Objectifs et exigences

- Choisir et formuler une question de recherche à laquelle une régression peut apporter un élément de réponse, en identifiant la **variable à expliquer** et les **variables explicatives** envisagées.
- Utiliser **un ou plusieurs jeux de données ouverts**, dont au moins un géospatial, et documenter pour chacun la source (URL), la licence, la date de téléchargement, le système de coordonnées et la résolution / l'échelle.
- Construire une chaîne de pré-traitements logique et justifiée (dans QGIS et/ou en Python) pour passer des données brutes à un **tableau d'analyse** prêt pour la modélisation (une ligne par observation, une colonne par variable). Cette chaîne doit inclure au minimum **trois traitements**, couvrant au moins **deux** des catégories suivantes :
  1. outils de préparation, de sélection et de réduction de l'information (clip, sélection spatiale, jointure, reclassifier, merge, dissolve, buffer, etc.) ;
  2. outils de superposition de plusieurs couches (intersect, erase, statistiques zonales, etc.) ;
  3. outils d'analyse spatiale (distance, interpolation, surface, hydrologie, densité, analyse de réseau, etc.).

  L'automatisation se fait au choix dans QGIS avec le **Modeleur graphique** (fichier `.model3`) ou en Python, dans la première partie du notebook maître.
- Structurer les couches de données dans **une seule geodatabase (GeoPackage)**, avec des couches préfixées selon leur rôle : `source_`, `temp_`, `input_` et `results_` (voir l'[étape II](etape2.md)). Les **rasters** (MNT, orthophotos, etc.) sont conservés comme fichiers GeoTIFF à côté du GeoPackage et **zippés** lors de l'empaquetage.
- Présenter une **analyse exploratoire** des données brutes (à l'aide de cartes, de distributions statistiques et/ou de corrélations entre variables).
- Ajuster **un modèle de régression ou de classification** tel que vu dans les travaux pratiques en Python, évalué sur des données non utilisées pour l'ajustement (échantillon de test) avec des métriques adaptées (R², RMSE, MAE, etc.), et justifier le choix du modèle utilisé.
- Analyser les **résidus** du modèle retenu, y compris leur répartition spatiale (carte des résidus).
- **Cartographier les prédictions** du modèle et quantifier les incertitudes (intervalles de confiance ou de prédiction avec justification, cf. TP Python et introduction à la régression). Produire une carte qui respecte les exigences cartographiques minimales.
- Assurer la **reproductibilité** du projet : dossier unique avec un `README` (description, sources, instructions d'exécution), fichier d'environnement (`environment.yml` ou `requirements.txt`) figeant les versions des librairies, chemins relatifs, graine aléatoire fixée, et notebook maître exécutable de bout en bout après « Restart & Run All ».
- Rédiger un court rapport d'accompagnement incluant le contexte, les objectifs, la méthodologie, les résultats obtenus et leur commentaire critique.

## Déroulement du projet

| Étape | Quand ? | Contenu | Rendu |
|-------|---------|---------|-------|
| [I : question et données](etape1.md) | semaine 6 | question et hypothèses, variables, schéma de la chaîne de pré-traitements, modèles envisagés, liste des données | **obligatoire** |
| [II : site web, GeoPackage et chaîne de pré-traitements](etape2.md) | semaine 7 | site web (portfolio & projet), GeoPackage structuré, chaîne de pré-traitements | — |
| [III : modélisation et notebook maître](etape3.md) | semaine 9 (à terminer en semaines 13–14 si nécessaire) | modèle de régression ou de classification, notebook maître Python | — |
| [IV : cartes, rapport et rendu final](etape4.md) | semaines 13–14 | cartes et graphiques, empaquetage, rapport final | **rendu final** |

## Rendus

| Rendu | Quand ? | Où ? |
|-------|---------|------|
| Étape I : question, variables, schéma de la chaîne, modèles envisagés, liste des données (10 %) | au plus tard à la fin de la semaine intercalaire (semaine 8) | [Moodle]({{ MOODLE_URL }}) |
| Rendu final : adresse de ton site web, qui présente le rapport, le notebook maître et le lien vers le projet empaqueté (40 %) | avant la fin du semestre | [Moodle]({{ MOODLE_URL }}) |

## Exemple de projet

Pour te faire une idée concrète du résultat attendu, consulte l'[exemple de projet : **glissements de terrain dans le canton de Vaud**](../tps/python/project_example_landslides.ipynb). C'est un exemple de notebook maître : il suit, section par section, la structure attendue (voir l'[étape III](etape3.md)). Il est fourni à titre d'illustration : le sujet, les données et les méthodes de ton propre projet restent libres.

% - [Exemple de projet : **?**](../python/?.ipynb)
