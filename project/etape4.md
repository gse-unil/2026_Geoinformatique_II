# Projet individuel - Etape IV : Cartes, rapport et rendu final

## Objectifs
Cette dernière étape (semaines 13–14) consiste à réaliser tes cartes et graphiques, à empaqueter ton projet et à rédiger ton rapport final. **Rendu final** : ton site web ; dépose son adresse sur [Moodle]({{ MOODLE_URL }}) avant la fin du semestre.

## 1. Cartes et visualisations
Ton rapport accompagne tes cartes et visualisations (graphiques, chiffres-clés) pour répondre à ta question de recherche. Avant de le rédiger, vérifie que tes cartes respectent les standards cartographiques minimaux vus au fil du cours et incluent :
- un titre ;
- une légende ;
- une échelle ;
- une orientation ;
- les sources ;
- l'auteur ;
- la date.

Des graphiques ou statistiques peuvent compléter la carte.

## 2. Rapport final
Le rapport doit être court (**3 pages au maximum**, sans compter les figures) et structuré comme suit.

### 2.1 Contexte et objectifs
Présente le contexte, les objectifs et ta question de recherche ; mets à jour ton plan d'étude pour refléter tes visualisations finales ; intègre tes hypothèses, ajustées après l'analyse des géodonnées.

### 2.2 Méthodologie

**Géodonnées** : décris brièvement tes données d'origine ; quantifie leur incertitude de mesure (avec les unités) ; donne leur source et leur lien *public* de téléchargement.

**Chaîne de pré-traitement** : décris-la assez clairement pour qu'elle puisse être reproduite, et ajoute son schéma en annexe.

### 2.3 Résultats
Présente tes résultats (au moins une carte, complétée si besoin de graphiques ou de statistiques) et analyse-les au regard de tes objectifs et hypothèses.

**1) Régression spatialisée** : ajuste au moins un modèle de régression ou de classification dont tu cartographies les prédictions sur ta zone d'étude. Donne ses **intervalles de confiance** (incertitude sur la relation estimée) ou ses **intervalles de prédiction** (incertitude sur chaque valeur individuelle prédite) en justifiant ton choix.

**2) Incertitudes** : estime quantitativement les incertitudes de mesure, d'estimation et de visualisation, avec les valeurs et unités pertinentes. Si tes résultats s'écartent de tes attentes, discute en 1–2 phrases des limites des données ou des difficultés techniques rencontrées.

### 2.4 Données et métadonnées
Fournis un lien de téléchargement vers ton projet empaqueté (voir la [section 3](#empaquetage), < 2 Go), en veillant à respecter les principes FAIR. Vérifie que tes couches ont des métadonnées complètes.

### Remarques
Le rapport doit être structuré et précis pour permettre la reproductibilité de ton projet par des étudiant·e·s n'ayant pas suivi sa conception. Veille donc à inclure tous les éléments nécessaires à la compréhension et à la réutilisation des données et méthodes.

(empaquetage)=
## 3. Empaquetage et remise du projet
Suis la méthode d'empaquetage du TP1 et la procédure de partage de l'étape II :
1. Regroupe dans un dossier `nom_prenom_projet` : la geodatabase `.gpkg` (couches `source_`, `temp_`, `input_`, `results_`), les rasters (GeoTIFF), le notebook Python maître `.ipynb`, le `README` et le fichier d'environnement, ainsi que le projet `.qgz` et le modèle `.model3` si tu as utilisé QGIS.
2. Vérifie que le projet s'ouvre sans couche manquante (dans QGIS, chemins relatifs : **Projet > Propriétés > Général > Enregistrer les chemins : Relatif**).
3. Comprime le dossier en `nom_prenom_projet.zip`, qui doit peser **moins de 2 Go** : au-delà, **sans compromettre la reproductibilité**, réduis l'étendue géographique des données partagées pour te concentrer sur la zone d'étude, ré-échantillonne les rasters, ou ne conserve que les couches `source_` nécessaires à rejouer la chaîne.
4. Copie le `.zip` sur OneDrive et place son lien de partage sur la page projet de ton site web.
5. Dépose l'adresse de ton site web sur [Moodle]({{ MOODLE_URL }}) : **c'est le rendu final**.

## 4. Critères d'évaluation du rendu final
- Le rendu est complet, conforme aux consignes et déposé dans les délais.
- Le GeoPackage est complet et contient les couches préfixées `source_` / `temp_` / `input_` / `results_`.
- La chaîne de pré-traitements est logique, justifiée et automatisée.
- Le notebook maître Python est exécutable de bout en bout sur une autre machine à partir du `README` et du fichier d'environnement. Il est documenté.
- Les modèles sont correctement ajustés, évalués et comparés ; le choix du modèle retenu est justifié et les résidus sont analysés.
- Les métadonnées sont complètes.
- Les résultats répondent à la question de recherche.
- La carte répond aux exigences de base en cartographie (titre, légende, échelle, orientation, sources, auteur, date).
- Le rapport présente et illustre correctement méthode et résultats avec un commentaire critique.
