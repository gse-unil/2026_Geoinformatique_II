## Objectifs pédagogique du cours SIG

TP1: # ArcGIS Pro & les machines virtuelles

1. Utiliser les machines virtuelles de l’UNIL
2. Télécharger les données du TP depuis OneDrive
3. Se familiariser avec le logiciel ArcGIS Pro
4. Visualiser des couches géographiques
5. Sauvegarder un projet ArcGIS Pro sur SWITCHdrive
6. Éditer l’apparence d’une couche
7. Ouvrir et éditer des tables attributaires

TP2: # Fondamentaux de l’information géographique

1. Comprendre les principes du géoréférencement et des informations géographiques
2. Comprendre les différences et les caractéristiques propres aux systèmes de coordonnées géographiques et projetées
3. Savoir ce qu’est le DATUM (système géodésique) et savoir le manipuler
4. Connaître les propriétés des différentes projections
5. Utiliser les indicateurs de Tissot pour différencier et comprendre les projections
6. Mesurer des distances

TP3: # Géodatabase et requêtes attributaires

1. Chercher et télécharger des géodonnées
2. Créer une Géodatabase où stocker et organiser les géodonnées
3. Éditer les géodonnées et faire des requêtes attributaires

TP4: # Sélection, jointures et relations

TP5: # Les outils de géotraitement
L’objectif de ce TP est de te montrer comment réaliser des analyses spatiales dans les SIG à partir de géodonnées. Tu apprendras à utiliser les principaux outils de géotraitement pour les opérations SIG de base. Une fois que tu auras expérimenté ces outils, tu seras également capable de les utiliser dans ton propre projet si nécessaire !

Dans les TP précédents, tu as appris à utiliser les outils de gestion des tables attributaires (_Select by attribute_, _Select by location_). Dans ce TP, nous allons apprendre comment utiliser :

- _les outils de sélection et d’extraction,_
- _les outils de proximité,_
- _les outils de superposition,_
avec des données vectorielles.

TP6: # Créer ta première carte thématique
Dans cette partie du TP, tu créeras une carte thématique de type choroplèthe (en aplats de couleurs) qui représente les résultats d’une initiative populaire. Après, on y ajoutera une représentation de la densité habitée, de façon à pouvoir en extraire une spatialité (ou information spatiale).

TP7: # Opérations Raster
Au cours de ce TP, tu vas te familiariser avec certains outils de géotraitement pour les données au format raster (=image). Tu travailleras avec des données satellites au format raster (provenant de la [NASA](https://www.nasa.gov/)), une couche thématique raster qui identifie les classes d’occupations du sol (créée par nos soins avec les données satellites de la NASA) et enfin un MNT (modèle numérique de terrain) que tu extrapoleras (grâce à la méthode de l’IDW “Inverse Distance Weighting”) à partir de données ponctuelles disponibles sur Swisstopo.

TP8: # Analyses de distance
Cet avant-dernier TP du semestre te permet d’expérimenter deux outils basés sur l’analyse de distance : le lissage spatial (appelé ‘densité de noyau’ dans ArcGIS) et les aires de chalandise (ou aires d’influence).

En dehors du paramétrage des outils (y compris variables d’environnement), cet exercice te permettra de mener une chaîne complète de géo-traitements, en reliant les données issues des deux analyses en une seule couche, avec l’outil de statistiques de zone.

TP9: # ModelBuilder
L’objectif de ce TP est de se familiariser avec la fonctionnalité “[ModelBuilder](https://pro.arcgis.com/fr/pro-app/latest/help/analysis/geoprocessing/modelbuilder/modelbuilder-quick-tour.htm)” d’ArcGIS. Ce langage de modélisation visuel permet de créer, modifier et gérer des modèles d’analyse spatiale. Ces modèles peuvent regrouper les chaînes d’opérations de géotraitement.

Puisque ModelBuilder est très utile pour la création, l’exécution et le partage de modèles personnalisés ArcGIS, nous te le recommandons tout particulièrement pour le projet individuel que tu devras faire dans le cadre de ce cours ! Disposer d’un modèle regroupant les opérations de géotraitement facilite également l’identification et la correction d’éventuelles erreurs.
