# Projet individuel - Etape IV

## Objectifs
L'objectif de cette dernière étape est de finaliser ton projet. Cela inclut la rédaction du rapport final, la communication de tes résultats sous forme de cartes et graphiques ainsi que la publication de ton projet complet via le site web.

## 1. Cartes et visualisations
Les cartes produites doivent respecter les exigences de base en cartographie et inclure:
- un titre ;
- une légende ;
- une échelle ;
- une orientation ;
- les sources ;
- l'auteur ;
- la date.

Des graphiques ou statistiques peuvent compléter la carte.

## 2. Structure du rapport final
Le rapport doit faire au maximum **3 pages** (hors figures et schéma de géotraitement) et doit être structuré comme suit:

### 2.1. Contexte et objectifs
- Présenter le contexte.
- Définir les objectifs.
- Rappeler la question de recherche.
- Présenter les hypothèses mises à jour après l'analyse.

### 2.2 Méthodologie

**Géodonnées :**
- décrire brièvement les données d'origine ;
- fournir leur source et leurs liens publics de téléchargement;
- quantifier leurs incertitudes de mesure avec leurs unités.

**Chaine de traitement :**
- expliquer clairement la chaîne de géotraitements pour qu'elle puisse être reproduite ;
- ajouter un schéma de la chaîne de géotraitement en annexe.

### 2.3 Résultats
Les résultats doivent inclure au moins une carte (complétée si besoin de graphiques ou de statistiques) et doivent être interprétés en fonction de tes objectifs et hypothèses. Tes résultats doivent également contenir :

**1) Au moins une régression spatialisée :**
- ajuste un modèle de régression ou de classification ;
- cartographie les prédictions sur ta zone d’étude ;
- si applicable (cf. TP 2), donne ses intervalles de confiance (incertitude sur la relation estimée) et ses intervalles de prédiction (incertitude sur chaque valeur individuelle prédite).

**2) Une quantification des incertitudes :**
- estime quantitativement les incertitudes de mesure, d’estimation et de visualisation, avec les valeurs et unités pertinentes ;
- si tes résultats s’écartent de tes attentes, discute une ou deux phrases des limites des données ou des difficultés techniques rencontrées.


### 2.4. Données et métadonnées
- Fourni un lien vers le projet empaqueté.
- Veuille à respecter les principes FAIR.
- Vérifie que tes couches ont des métadonnées complètes.


## 3. Empaquetage du projet
Suis la méthode d’empaquetage du TP1 et la procédure de partage de l’étape II :
1. Regroupe dans un dossier nom_prenom_projet : le projet .qgz, la geodatabase .gpkg (couches src_, tmp_, hab_, ana_), le modèle .model3, les rasters (GeoTIFF) et le notebook Python maître .ipynb.
2. Vérifie que le projet s’ouvre sans couche manquante (dans QGIS, chemins relatifs : Projet > Propriétés > Général > Enregistrer les chemins : Relatif ).
3. Comprime le dossier en nom_prenom_projet.zip, **qui doit peser moins de 2 Go** : au-delà, sans compromettre la reproductibilité, réduis l’étendue géographique des données partagées pour te concentrer sur la zone d’étude, ré-échantillonne les rasters, ou ne conserve que les couches src_ nécessaires à rejouer la chaîne.
4. Copie le .zip sur OneDrive et place son lien de partage sur la page projet de ton site web.
5. Dépose l’adresse de ton site web sur Moodle : c’est le rendu final.


## 4. Critères d'évaluation du rendu final :

- Le rendu est complet, conforme aux consignes et déposé dans les délais.
- Le projet .qgz s’ouvre sans couche manquante et la géodatabase est complète, avec ses couches préfixées src_ / tmp_ / hab_ / ana_.
- La chaîne de géotraitements (Modeleur graphique) est logique et fonctionnelle.
- Le notebook maître Python est exécutable de bout en bout et documenté.
- Les métadonnées sont complètes.
- Les résultats répondent à la question de recherche.
- Les résultats s’appuient rigoureusement sur un algorithme de régression/classification ou une analyse statistique.
- La carte répond aux exigences de base en cartographie (titre, légende, échelle, orientation, sources, auteur, date).
-  Le rapport présente et illustre correctement méthode et résultats avec un commentaire critique