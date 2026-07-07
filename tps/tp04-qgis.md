# TP4 : Opérations Raster

## Introduction

Au cours de ce TP, tu vas te familiariser avec certains outils de géotraitement pour les données au format raster (=image). Tu travailleras avec des données satellites au format raster (provenant de la [NASA](https://www.nasa.gov/)), une couche thématique raster qui identifie les classes d’occupations du sol (créée par nos soins avec les données satellites de la NASA) et enfin un MNT (modèle numérique de terrain) que tu extrapoleras (grâce à la méthode de l’IDW “Inverse Distance Weighting”) à partir de données ponctuelles disponibles sur Swisstopo.

Nos objectifs pédagogiques sont les suivants:

1. Explorer les métadonnées d'un raster (bandes, résolution, CRS)
2. Fusionner des bandes spectrales raster en un seul fichier multibandes
3. Utiliser la calculatrice raster pour dériver de nouvelles informations
4. Effectuer une interpolation spatiale (IDW) à partir de données ponctuelles
5. Réaliser des cartes thématiques raster et empaqueter le projet QGIS

Ce TP n’aurait pas été possible sans les ressources listées ci-dessous:

* _TP7 du cours “Géomatique et SIG” du Privat-docent Dr. Marj Tonini_

## 1\. Téléchargement des données du TP et exploration des métadonnées

1a) Télécharge à [cet hyperlien](https://unils-my.sharepoint.com/:f:/g/personal/ayoub_fatihi_unil_ch/IgDD5wH1DzKtTp1vLVbGrsfoAWbEkhSnB92HPaI1e0EiBu0?e=4EmmQr) un dossier qui contient déjà les couches nécessaires ainsi qu'une mise en page finale de la carte que tu pourras utiliser pour l'habillage.

1b) Ouvre le dossier compressé `zip` que tu viens de télécharger. Il contient les couches raster que nous allons utiliser :

* MapTicino1990\_8classes.tif : occupation du sol en 1990 au Tessin avec une classification en 8 classes (“Forêt”, “Prés”, “Eau”, “Neige”, “Sols nus”, “Aires urbaines”, “Nuages”, “Ombres”) et calculées à partir des données de Landsat4.
* Landsat4\_1990\_194028\_bx.tif : les 7 bandes spectrales individuelles collectées par le satellite Landsat 4 de la NASA (b1: Bleu ; b2:Vert ; b3: Rouge ; b4: Proche infrarouge ; b5: Infrarouge moyen -1 ; b6: Thermique ; b7: Infrarouge moyen -2).
* MNT\_Ticino.tif : un modèle numérique de terrain du Canton Tessin. Nota bene : ce n’est pas ce MNT qu’il faudra utiliser pour la carte finale ! Cette couche nous servira uniquement comme base de calcul.

1c) Vérifie que le [système de référence](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_projections/working_with_projections.html#project-coordinate-reference-system) pour ton projet est bien: (EPSG: 2056 - CH1903+ LV95). Tu peux maintenant commencer le TP.

1d) Prends le temps d’explorer les métadonnées des couches (on parle de métadonnées, mais il s’agit, dans QGIS, des informations de la couche [ongler Information sous Propriétés de la couche {double-clicke la couche}]) et réponds aux premières questions sur le quiz Moodle. Choisis bien les métadonnées de la **bande 4** pour répondre aux questions.

Pour la suite du quiz Moodle, nous allons travailler sur les [bandes](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_properties.html#raster-properties-dialog) spectrales qui apparaissent comme 7 couches séparées. Afin d’effectuer les opérations d’analyse d’image, il faudra les fusionner dans un fichier multibandes unique. Pour ce faire, il existe un outil nommé [Raster > Miscellaneous > Merge](https://docs.qgis.org/3.44/fr/docs/training_manual/rasters/data_manipulation.html#merging-rasters).

1e) Une fois le menu de l’outil ouvert, sélectionne les fichiers qui correspondent à chaque bande **en ordre croissant** (de b1 à b7). Et coche `Place each input file in a separate layer`.

1f) Sauvegarde la nouvelle image satellitaire comme fichier `.tif` (GeoTIFF). C'est ce raster multibandes que tu utiliseras pour toute la suite du TP.

1g) Explore la visualisation de ta nouvelle image satellitaire, en essayant différent combinaisons.

<details>
<summary>Solution – Merge</summary>
<img src=https://wp.unil.ch/dawn/files/2022/11/Composite-Band.gif>
</details>
<br>

## 2\. Analyse des bandes spectrales

2a) Pour commencer, il faut uniquement visualiser la couche multibandes que tu viens de créer, en décochant toutes les autres couches depuis la fenêtre [Couches](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/qgis_gui.html#layer). Cela évitera que QGIS ne doive rafraîchir toutes les couches à chaque fois que tu bouges sur la carte.

2b) Ouvre l'onglet de symbologie dans la fenêtre des propriétés de la couche multibandes (double-clique la couche) et essaye les différentes combinaisons de bandes comme bandes rouge, verte et bleue.

2c) Après t’être familiarisé.e avec le fonctionnement des bandes, essaye de reproduire les compositions du tableau ci-dessous, qui indique la composition recommandée pour les images Landsat.

![](https://wp.unil.ch/dawn/files/2022/11/Schermata-2022-11-11-alle-16.22.28-1024x285.png)

Des opérations peuvent être effectuées sur les différentes bandes de façon à mettre en évidence certains éléments. Dans le menu "Raster", tu trouveras l’outil [Calculatrice raster](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_analysis.html#raster-calculator) qui te permet de faire différentes analyse basées sur les images multibandes.

Une des fonctions qui peuvent être appliquées à un raster multibandes est le calcul du NDVI. Cet index de végétation normalisé (“Normalized Difference Vegetation Index”) met en évidence la couverture végétale sur le territoire. Il est très utilisé en agriculture et sylviculture pour connaître l’état de santé des plantes, comme le montre l’image ci-dessous.

![](https://wp.unil.ch/dawn/files/2022/11/plants.jpg)

Source à consulter pour plus d’informations : [https://eos.com/blog/ndvi-faq-all-you-need-to-know-about-ndvi/](https://eos.com/blog/ndvi-faq-all-you-need-to-know-about-ndvi/)

Sur QGIS le calcul de cet indicateur est automatique, et effectué grâce à la formule ci-dessous :

![](https://wp.unil.ch/dawn/files/2022/11/image.png)

Où R désigne la réflectance spectrale dans la bande rouge (la bande 3 dans le TP) et PIR (ou NIR, Near InfraRed en anglais) indique la réflectance spectrale dans la bande du Proche-Infrarouge (la bande 4).

2d) Applique la fonction NDVI dans la [Calculatrice raster](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_analysis.html#raster-calculator) .

2e) Explore désormais les autres outils d'analyse raster disponibles dans la [Boîte à outils de traitements](https://docs.qgis.org/3.40/fr/docs/user_manual/processing/toolbox.html) (menu `Traitement > Boîte à outils`), notamment sous la catégorie `Raster Analysis`. Par exemple, QGIS propose un algorithme [NDVI](https://docs.qgis.org/3.40/fr/docs/user_manual/processing_algs/qgis/rasteranalysis.html#id2) prêt à l'emploi. Réponds ensuite aux questions de la deuxième page du quiz Moodle.

<details>
<summary>Solution NDVI</summary>
`( "tp7_landsat@4" - "tp7_landsat@3" )  /  ( "tp7_landsat@4" + "tp7_landsat@3" )`
![](https://wp.unil.ch/dawn/files/2022/11/NDVI.gif)
</details>
<br>

2f) Sauvegarde bien la nouvelle couche du NDVI dans ta géodatabase ! Tu devras utiliser ce rendu à la fin du travail.

## 3\. Correction du raster

Le raster “MapTicino1990\_8classes.tif” est une cartographie de l’occupation du sol au Tessin en 1990. Les données sont recueillies par le satellite Landsat 4 de la NASA, et ensuite analysées de sorte à créer 8 classes d’occupation du sol : “Forêt”, “Prés”, “Eau”, “Neige”, “Sols nus”, “Aires urbaines”, “Nuages”, “Ombres”.

La fonction qui permet de faire cette différenciation en se basant uniquement sur les données satellitaires (les 7 bandes spectrales vues plus haut) est par contre très sensible et engendre des erreurs.

L’erreur principale qu’on retrouve est due à la similitude entre les longueurs d’ondes émises par les sols nus et les sols anthropiques (les zones urbaines). Ainsi, on retrouve des pixels classés comme “aires urbaines” en haute montagne à la place d’une classification comme “sols nus”.

Pour corriger ces erreurs, on va utiliser une seconde fois la [Calculatrice Raster](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_analysis.html#raster-calculator).

3a) Ouvre l’outil en question et essaye de trouver l’expression qui te permet de modifier les valeurs erronées dont on a parlé avant (lis d’abord la suite avant de t’y attaquer). En pratique, il faudra créer une requête permettant de modifier l’affectation des pixels classés comme “zone urbaine” et situés au-dessus de 1’400 mètres d’altitude en les classants comme “sols nus”.

**⚠️** Utilise les variables ainsi que les opérateurs offerts par l’outil. Tu pourrais écrire toi-même le tout, mais il arrive que les symboles ne soient pas identiques, ce qui pourrait engendrer une erreur. En outre, si tu fais une erreur minime dans l’écriture des couches, l’outil produira un autre message d’erreur.

Voici quelques exemples de requêtes qui peuvent être menées :

* _(“MapTicino1990\_8classes@1” == 4)_ : sélection de tous les pixels de la couche “MapTicino1990\_8classes” ayant une valeur égale à 4 (c.à.d. qui appartiennent à la classe “neige”).
* _(“MNT25\_Ticino@1” < 600)_ : sélection de tous les pixels situés à une altitude inférieure à 600 mètres dans le MNT “MNT25\_Ticino”.

Les deux requêtes ci-dessus donneront comme résultat un nombre, puisqu’elles indiqueront combien de pixels répondent à la requête en question. Elles donnent aussi la position de ces pixels.

Il existe aussi des fonctions conditionnelles, qui s’appliquent uniquement dans le cas où une condition préalablement fixée est respectée.

* _if( condition, valeur-si-vrai, valeur-si-faux)_ : cette requête appliquera la valeur “valeur-si-vrai” dans le cas où la condition initiale est respectée ; et appliquera la valeur “valeur-si-faux” dans le cas où la condition initiale n’est pas respectée. Il fonctionne de la même manière que le “=SI()” dans Excel.
* _if ( (“MNT25\_Ticino@1” > 600) , 600 , “MNT25\_Ticino@1”)_ : cette requête définit un plafond d’altitude à 600 mètres. La condition est “si le MNT25\_Ticino présente une valeur **supérieure** à 600 mètres d’altitude, assigne la valeur de 600m” ; “si le MNT25\_Ticino présente une valeur **inférieure** à 600 mètres d’altitude, laisse la valeur d’origine”.

Les requêtes ci-dessus ont une seule condition, mais on peut très bien indiquer plusieurs conditions à remplir avec le symbole “&”.

_if ( ( “MNT25\_Ticino@1” > 600) & (“MapTicino1990\_8classes@1” == 7) , 4 , “MapTicino1990\_8classes@1” )_ : cette requête modifie la classification des pixels 7 (“ombres”) en pixels 4 (“neige”) si l’altitude est supérieure à 600 mètres. Donc : “si le MNT indique une valeur supérieure à 600 m, et que le pixel appartient à la classes 7 “Ombres”, alors assigne la valeur du pixel à 4 (“neige”). Si une des condition n’est pas remplie, laisse la valeur d’origine”.

⚠️ C’est une requête de ce type qui te permettra d’effectuer le reclassement des pixels ayant la valeur 6 “Aires urbaines” et situés au-dessus de 1’400 mètres d’altitude en pixels avec valeur 5 “Sols nus”.

3b) Effectue la requête, puis, une fois la requête effectuée, sauvegarde le résultat dans une nouvelle couche que tu nommeras avec la mention “ReClass” (ex. ReClass\_MapTicino1990\_8classes).

Garde cette couche dans ton géopackage car elle te sera redemandée plus tard pour le rendu final.

<details>
<summary>Solution reclassement</summary>
Si tu ne visualises pas la vidéo ci-dessous, active le mode plein écran si tu es sur MacOS, ou tourne ton appareil si tu es sur iOS ou iPadOS. La vidéo est toujours visible depuis Windows (sur les machines virtuelles).

<iframe src=https://wp.unil.ch/dawn/files/2022/11/ReCLass.mp4></iframe>

Étant donné la qualité de la vidéo, on t’offre un zoom sur la condition qui a été utilisée. Essaye toutefois de l’écrire toi-même avant de regarder la solution.

<details>
    <summary>SolutionRequête</summary>
    <pre>if (  ( "MNT25_Ticino@1" > 1400 )  AND  ( "MapTicino1990_8classes@1" = 6 ) , 5, "MapTicino1990_8classes@1" )</pre>
    <img src=https://wp.unil.ch/dawn/files/2022/11/Schermata-2022-11-13-alle-14.13.27.png>
</details>
<br>
</details>
<br>

## 4\. Interpolation

Bravo, tu as presque fini ! Dans cette dernière partie, tu créeras un MNT à partir de données ponctuelles disponibles sur le site de l’Office fédéral de topographie (Swisstopo). Il s’agit du modèle numérique de base du terrain de la Suisse, utilisé pour la production du MNT avec une maille de 25 m. Pour ce faire, on se basera sur une méthode déterministe classique, à savoir la pondération par l’inverse de la distance ou [_Inverse Distance Weighting_ (IDW)](https://docs.qgis.org/3.40/fr/docs/gentle_gis_introduction/spatial_analysis_interpolation.html#inverse-distance-weighted-idw).

Les phénomènes spatio-continus sont définis en tout point de l’espace géographique (ex. l’altitude et la température) mais sont généralement étudiés à travers des données ponctuelles. Entre les points d’échantillonnage, les valeurs de ces phénomènes ne sont pas mesurées. L’objectif des méthodes d’interpolation consiste à prédire ces valeurs inconnues sur la base de l’autocorrélation spatiale :

« _Deux objets proches ont plus de chance \[d’interagir\] que deux objets éloignés_ » ([première loi de la géographie](https://support.esri.com/fr-fr/gis-dictionary/tobler-s-first-law-of-geography) de Waldo Tobler).

Pour qu’une modélisation soit satisfaisante, il est primordial qu’elle soit basée sur une analyse exploratoire des données et sur une analyse des erreurs (quelle que soit la méthode d’interpolation choisie).

Le but de ce TP est d’interpoler assez rapidement (au détriment de la qualité du résultat) une surface raster à partir de données ponctuelles de l’altitude.

4a) Pour télécharger les données, rends-toi sur le site de swisstopo et appuie sur « [DHM25 – Modèle de base ESRI Shapefile](https://cms.geo.admin.ch/ogd/topography/DHM25_BM_SHP.zip) » qui se trouve sous l’onglet Géodonnées et applications > Modèles d’altitude > MNT25.

4b) Ensuite, importe le fichier shape « **dhm25\_p** » dans ton projet (sans oublier de [dézipper](https://support.microsoft.com/fr-fr/windows/compresser-et-d%C3%A9compresser-des-fichiers-f6dde0a7-0fec-8294-e1d3-703ed85e7ebc) le fichier, deux dossiers en seront extraits).

Pour prédire l’altitude en tout point de l’espace géographique Suisse on utilisera l’outil [IDW](https://docs.qgis.org/3.40/fr/docs/gentle_gis_introduction/spatial_analysis_interpolation.html#inverse-distance-weighted-idw).

4c) Cherche cet outil dans la [boîte à outil de traitements](https://docs.qgis.org/3.40/fr/docs/user_manual/processing/toolbox.html).

4d) Grâce à cet outil, estime le MNT à partir des données Swisstopo.
* Coche `Utiliser la coordonnée Z pour l'interpolation` et puis ajoute le en clickant le plus vert
* Pixel size: 900

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/11/Enregistrement-20221115_180606.gif>
</details>
<br>

4e) Finalement, génère une représentation 3D de la surface du MNT grâce à l’outil _Hillshade_ ([Ombrage](https://docs.qgis.org/3.40/fr/docs/training_manual/rasters/terrain_analysis.html#follow-along-calculating-a-hillshade)) sous `Raster > Analysis > Ombrage`.

## 5\. Créer les trois cartes de résultats

Il ne te reste plus qu’à rendre tes résultats sur Moodle. Pour ce faire, crée trois [mises en page](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/overview_composer.html#overview-of-the-print-layout) (_Print Layouts_) : **NDVI**, **occup\_sol**, et **IDW**, avec lesquelles tu pourras exporter les rasters respectifs au format `.pdf`.

5a) Pour chaque mise en page, fais correspondre l’information présente sur la carte à son titre. Pour modifier les couches affichées, il te suffit d’activer/désactiver les couches dans le panneau [Couches](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/qgis_gui.html#layer) de ton projet avant d'ajouter la carte à la mise en page. Tu peux aussi créer plusieurs [thèmes de couches](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/qgis_gui.html#layer-themes) si tu souhaites basculer rapidement entre les trois rendus.

5b) Pour la carte concernant l’occupation du sol, insère une [légende](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_legend.html) qui illustre les 8 classes. Utilise un [rendu de classification paletté](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_properties.html#paletted-rendering) sur la couche `ReClass\_MapTicino1990\_8classes` pour que chaque classe ait sa propre couleur.

5c) Finalement, pour chaque carte, ajoute les éléments d'habillage cartographique essentiels : [échelle](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_scalebar.html), [flèche du nord](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_arrow.html), titre, ainsi que ton nom, prénom et les **sources des données** (NASA Landsat 4, Swisstopo).

## 6\. Rendus et paquetage du projet

6a) Tu peux d’ores et déjà soumettre les trois cartes au format `.pdf` sur Moodle : [Rendus\_Cartes\_TP4](https://moodle.unil.ch/mod/assign/view.php?id=1736952). N’oublie pas le format du rendu : **_nom\_prenom\_cartes\_TP4.pdf_** (tu peux consulter la grille d’évaluation sur Moodle). Pour exporter une mise en page en PDF, utilise `Projet > Mises en page > Exporter > Exporter au format PDF` ou le bouton équivalent dans la fenêtre du _Print Layout_.

6b) Pour le rendu du projet, rassemble tes rasters de résultats (les fichiers `.tif` : image multibandes, NDVI, reclassement et MNT IDW) dans un dossier unique, puis compresse-le en `.zip`. Nomme l'archive de manière logique (ex. _nom\_prenom\_TP4.zip_).

6c) Copie le fichier `.zip` de la machine virtuelle sur ton OneDrive et crée un lien de partage.

6d) Tu peux maintenant te rendre à nouveau sur Moodle pour soumettre à ce lien : [Rendus\_projet\_TP4](https://moodle.unil.ch/mod/quiz/view.php?id=1736953). N’oublie pas le format du rendu : **_nom\_prenom\_TP4.zip_**

Félicitations pour avoir terminé le TP et à la semaine prochaine pour la création du portfolio !
