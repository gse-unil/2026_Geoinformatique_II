# TP4 : Opérations raster

## Introduction

Au cours de ce TP, tu vas découvrir plusieurs traitements de données raster. Tu travailleras avec des images satellitaires de la [NASA](https://www.nasa.gov/), une classification de l'occupation du sol dérivée de ces images et un modèle numérique de terrain (MNT) que tu interpoleras par pondération inverse de la distance (IDW) à partir de points de swisstopo.

Nos objectifs pédagogiques sont les suivants :

1. Explorer les métadonnées d'un raster (bandes, résolution, SCR)
2. Fusionner des bandes spectrales raster en un seul fichier multibandes
3. Utiliser la calculatrice raster pour dériver de nouvelles informations
4. Effectuer une interpolation spatiale (IDW) à partir de données ponctuelles
5. Réaliser des cartes thématiques raster et empaqueter le projet QGIS

Ce TP n’aurait pas été possible sans les ressources listées ci-dessous :

* _TP7 du cours “Géomatique et SIG” du Privat-docent Dr. Marj Tonini_

## 1\. Téléchargement des données du TP et exploration des métadonnées

1a) Télécharge à [cet hyperlien](https://unils-my.sharepoint.com/:f:/g/personal/ayoub_fatihi_unil_ch/IgDD5wH1DzKtTp1vLVbGrsfoAWbEkhSnB92HPaI1e0EiBu0?e=4EmmQr) un dossier qui contient déjà les couches nécessaires ainsi qu'une mise en page finale de la carte que tu pourras utiliser pour l'habillage.

1b) Décompresse l'archive `.zip`. Le dossier contient les rasters suivants :

* `MapTicino1990_8classes.tif` : occupation du sol du Tessin en 1990, classée en huit catégories (« Forêt », « Prés », « Eau », « Neige », « Sols nus », « Aires urbaines », « Nuages » et « Ombres ») à partir d'images Landsat 4 ;
* `Landsat4_1990_194028_bx.tif` : sept fichiers correspondant aux bandes Landsat 4 (b1 : bleu ; b2 : vert ; b3 : rouge ; b4 : proche infrarouge ; b5 : infrarouge moyen 1 ; b6 : thermique ; b7 : infrarouge moyen 2) ;
* `MNT25_Ticino.tif` : MNT du canton du Tessin, utilisé uniquement pour le reclassement de l'occupation du sol.

1c) Vérifie que le [système de coordonnées de référence](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_projections/working_with_projections.html#project-coordinate-reference-system) (SCR) du projet est **EPSG:2056 — CH1903+ / LV95**.

1d) Explore les métadonnées de chaque couche : double-clique sur la couche, puis ouvre l'onglet **Information**. Pour le [quiz Moodle]({{ MOODLE_QUIZ_TP4 }}), relève précisément les informations de la **bande 4** : dimensions, résolution, type de données, étendue et SCR.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp4/tp4-00001.gif>
</details>
<br>

Les [bandes](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_properties.html#raster-properties-dialog) spectrales sont fournies dans sept fichiers séparés. Empile-les dans un raster multibande avec **Raster > Divers > Fusionner…** (**_Merge_**).

1e) Ajoute les fichiers **dans l'ordre croissant**, de b1 à b7, puis coche **Placer chaque fichier en entrée dans une bande séparée**.

1f) Sauvegarde la nouvelle image satellitaire comme fichier `.tif` (GeoTIFF). C'est ce raster multibandes que tu utiliseras pour toute la suite du TP.

1g) Explore l'image satellitaire en essayant différentes combinaisons de bandes.

<details>
<summary>Solution — Fusionner</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp4/tp4-00002.gif>
</details>
<br>

## 2\. Analyse des bandes spectrales

2a) Pour commencer, il faut uniquement visualiser la couche multibandes que tu viens de créer, en décochant toutes les autres couches depuis la fenêtre [Couches](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/qgis_gui.html#layer). Cela évitera que QGIS ne doive rafraîchir toutes les couches à chaque fois que tu bouges sur la carte.

2b) Ouvre l'onglet de symbologie dans la fenêtre des propriétés de la couche multibandes (double-clique la couche) et essaye les différentes combinaisons de bandes comme bandes rouge, verte et bleue.

2c) Reproduis les compositions colorées du tableau ci-dessous, qui indique les combinaisons courantes pour les images Landsat.

![](https://wp.unil.ch/dawn/files/2022/11/Schermata-2022-11-11-alle-16.22.28-1024x285.png)

Des opérations entre bandes permettent de mettre en évidence certains phénomènes. Le menu **Raster** contient la [**Calculatrice raster**](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_analysis.html#raster-calculator), qui crée un nouveau raster à partir d'une expression.

L'indice de végétation par différence normalisée (NDVI, _Normalized Difference Vegetation Index_) met en évidence la végétation. Il est couramment utilisé en agriculture et en sylviculture pour suivre son état.

![](https://wp.unil.ch/dawn/files/2022/11/plants.jpg)

Source à consulter pour plus d’informations : [https://eos.com/blog/ndvi-faq-all-you-need-to-know-about-ndvi/](https://eos.com/blog/ndvi-faq-all-you-need-to-know-about-ndvi/)

Le NDVI se calcule avec la formule suivante :

![](https://wp.unil.ch/dawn/files/2022/11/image.png)

Où R désigne la réflectance spectrale dans la bande rouge (la bande 3 dans le TP) et PIR (ou NIR, Near InfraRed en anglais) indique la réflectance spectrale dans la bande du Proche-Infrarouge (la bande 4).

2d) Calcule le NDVI dans la [**Calculatrice raster**](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_analysis.html#raster-calculator). Donne au raster de sortie un type à virgule flottante afin de conserver les valeurs décimales comprises entre −1 et 1.

2f) Enregistre le NDVI dans un fichier GeoTIFF `.tif`. Tu l'utiliseras pour la carte finale.

<details>
<summary>Solution - NDVI</summary>
<code>
( "merged-landsat4-1990@4" - "merged-landsat4-1990@3" )  /  ( "merged-landsat4-1990@4" + "merged-landsat4-1990@3" )
</code>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp4/tp4-00003.gif>
</details>
<br>

## 3\. Correction du raster

Le raster `MapTicino1990_8classes.tif` cartographie l'occupation du sol du Tessin en 1990. Une classification des images Landsat 4 lui attribue huit classes : « Forêt », « Prés », « Eau », « Neige », « Sols nus », « Aires urbaines », « Nuages » et « Ombres ».

La fonction qui permet de faire cette différenciation en se basant uniquement sur les données satellitaires (les 7 bandes spectrales vues plus haut) est par contre très sensible et engendre des erreurs.

L'erreur principale vient de la similarité de la réponse spectrale des sols nus et de certaines surfaces artificialisées. Des pixels de haute montagne sont donc classés à tort comme « aires urbaines » plutôt que comme « sols nus ».

Pour corriger ces erreurs, utilise une seconde fois la [Calculatrice raster](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_analysis.html#raster-calculator).

3a) Dans la Calculatrice raster, construis une expression qui reclasse en « sols nus » les pixels classés « aires urbaines » au-dessus de 1 400 m. Lis les indications suivantes avant de commencer.

**⚠️** Utilise les variables ainsi que les opérateurs offerts par l’outil. Tu pourrais écrire toi-même le tout, mais il arrive que les symboles ne soient pas identiques, ce qui pourrait engendrer une erreur. En outre, si tu fais une erreur minime dans l’écriture des couches, l’outil produira un autre message d’erreur.

Voici quelques exemples de requêtes qui peuvent être menées :

* `"MapTicino1990_8classes@1" = 4` : repère les pixels de la classe 4 (« neige ») ;
* `"MNT25_Ticino@1" < 600` : repère les pixels du MNT situés sous 600 m.

Chacune de ces expressions produit un raster booléen : chaque pixel vaut 1 si la condition est vraie et 0 si elle est fausse. Le résultat indique donc aussi la position des pixels concernés.

Une fonction conditionnelle permet de choisir la valeur de sortie selon qu'une condition est vraie ou fausse :

* _if(condition, valeur_si_vrai, valeur_si_faux)_ applique la première valeur lorsque la condition est vraie et la seconde lorsqu'elle est fausse, comme la fonction `SI()` d'Excel.
* `if("MNT25_Ticino@1" > 600, 600, "MNT25_Ticino@1")` plafonne le MNT à 600 m : les valeurs supérieures deviennent 600 et les autres restent inchangées.

Les expressions précédentes n'ont qu'une condition. Dans la Calculatrice raster de QGIS, combine plusieurs conditions avec l'opérateur `AND`.

`if(("MNT25_Ticino@1" > 600) AND ("MapTicino1990_8classes@1" = 7), 4, "MapTicino1990_8classes@1")` reclasse les ombres (classe 7) en neige (classe 4) au-dessus de 600 m. Si l'une des conditions est fausse, la valeur d'origine est conservée.

⚠️ Adapte cette expression pour reclasser en « Sols nus » (valeur 5) les pixels « Aires urbaines » (valeur 6) situés au-dessus de 1 400 m.

3b) Exécute l'expression et enregistre le résultat dans un GeoTIFF nommé `ReClass_MapTicino1990_8classes.tif`. Tu l'utiliseras dans le rendu final.

<details>
<summary>Solution - reclassement</summary>
<pre>if (  ( "MNT25_Ticino@1" > 1400 )  AND  ( "MapTicino1990_8classes@1" = 6 ) , 5, "MapTicino1990_8classes@1" )</pre>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp4/tp4-00004.gif>
<br>

## 4\. Interpolation

Dans cette dernière partie, tu vas créer un MNT à partir de points altimétriques de l'Office fédéral de topographie (swisstopo). Tu utiliseras une méthode déterministe classique : la [pondération par l'inverse de la distance](https://docs.qgis.org/3.40/fr/docs/gentle_gis_introduction/spatial_analysis_interpolation.html#inverse-distance-weighted-idw), ou IDW (_Inverse Distance Weighting_).

Les phénomènes spatio-continus sont définis en tout point de l’espace géographique (ex. l’altitude et la température) mais sont généralement étudiés à travers des données ponctuelles. Entre les points d’échantillonnage, les valeurs de ces phénomènes ne sont pas mesurées. L’objectif des méthodes d’interpolation consiste à prédire ces valeurs inconnues sur la base de l’autocorrélation spatiale :

« _Tout interagit avec tout, mais deux objets proches ont plus de chances d'interagir que deux objets éloignés._ » ([première loi de la géographie](https://support.esri.com/fr-fr/gis-dictionary/tobler-s-first-law-of-geography) de Waldo Tobler).

Pour qu’une modélisation soit satisfaisante, il est primordial qu’elle soit basée sur une analyse exploratoire des données et sur une analyse des erreurs (quelle que soit la méthode d’interpolation choisie).

L'objectif est de produire rapidement une surface raster d'altitude. La taille de pixel volontairement grossière limite le temps de calcul, au détriment du niveau de détail.

4a) Télécharge les données [DHM25 — Modèle de base ESRI Shapefile](https://cms.geo.admin.ch/ogd/topography/DHM25_BM_SHP.zip) de swisstopo.

4b) Décompresse l'archive principale, qui contient `dhm25_l.zip` et `dhm25_p.zip`. Décompresse ensuite `dhm25_p.zip`, puis ajoute le Shapefile ponctuel `dhm25_p.shp` au projet.

Pour estimer l’altitude entre les points en Suisse, utilise l'outil [IDW](https://docs.qgis.org/3.40/fr/docs/gentle_gis_introduction/spatial_analysis_interpolation.html#inverse-distance-weighted-idw).

4c) Recherche **Interpolation IDW** dans la [boîte à outils de traitements](https://docs.qgis.org/3.40/fr/docs/user_manual/processing/toolbox.html).

4d) Estime le MNT à partir des points swisstopo :
* choisis `dhm25_p` comme couche vectorielle ;
* active **Utiliser la coordonnée Z pour l'interpolation**, puis clique sur le bouton **+** vert pour ajouter la couche à la liste ;
* choisis **Points** comme type de données ;
* définis l'étendue à partir de `dhm25_p` ;
* fixe la taille de pixel à **900 m** en X et en Y ;
* enregistre le résultat dans `MNT_IDW.tif`.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp4/tp4-00005.gif>
</details>
<br>

4e) Génère enfin un [**Ombrage**](https://docs.qgis.org/3.40/fr/docs/training_manual/rasters/terrain_analysis.html#follow-along-calculating-a-hillshade) (**_Hillshade_**) du MNT interpolé avec **Raster > Analyse > Ombrage…**. Utilise d'abord les paramètres par défaut : facteur Z `1`, azimut `315°` et altitude de la lumière `45°`. Enregistre le résultat dans `Ombrage_IDW.tif`. L'ombrage donne une impression de relief, mais ce n'est pas une représentation 3D.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp4/tp4-00006.gif>
</details>
<br>

## 5\. Créer les trois cartes de résultats

Crée trois [mises en page](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/overview_composer.html#overview-of-the-print-layout) : **NDVI**, **occup_sol** et **IDW**. Chacune servira à exporter le résultat correspondant au format PDF.

5a) Crée un [thème de couches](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/qgis_gui.html#layer-themes) pour chaque résultat, puis associe le thème correspondant à l'élément carte de chaque mise en page. Pour la carte **IDW**, affiche le MNT interpolé et superpose l'ombrage avec une transparence adaptée. Verrouille enfin les couches et les styles de chaque élément carte afin qu'un changement dans le canevas ne modifie pas les autres mises en page.

5b) Pour la carte concernant l’occupation du sol, insère une [légende](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_legend.html) qui illustre les 8 classes. Utilise un [rendu de classification paletté](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_properties.html#paletted-rendering) sur la couche `ReClass\_MapTicino1990\_8classes` pour que chaque classe ait sa propre couleur.

5c) Pour chaque carte, ajoute les éléments essentiels : [barre d'échelle](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_scalebar.html), [flèche du nord](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_image.html#the-picture-item), titre, tes nom et prénom, et **sources des données** (NASA Landsat 4 et swisstopo).

## 6\. Rendus et paquetage du projet

6a) Regroupe les trois cartes dans le fichier `nom_prenom_cartes_TP4.pdf`, puis dépose-le dans [Rendus_Cartes_TP4]({{ MOODLE_RENDU_TP4_CARTES }}). Consulte la grille d'évaluation avant la remise. Depuis chaque mise en page, utilise **Mise en page > Exporter au format PDF…** ; fusionne ensuite les trois PDF si nécessaire.

6b) Empaquette le projet selon la méthode du TP1 (§9). Place dans un même dossier le projet `.qgz` et les GeoTIFF nécessaires : image multibande, NDVI, reclassement, MNT IDW et ombrage. Rouvre le projet pour vérifier les chemins, puis compresse le dossier en `nom_prenom_TP4.zip`.

6c) Copie le fichier `.zip` de la machine virtuelle sur ton OneDrive et crée un lien de partage.

6d) Soumets le lien de partage dans [Rendus_projet_TP4]({{ MOODLE_RENDU_TP4_PROJET }}) et vérifie que l'archive porte bien le nom `nom_prenom_TP4.zip`.

Félicitations pour avoir terminé le TP et à la semaine prochaine pour la création du portfolio !
