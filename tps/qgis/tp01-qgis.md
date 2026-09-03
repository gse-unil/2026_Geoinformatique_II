# TP1 : QGIS & les machines virtuelles

## Introduction

Bienvenue au premier TP du cours de Géoinformatique II !
Nos objectifs pédagogiques sont les suivants :

1. Utiliser les machines virtuelles de l’UNIL
2. Télécharger les données du TP depuis OneDrive
3. Se familiariser avec le logiciel QGIS
4. Visualiser des couches géographiques
5. Sauvegarder un projet QGIS sur OneDrive
6. Éditer l’apparence d’une couche
7. Mesurer la distance entre deux éléments
8. Ouvrir et éditer des tables attributaires
9. Empaqueter un projet QGIS (projet, GeoPackage, rasters et archive ZIP) pour la remise
10. Explorer les systèmes de coordonnées et les projections

Ce TP n’aurait pas été possible sans les ressources listées ci-dessous :

* _TP1 du cours “Géomatique et SIG” de Privat-docent Dr. Marj Tonini_
* _Les tutoriels en ligne du [Manuel d'exercices QGIS](https://docs.qgis.org/3.44/fr/docs/training_manual/index.html)_

Commençons sans plus tarder !

## 1\. Utiliser les machines virtuelles de l’UNIL

1a) La première étape est d’**ouvrir le logiciel _VMware Horizon Client_**. Si tu travailles sur un poste des salles informatiques, le logiciel devrait déjà être installé et il suffit de cliquer sur l’icône du logiciel (copiée ci-dessous à toutes fins utiles). Si tu travailles sur ton propre ordinateur, il te faudra d’abord installer le logiciel en suivant les instructions du paragraphe “Installation du logiciel _VMware Horizon Client_” [à ce lien](https://wiki.unil.ch/ci/books/salles-informatiques-des-facult%C3%A9s/page/vdi-acces).

<img src="https://wp.unil.ch/dawn/files/2022/09/1200x630wa-1024x538.png" width="250">

1b) Connecte-toi en suivant la section « Connexion à une machine virtuelle » [de la même page](https://wiki.unil.ch/ci/books/salles-informatiques-des-facult%C3%A9s/page/vdi-acces) :

* clique sur **Nouveau serveur** ;
* entre l’adresse `vdi.unil.ch` ;
* connecte-toi avec tes identifiants **UNIL** ;
* double-clique sur la machine virtuelle pour l'ouvrir.

1c) Ton poste de travail devrait maintenant ressembler à celui de la capture ci-dessous. Si nécessaire, quitte le mode « Plein écran » avec le bouton _Fullscreen_, comme dans le tutoriel.

<details>
<summary>Tutoriel</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_1.gif>
</details>

## 2\. Télécharger les données du TP depuis OneDrive

Télécharge les données du TP sur ta machine virtuelle depuis le [dossier OneDrive du cours](https://unils-my.sharepoint.com/:f:/g/personal/tom_beucler_unil_ch/IgAbdMV6LtilQocQhWgGGyIrAecbnnShumSyv65fPHE8yqw?e=PeZ9wa). Ouvre le dossier `tp1`, puis télécharge son contenu dans un dossier local avant de poursuivre.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_2-1.gif>
</details>

## 3\. Se familiariser avec le logiciel QGIS

3a) Ouvre le logiciel QGIS depuis ta machine virtuelle ou localement.

:::{note} Installer QGIS localement
Si tu préfères travailler directement sur ton propre ordinateur plutôt que sur une machine virtuelle UNIL, tu peux installer QGIS localement.

1. Télécharge QGIS depuis le site officiel : <https://qgis.org/fr/site/forusers/download.html>
2. Choisis la version recommandée pour ton système d’exploitation (Windows, macOS ou Linux).
3. Lance l’installateur téléchargé.
4. Garde les options d’installation par défaut.
5. Une fois l’installation terminée, ouvre QGIS Desktop.
:::

3b) Depuis la page d'accueil, ouvre le modèle **OpenStreetMap Basemap** dans l'onglet **Modèles** (_Templates_) pour te familiariser avec l’interface de QGIS.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00001.gif>
</details>

3c) Navigue jusqu'au bâtiment Géopolis. Quelles sont ses coordonnées ?

<details>
<summary>Solution</summary>
<br>
Tu peux trouver les coordonnées d'un point en plaçant ton curseur sur ce point et en lisant les coordonnées indiquées en bas au centre de ton écran. Les coordonnées de Géopolis sont approximativement 732 416,60 et 5 865 133,56 dans le système de coordonnées EPSG:3857 — WGS 84 / Pseudo-Mercator. 
</details>

## 4\. Visualiser des couches géographiques

Maintenant que tout est installé, tu peux charger et manipuler les données géographiques. Tu travailleras avec une carte des lacs, des villes, des routes et de la topographie suisses.

![](https://wp.unil.ch/dawn/files/2022/09/Lausanne-1024x576.jpeg)

Aerial view of Leman lake – Lausanne city in Switzerland  
Par [Samuel B.](https://stock.adobe.com/ch_fr/contributor/200820058/samuel-b?load_type=author&prev_url=detail)

4a) Dans le panneau **Explorateur**, repère le GeoPackage `tp1.gpkg`, développe-le, puis ouvre le projet `tp1_main_prj` qu'il contient. Consulte au besoin la documentation sur les [fichiers de projet](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/project_files.html#working-with-project-files) et le [Manuel d'exercices QGIS](https://docs.qgis.org/3.40/fr/docs/training_manual/index.html).

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00002.gif>
</details>

4b) Explore les propriétés des couches [vectorielles](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/vector_properties.html) et [raster](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_properties.html) : fais un clic droit sur une couche, puis choisis **Propriétés**. Repère notamment sa source, son type de géométrie ou son nombre de bandes, ainsi que son SCR.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00003.gif>
</details>

4c) Réponds aux questions de la première page du “Quiz\_TP1” sur [Moodle]({{ MOODLE_QUIZ_TP1 }}) en utilisant les propriétés de chaque couche. Chaque réponse est enregistrée, mais tu peux soumettre de nouvelles réponses sans pénalité après avoir reçu du feedback de Moodle.

## 5\. Sauvegarder un projet QGIS sur OneDrive

Nous arrivons désormais à un élément essentiel de chaque TP, surtout étant donné la nature parfois instable de nos connexions internet : sauvegarder nos projets sur [OneDrive](https://www.microsoft.com/fr-fr/microsoft-365/onedrive/online-cloud-storage) pour pouvoir y accéder après la fermeture de notre session virtuelle.

5a) Si tu ne l’as pas déjà fait, suis les [instructions à ce lien](https://www.unil.ch/ci/onedrive) (accède au service) pour créer ton compte OneDrive avec tes identifiants de l’UNIL.

5b) **Après avoir créé ton compte OneDrive**, tu pourras sauvegarder ton projet dans le dossier “OneDrive – Université de Lausanne”.

<details>
<summary>Solution</summary>
<br>
  <img loading="lazy" src=https://wp.unil.ch/dawn/files/2023/09/onedrive-geomatique.gif>
</details>

5c) Attention, il faut bien attendre le symbole “vu” dans le statut du téléchargement OneDrive.

5d) Vérifie que tu peux maintenant accéder à ton projet depuis n’importe quel navigateur en utilisant [cet hyperlien](https://onedrive.live.com/login/).

## 6\. Éditer l’apparence d’une couche

Maintenant que ton projet est sauvegardé de manière fiable, tu peux améliorer l'apparence de la carte !

![](https://wp.unil.ch/dawn/files/2022/09/AdobeStock_222755735-1024x1024.jpeg)

Hand drawing Switzerland maps with hand lettering. Illustration. EPS 10.  
Par [angkanasu](https://stock.adobe.com/ch_fr/contributor/204890139/angkanasu?load_type=author&prev_url=detail)

:::{note}
Ici, tu modifies l'apparence des couches **directement dans le canevas cartographique** de QGIS. Tu apprendras à créer une **mise en page** complète (titre, légende, barre d'échelle, flèche du nord et export PDF) au **TP2**.
:::

6a) Familiarise-toi avec les outils de [navigation dans la carte](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/qgis_gui.html#view) : zoome, dézoome et déplace-toi sur la Suisse à l'aide de la souris (molette pour le zoom, clic gauche + glisser pour déplacer).

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00004.gif>
</details>

6b) Affiche le nom des villes : Pour cela, ouvre les propriétés de la couche `Towns` puis l'[onglet **Étiquettes**](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/vector_properties.html#labels-properties). Choisis le champ `ID1`, puis personnalise l'affichage si tu le souhaites.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00005.gif>
</details>

6c) Affiche le nom des lacs suisses avec une taille de police plus petite que celle des villes.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00006.gif>
</details>

6d) Agrandis les symboles représentant les villes et modifie leur couleur dans l'[onglet **Symbologie**](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/vector_properties.html#symbology-properties).

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00007.gif>
</details>

6e) Épaissis la ligne séparant les cantons et change la couleur de remplissage pour mieux les faire apparaître.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00008.gif>
</details>

6f) De même, change la couleur et l’épaisseur des routes pour mieux les faire apparaître.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00009.gif>
</details>

6g) Joue avec les propriétés de la couche “HillShadeCH” pour améliorer ta carte, et [modifie sa transparence](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_properties.html#transparency-properties) (par exemple utilise une transparence de 50%).

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00010.gif>
</details>

6h) Ajuste l’ordre des couches en les faisant glisser dans le panneau **Couches**, afin de mettre en valeur les informations qui t’intéressent le plus.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00011.gif>
</details>

6i) N’oublie pas de sauvegarder ton projet et de le transférer sur OneDrive car ce serait dommage de perdre cette belle carte.

<details>
<summary>Solution</summary>
Suis le tutoriel ci-dessous pour sauvegarder ton projet. Pour le transferer sur One Drive, utilise les indications de la section 5.

<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00012.gif>
</details>

## 7\. Mesurer la distance entre deux éléments

7a) Activer l'accrochage

Avant de mesurer précisément une distance, active l'**accrochage** (_snapping_) afin que le curseur s'accroche automatiquement aux entités.

1. Affiche la **Barre d'outils d'accrochage** avec **Vue > Barres d'outils > Accrochage**, puis active l'icône aimant 🧲.
2. En utilisant l'icone à droite de l'aimant, ouvre les **Options d'accrochage…**. Utilise ensuite l'outils de configuration avancé pour activer l'accrochage pour les couches souhaitées, par exemple `Towns` et `Lakes`.
3. Choisis :
   * **Type** : Sommet (vertex en anglais)
   * **Tolérance** : par exemple `10 pixels`

<details>
<summary>Notes</summary>
* Vérifie que l’icône 🧲 est activée.
* Lorsque tu approches le curseur d’une ville ou d’un bord de lac, un petit marqueur apparaît automatiquement.
</details>

7b) Mesurer la distance entre deux éléments

Nous allons maintenant utiliser l’outil de mesure de QGIS.

1. Clique sur l’outil **Mesurer une ligne** dans la barre d’outils
   (_ou_ menu **Vue > Mesurer > Mesurer une ligne**).
2. Zoome sur la zone qui t’intéresse.
3. Clique sur une première ville.
4. Clique ensuite sur une deuxième ville pour mesurer la distance entre elles.
5. Lis la distance affichée dans la fenêtre de mesure.
6. Répète l’opération pour mesurer l’étendue du **Lac Léman** d’une extrémité à l’autre.

<details>
<summary>Solution</summary>
Cette solution utilise un "raccourci" sans ouvrir la fenêtre d'option d'accrochage. Dans notre cas, cela n'a pas d'impact sur le résultat!
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00013.gif>

Exemples de distances :
* Lausanne ↔ Genève : environ 51,3 km
</details>

Maintenant, réponds aux questions du “Quiz\_TP1” sur [Moodle]({{ MOODLE_QUIZ_TP1 }}). Tu peux reprendre le test autant de fois que tu le souhaites.

## 8\. Ouvrir et éditer des tables attributaires

:::{important}
La **table attributaire**, élément central des systèmes d’information géographique, **organise** et **affiche** les informations détaillées relatives aux entités d’une couche donnée. Chaque **ligne** de la table correspond à une **entité**, tandis que les **colonnes** contiennent ses **attributs** spécifiques. Cette table permet d’effectuer des recherches, des sélections, des tris, des filtrages et des modifications sur les entités.
:::

![](https://wp.unil.ch/dawn/files/2022/09/AdobeStock_126427751-1024x683.jpeg)

Table with numerical data  
Par [Elena Abrazhevich](https://stock.adobe.com/ch_fr/contributor/204136066/elena-abrazhevich?load_type=author&prev_url=detail)

Pour rendre tout cela plus concret, jouons de suite avec ces tables attributaires, et n’oublie pas de répondre aux questions correspondantes sur la deuxième page du “Quiz\_TP1” sur [Moodle]({{ MOODLE_QUIZ_TP1 }}).

8a) Ouvre les [tables attributaires](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html) des villes et des cantons. Trie-les d'abord par ordre alphabétique, puis par population.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00014.gif>
</details>

Tu peux ajouter ou supprimer des champs dans une table attributaire. Les champs peuvent être de différents types :

* numérique (entier, entier long, nombre décimal, etc.) ;
* alphanumérique (texte) ;
* date et heure ;
* etc.

Tu peux calculer les valeurs d'un champ avec la [**Calculatrice de champs**](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html#using-the-field-calculator), qui permet d'effectuer des calculs généraux ou liés à la géométrie des entités (longueur, surface, périmètre, coordonnées du centroïde, etc.).

8b) Active le mode **Édition**, puis utilise la **Calculatrice de champs** pour créer, dans la couche `Roads`, un champ décimal `longueur_km`. Vérifie que la couche utilise un SCR projeté en mètres, puis saisis l'expression `$length / 1000` pour obtenir la longueur de chaque route en kilomètres.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00015.gif>
</details>

8c) Examine les [statistiques](https://docs.qgis.org/3.40/fr/docs/training_manual/vector_analysis/spatial_statistics.html#follow-along-basic-statistics) de la longueur des routes.
<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00016.gif>
</details>

8d) Effectue une sauvegarde finale de ton projet. N’oublie pas de finir de répondre aux questions du “Quiz\_TP1” sur [Moodle]({{ MOODLE_QUIZ_TP1 }}) si tu souhaites obtenir la note maximale.

## 9. Sauvegarder et partager ton projet

::: {important}
Tout au long des TP, **continue à travailler avec le même projet QGIS et
le même GeoPackage**. Le GeoPackage (`.gpkg`) permet de regrouper dans
un seul fichier tes couches vectorielles, leur mise en forme et ton
projet QGIS.

Lorsque tu dois rendre ou partager ton travail, il suffit d'en préparer
une copie.
:::

9a) Prépare une copie pour la remise

Fais une copie de ton GeoPackage et renomme-la :

`nom_prenom_TP1.gpkg`

Ouvre cette copie dans QGIS et vérifie que ton projet et toutes tes
couches s'affichent correctement.

::: {tip}
Tu peux ouvrir un projet enregistré dans un GeoPackage depuis **Projet
\> Ouvrir depuis \> GeoPackage...**.
:::

9b) Vérifie les fichiers externes

Certaines données, notamment les **rasters** (`.tif`, `.asc`, etc.),
peuvent être enregistrées en dehors du GeoPackage.

Si ton projet en utilise (par exemple dans le TP4) :

1. crée un dossier `nom_prenom_TP1` ;
2. place ton GeoPackage et les rasters nécessaires dans ce dossier ;
3. ouvre le projet et vérifie que les rasters s'affichent correctement
    ;
4. si un raster est manquant, ajoute le fichier correspondant au projet
    depuis l'interface **Couches** de QGIS, puis **sauvegarde à nouveau
    le projet**.

Ton dossier pourra par exemple contenir :

``` text
nom_prenom_TP1/
├── nom_prenom_TP1.gpkg
├── raster_1.tif
└── raster_2.tif
```

9c) Prépare le fichier à partager

Si ton travail est entièrement contenu dans le GeoPackage, tu peux
simplement partager :

`nom_prenom_TP1.gpkg`

Si ton projet utilise également des fichiers externes, comme des
rasters, compresse le **dossier complet** en `.zip` :

`nom_prenom_TP1.zip`

Avant de le partager, ouvre une dernière fois le projet pour vérifier
que **toutes les couches s'affichent correctement**.

9d) Dépose ton travail sur [Moodle]({{ MOODLE_RENDU_TP1 }})

Dépose le fichier demandé (`.gpkg` ou `.zip`, selon le contenu de ton
projet) sur [Moodle]({{ MOODLE_RENDU_TP1 }}) avant la
semaine prochaine.

Le lien de dépôt est également indiqué dans la section [Évaluation et
rendus](../overview/tp01.md#tp1-rendus) du TP1.

::: {note}
**À retenir :**

* **Projet + couches vectorielles** → un seul fichier `.gpkg` peut
    suffire.
* **Projet avec des rasters externes** → mets le `.gpkg` et les
    rasters dans un dossier, vérifie le projet, puis partage le dossier
    en `.zip`.
:::

## 10\. Exploration des systèmes de coordonnées et projections

Dans cet exercice, tu vas afficher et explorer différentes projections cartographiques afin d’étudier les distorsions induites au niveau de la direction, des surfaces et des distances.

Dans le panneau **Explorateur**, ouvre le projet `tp1_crs_prj` stocké dans le GeoPackage `tp1.gpkg`. QGIS devrait afficher une carte du monde avec des cercles verts : les [indicatrices de Tissot](https://fr.wikipedia.org/wiki/Indicatrice_de_Tissot).

Maintenant, réponds aux questions du “Quiz\_TP1” sur [Moodle]({{ MOODLE_QUIZ_TP1 }}). Tu peux reprendre le test autant de fois que tu le souhaites.

Pour changer le SCR du projet, clique sur l'indicateur de SCR dans l'angle inférieur droit de QGIS ou ouvre **Projet > Propriétés > SCR**. Recherche ensuite le nom ou l'identifiant de la projection dans la liste. Consulte au besoin la [documentation sur les systèmes de coordonnées](https://docs.qgis.org/3.40/fr/docs/gentle_gis_introduction/coordinate_reference_systems.html#now-you-try).

Identifiants de SCR à essayer :

* `EPSG:4326`
* `ESRI:54009`
* `ESRI:54030`
* `EPSG:3857`

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00017.gif>
</details>
