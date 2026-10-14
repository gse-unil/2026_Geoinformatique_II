# Projet individuel - Etape I : Question et recherche des données

## Objectifs
Cette première étape (semaine 6) vise à obtenir une vision d'ensemble de ton projet. Elle fait l'objet d'un **rendu intermédiaire obligatoire**, à déposer sur [Moodle]({{ MOODLE_RENDU_ETAPE1 }}) au plus tard à la fin de la semaine intercalaire (semaine 8). Ce rendu contient ta question et tes hypothèses de recherche, la variable à expliquer et les variables explicatives, le schéma de ta chaîne de pré-traitements, le modèle que tu souhaites utiliser et la liste des données dont tu auras besoin.

### 1. Définition de la question et des hypothèses de recherche

- Définis une zone d'études (par exemple la Suisse, le Canton du Valais, la commune de Crissier, l'Europe, les rives du Lac de Neuchâtel ...)
- Formule une question de recherche **claire, détaillée et concrète**, à laquelle un modèle de régression ou une classification peut apporter un élément de réponse. Nous encourageons l’inventivité dans le choix de la question de recherche !
- Définis le contexte et justifie l'intérêt de ta question de recherche.
- Présente des hypothèses de recherche adaptées à ta question de recherche.

### 2. Identification et téléchargement des données sources
Une fois la question de recherche établie, l’étape suivante consiste à identifier les données sources nécessaires à ton analyse.

Pour commencer, recense les types d’objets géographiques pertinents pour ton projet (arrêts de bus, communes, sentiers pédestres, écoles, etc.) ainsi que leur primitive géographique (point, ligne ou polygone).

Ensuite, recherche les jeux de données à partir desquels tu pourras télécharger ces informations. Pour ce projet, l’utilisation **d'un ou de plusieurs jeux de données ouverts** est requise, dont **au moins un de nature géospatiale**.

Tu peux alors lister les jeux de données nécessaires avec, pour chacun :
- de quelles données tu as besoin (souvent une partie du jeu de données) ;
- le nom de la couche de données ;
- son fournisseur ;
- son type (vecteur, raster ou table) ;
- son lien public de téléchargement (URL) ;
- la date de téléchargement ;
- son système de coordonnées 
- sa résolution ou son échelle ;
- son rôle dans l'analyse (variable d'entrée, variable à expliquer, variable explicative, habillage de la carte).

Quelques exemples :
- Surfaces de forêt, swissTLM3D, swisstopo, vecteur, https://www.swisstopo.admin.ch/de/geodata/landscape/tlm3d.html, 13.11.2026, MN 95, 1-3m, variable d'entrée.
- Arbres individuels, Arbres, commune de Lausanne, vecteur, https://viageo.ch/catalogue/donnee/300196, 13.11.2026, MN95, / (saisie manuelle), variable explicative.
- Altitude, swissALTI3D, swisstopo, raster, https://www.swisstopo.admin.ch/de/geodata/height/alti3d.html, 13.11.2026, MN95, 2m, habillage de la carte.

N'hésite pas à t'inspirer des sources de géodonnées listées ci-dessous : 
- [Office fédéral de topographie (Swisstopo)](https://www.swisstopo.admin.ch/fr/home.html)
- [Géoportail Suisse](https://map.geo.admin.ch/)
- Office fédéral de la statistique:
    - [Atlas statistique de la Suisse](https://www.atlas.bfs.admin.ch/maps/13/de/15805_8582_8581_8580/24724.html)
    - [Données Géostat](http://www.geostat.admin.ch)
    - [Données ThemaKart](https://www.bfs.admin.ch/bfs/fr/home/services/cartes/services-themakart.html)
    - [Tableaux interactifs Stat-Tab](https://www.pxweb.bfs.admin.ch/pxweb/de/)
- [Données ouvertes de l’administration publique suisse](https://opendata.swiss/fr)
- [Portail de référence en Suisse Romande](https://viageo.ch/)
- [Open Street Map](https://www.openstreetmap.org), téléchargement depuis [GeoFabrik](https://download.geofabrik.de)
- [CORINE](https://land.copernicus.eu/pan-european/corine-land-cover) et [CORINE Switzerland](https://www.wsl.ch/fr/projets/corine-schweiz/)
- [Catalogue géographique de la Suisse](https://www.swisstopo.admin.ch/fr/geocat-ch-catalogue-suisse-de-geometadonnees)
- [Natural Earth Data](https://www.naturalearthdata.com/)
- [Free GIS Data](https://freegisdata.rtwilson.com/)
- [Géodonnées de l'UNIL](https://unil-sgc.github.io/geodata/)


### 3. Réalisation du schéma de la chaîne de pré-traitements 

Pour transformer les données brutes en **tableau d'analyse** prêt pour la modélisation (une ligne par observation, une colonne par variable), tu vas utiliser différents pré-traitements. Ceux-ci peuvent être réalisés dans QGIS ou en Python, et sont résumés dans une chaine de pré-traitements. La chaine de prétraitement présentée pour ce projet doit inclure au minimum **trois traitements**, couvrant au moins **deux** des catégories suivantes :
1. Outils de préparation, de sélection et de réduction de l'information (clip, sélection spatiale, jointure, reclassifier, merge, dissolve, buffer, etc.).
2. Outils de superposition de plusieurs couches (intersect, erase, statistiques zonales, etc.).
3. Outils d'analyse spatiale (distance, interpolation, surface, hydrologie, densité, analyse de réseau, etc.).

L’ensemble des pré-traitements, ainsi que les données d'entrée (données brutes) et de sortie (données pré-traitées, prêtes à être utilisées par le modèle), doivent être représentés dans un schéma de chaîne de pré-traitements, en respectant la convention graphique suivante :
- Ovale bleu = données sources en entrée
- Ovales verts = données transformées en sortie (intermédiaires ou finales)
- Rectangles jaunes = opérations de géotraitement 

### 3. Modèle de regression ou de classification

La dernière étape de ce projet consiste à appliquer un modèle de régression ou de classification. Ce modèle utilise deux types de variables :
- **Variable(s) à expliquer** (« sortie ») : La ou les variable(s) que le modèle cherche à prédire.
- **Variable(s) explicative(s)** (« entrée ») : La ou les variable(s) utilisée(s) pour effecter ces prédictions.

Assure-toi de justifier le choix du modèle retenu en fonction de ta question de recherche et d’indiquer clairement quelles sont les variables explicatives et la variable à expliquer.

## Critères d'évaluation du rendu intermédiaire
- Le rendu est complet et déposé dans les délais ;
- La question de recherche et les hypothèses associées sont claires, détaillées et ancrées dans un contexte concret ;
- La zone d’étude est clairement délimitée et cohérente avec la question de recherche ;
- Les données sources comprennent un ou plusieurs jeux de données ouverts, dont au moins un géospatial, et sont cohérentes avec la question de recherche et la chaîne de pré-traitements ;
- Toutes les informations requises sont renseignées pour chaque jeu de données ;
- Le schéma de la chaîne de pré-traitements est clair et inclut au moins 3 traitements couvrant au moins 2 des catégories listées dans les exigences du projet ;
- La chaîne de pré-traitements et les modèles envisagés sont adaptés pour répondre à la question de recherche ;
- Les variables à expliquer et explicatives sont clairement identifiées.