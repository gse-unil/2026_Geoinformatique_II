# Projet individuel - Etape I : Question et recherche des données

## Objectifs
Cette première étape (semaine 6) vise à obtenir une vision d'ensemble de ton projet. Elle fait l'objet d'un **rendu intermédiaire obligatoire**, à déposer sur [Moodle]({{ MOODLE_URL }}) au plus tard à la fin de la semaine intercalaire (semaine 8). Ce rendu contient ta question et tes hypothèses de recherche, la variable à expliquer et les variables explicatives, le schéma de ta chaîne de pré-traitements, les modèles que tu comptes comparer et la liste des données dont tu auras besoin.

### 1. Question et hypothèses de recherche
- Définis le contexte et les objectifs du projet.
- Formule une question de recherche **claire, détaillée et concrète**, à laquelle une régression peut apporter un élément de réponse.
- Présente des hypothèses de recherche adaptées à ta question de recherche.

### 2. Variables
- La **variable à expliquer** (« sortie ») : le phénomène que ton modèle doit prédire.
- Les **variables explicatives** (« entrées ») : les variables à partir desquelles tu comptes le prédire.

### 3. Schéma de la chaîne de pré-traitements et modèles envisagés

Le schéma montre comment tu passes des données brutes à un **tableau d'analyse** prêt pour la modélisation (une ligne par observation, une colonne par variable). Les pré-traitements peuvent être réalisés dans QGIS ou en Python. La chaîne doit inclure au minimum **trois traitements**, couvrant au moins **deux** des catégories suivantes :
1. Outils de préparation, de sélection et de réduction de l'information (clip, sélection spatiale, jointure, reclassifier, merge, dissolve, buffer, etc.).
2. Outils de superposition de plusieurs couches (intersect, erase, statistiques zonales, etc.).
3. Outils d'analyse spatiale (distance, interpolation, surface, hydrologie, densité, analyse de réseau, etc.).

Indique aussi les modèles de régression ou de classification que tu comptes comparer (cf. TP Python).

### 4. Identification des données
Le projet utilise **un ou plusieurs jeux de données ouverts**, dont au moins un géospatial. Liste les jeux de données nécessaires avec, pour chacun :
- son nom et son type (vecteur, raster ou table) ;
- sa source et son lien public de téléchargement (URL) ;
- sa licence ;
- sa date de téléchargement ;
- son système de coordonnées et sa résolution ou son échelle ;
- son rôle dans l'analyse (variable à expliquer, variable explicative, habillage de la carte).

N'hésite pas à t'inspirer des sources de géodonnées listées dans le syllabus du cours.

## Critères d'évaluation du rendu intermédiaire
- Le rendu est complet et déposé dans les délais.
- La question de recherche est claire, détaillée et concrète ; les variables à expliquer et explicatives sont identifiées.
- Le schéma de la chaîne de pré-traitements et les modèles envisagés sont adéquats.
- La liste des données sources est fournie et cohérente avec la chaîne de pré-traitements.
- Le rendu est complet et déposé dans les délais.
- La question de recherche est claire, détaillée et concrète ; les variables explicatives et à expliquer sont identifiées.
- La zone d'étude est bien définie et est cohérente avec la question de recherche.
- La liste de données sources contient un ou plusieurs jeux de données ouverts, dont au moins un géospatial, et est cohérente avec la question de recherche et la chaîne de pré-traitements.
- Pour chaque jeu de données, la source (URL), la licence, la date de téléchargement, le système de coordonnées et la résolution / l'échelle sont documentés.
- Le schéma de la chaîne de pré-traitements inclus au moins 3 traitements couvrant au moins 2 des catégories listées dans les exigences du projet.
- La chaîne de pré-traitements et les modèles envisagés sont adaptés pour répondre à la question de recherche.