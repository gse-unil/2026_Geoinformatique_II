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
* _Les tutoriels en ligne du [Manuel d'exercices QGIS](https://docs.qgis.org/3.40/fr/docs/training_manual/index.html)_

Commençons sans plus tarder !

## 1\. Utiliser les machines virtuelles de l’UNIL

1a) La première étape est d’**ouvrir le logiciel _VMware Horizon Client_**. Si tu travailles sur un poste des salles informatiques, le logiciel devrait déjà être installé et il suffit de cliquer sur l’icône du logiciel (copiée ci-dessous à toutes fins utiles). Si tu travailles sur ton propre ordinateur, il te faudra d’abord installer le logiciel en suivant les instructions du premier paragraphe “Installation du logiciel _VMware Horizon Client_” [à ce lien](https://wiki.unil.ch/ci/books/salles-informatiques-des-facult%C3%A9s/page/vdi-acces).

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

Télécharge les données du TP sur ta machine virtuelle depuis le [dossier OneDrive du cours](https://unils-my.sharepoint.com/:f:/g/personal/ayoub_fatihi_unil_ch/IgDD5wH1DzKtTp1vLVbGrsfoAWbEkhSnB92HPaI1e0EiBu0?e=4EmmQr). Ouvre le dossier `tp1`, puis télécharge son contenu dans un dossier local avant de poursuivre.

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

3b) Depuis la page d'accueil, ouvre un **Nouveau projet vide** ou le modèle **OpenStreetMap Basemap** dans l'onglet **Modèles** (_Templates_) pour te familiariser avec l’interface de QGIS.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00001.gif>
</details>

3c) Navigue jusqu'au bâtiment Géopolis. Quelles sont ses coordonnées ?

<details>
<summary>Solution</summary>
<br>
Les coordonnées de Géopolis sont approximativement 732 416,60 et 5 865 133,56 en EPSG:3857 — WGS 84 / Pseudo-Mercator.
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

4c) Réponds aux questions de la première page du “Quiz\_TP1” sur Moodle en utilisant les propriétés de chaque couche. Chaque réponse est enregistrée, mais tu peux soumettre de nouvelles réponses sans pénalité après avoir reçu du feedback de Moodle.

## 5\. Sauvegarder un projet QGIS sur OneDrive

Nous arrivons désormais à un élément essentiel de chaque TP, surtout étant donné la nature parfois instable de nos connexions internet : sauvegarder nos projets sur [OneDrive](https://www.microsoft.com/fr-fr/microsoft-365/onedrive/online-cloud-storage) pour pouvoir y accéder après la fermeture de notre session virtuelle.

5a) Si tu ne l’as pas déjà fait, suis les [instructions à ce lien](https://www.unil.ch/ci/onedrive) (accède au service) pour créer ton compte OneDrive avec tes identifiants de l’UNIL.

5b) **Après avoir créé ton compte OneDrive**, tu pourras sauvegarder ton projet dans le dossier “OneDrive – Université de Lausanne”.

<details>
<summary>Solution</summary>
<br>
![](https://wp.unil.ch/dawn/files/2023/09/onedrive-geomatique.gif)
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

6a) Familiarise-toi avec les outils de [navigation dans la carte](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/qgis_gui.html#map-canvas) : zoome, dézoome et déplace-toi sur la Suisse à l'aide de la souris (molette pour le zoom, clic gauche + glisser pour déplacer).

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00004.gif>
</details>

6b) Affiche le nom des villes avec l'[onglet **Étiquettes**](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/vector_properties.html#labels-properties) des propriétés de la couche `Towns`. Choisis le champ `ID1`, puis personnalise l'affichage si tu le souhaites.

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
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00010.gif>
</details>

6g) Joue avec les propriétés de la couche “HillShadeCH” pour améliorer ta carte, et [modifie sa transparence](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_properties.html#transparency-properties) (par exemple utilise une transparence de 50%).

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00011.gif>
</details>

6h) Ajuste l’ordre des couches en les faisant glisser dans le panneau **Couches**, afin de mettre en valeur les informations qui t’intéressent le plus.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00012.gif>
</details>

6i) N’oublie pas de sauvegarder ton projet et de le transférer sur OneDrive car ce serait dommage de perdre cette belle carte.

<details>
<summary>Solution</summary>
Voir réponse à la question 5c

<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00012.gif>
</details>

## 7\. Mesurer la distance entre deux éléments

7a) Activer l'accrochage

Avant de mesurer précisément une distance, active l'**accrochage** (_snapping_) afin que le curseur s'accroche automatiquement aux entités.

1. Affiche la **Barre d'outils d'accrochage** avec **Vue > Barres d'outils > Accrochage**, puis active l'icône aimant 🧲.
2. Ouvre les **Options d'accrochage…** et active l'accrochage pour les couches souhaitées, par exemple `Towns` et `Lakes`.
3. Choisis :
   * **Type** : Sommet
   * **Tolérance** : par exemple `10 pixels`
4. Clique sur **OK**.

<details>
<summary>Solution</summary>
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
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00013.gif>

Exemples de distances :
* Lausanne ↔ Genève : environ 51,3 km
</details>

Maintenant, réponds aux questions du “Quiz\_TP1” sur Moodle. Tu peux reprendre le test autant de fois que tu le souhaites.

## 8\. Ouvrir et éditer des tables attributaires

:::{important}
La **table attributaire**, élément central des systèmes d’information géographique, **organise** et **affiche** les informations détaillées relatives aux entités d’une couche donnée. Chaque **ligne** de la table correspond à une **entité**, tandis que les **colonnes** contiennent ses **attributs** spécifiques. Cette table permet d’effectuer des recherches, des sélections, des tris, des filtrages et des modifications sur les entités.
:::

![](https://wp.unil.ch/dawn/files/2022/09/AdobeStock_126427751-1024x683.jpeg)

Table with numerical data  
Par [Elena Abrazhevich](https://stock.adobe.com/ch_fr/contributor/204136066/elena-abrazhevich?load_type=author&prev_url=detail)

Pour rendre tout cela plus concret, jouons de suite avec ces tables attributaires, et n’oublie pas de répondre aux questions correspondantes sur la deuxième page du “Quiz\_TP1” sur Moodle.

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

Tu peux calculer les valeurs d'un champ avec l'outil suivant :

* la [**Calculatrice de champs**](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html#using-the-field-calculator), qui permet d'effectuer des calculs généraux ou liés à la géométrie des entités (longueur, surface, périmètre, coordonnées du centroïde, etc.).

8b) Active le mode **Édition**, puis utilise la **Calculatrice de champs** pour créer, dans la couche `Roads`, un champ contenant la longueur de chaque route. Choisis un type numérique décimal et utilise l'expression `$length`. Vérifie que le SCR de la couche emploie des mètres avant d'interpréter les valeurs.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00015.gif>
</details>

8c) Examine les [statistiques](https://docs.qgis.org/3.40/fr/docs/training_manual/vector_analysis/spatial_statistics.html#follow-along-basic-statistics) de la longueur des routes.
<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00016.gif>
</details>

8d) Effectue une sauvegarde finale de ton projet. N’oublie pas de finir de répondre aux questions du “Quiz\_TP1” sur Moodle si tu souhaites obtenir la note maximale.

## 9\. Empaquetage du projet pour la remise

:::{important}
Pour rendre ton projet sur Moodle, un simple fichier `.qgz` ne suffit pas : il ne contient que les **références** aux couches, pas les données elles-mêmes. Tu dois **empaqueter** ton projet (projet + données) dans un seul fichier `.zip`.
:::

Voici la marche à suivre, que tu réutiliseras pour tous les TP :

**9a) Regroupe les fichiers dans un dossier de remise**

Crée un dossier `nom_prenom_TP1`. Sauvegarde ton projet dans ce dossier au format `.qgz` avec **Projet > Enregistrer sous…**. Un projet `.qgz` conserve la mise en page et les références aux données, mais ne copie pas automatiquement les couches.

<details>
<summary>Astuce</summary>
Un GeoPackage (<code>.gpkg</code>) peut regrouper plusieurs couches vectorielles. Il ne faut toutefois pas confondre l'enregistrement du projet avec la copie de ses données : vérifie que les couches nécessaires se trouvent bien dans ton dossier de remise.
</details>
<br>

**9b) Ajoute les données**

Dans la **Boîte à outils de traitements**, lance **Couches de package**. Sélectionne toutes les couches vectorielles nécessaires au projet et enregistre-les dans `nom_prenom_TP1.gpkg`. Remplace ensuite les couches d'origine par celles du GeoPackage, puis copie dans le dossier les rasters utilisés (`.tif`, `.asc`, etc.). Dans le projet, choisis **Projet > Propriétés > Général > Enregistrer les chemins : Relatif**.

**9c) Compresse le tout en `.zip`**

Ferme puis rouvre le projet depuis le dossier de remise pour vérifier qu'aucune couche n'est manquante. Compresse ensuite le dossier complet en `.zip` et nomme l'archive `nom_prenom_TP1.zip`.

**9d) Dépose le `.zip` sur Moodle** avant la semaine prochaine.

:::{note}
**Récapitulatif de l'empaquetage :**

1. Enregistrer le projet `.qgz` dans un dossier de remise
2. Copier les vecteurs nécessaires avec **Couches de package** et ajouter les rasters
3. Rouvrir le projet et vérifier que toutes les couches sont disponibles
4. Compresser le dossier en `.zip`, puis le déposer sur Moodle
:::

## 10\. Exploration des systèmes de coordonnées et projections

Dans cet exercice, tu vas afficher et explorer différentes projections cartographiques afin d’étudier les distorsions induites au niveau de la direction, des surfaces et des distances.

Dans le panneau **Explorateur**, ouvre le projet `tp1_crs_prj` stocké dans le GeoPackage `tp1.gpkg`. QGIS devrait afficher une carte du monde avec des cercles verts : les [indicatrices de Tissot](https://fr.wikipedia.org/wiki/Indicatrice_de_Tissot).

Maintenant, réponds aux questions du “Quiz\_TP1” sur Moodle. Tu peux reprendre le test autant de fois que tu le souhaites.

Pour changer le SCR du projet, clique sur l'indicateur de SCR dans l'angle inférieur droit de QGIS ou ouvre **Projet > Propriétés > SCR**. Recherche ensuite le nom ou l'identifiant de la projection dans la liste. Consulte au besoin la [documentation sur les systèmes de coordonnées](https://docs.qgis.org/3.40/fr/docs/gentle_gis_introduction/coordinate_reference_systems.html#now-you-try).

Identifiants de SCR à essayer :

* 4326
* 54009
* 54030
* 3857

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp1/tp1-00017.gif>
</details>
