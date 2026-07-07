# TP1 : QGIS & les machines virtuelles

## Introduction

Bienvenue au premier TP du cours de Géoinformatique II!
Nos objectifs pédagogiques sont les suivants:

1. Utiliser les machines virtuelles de l’UNIL
2. Télécharger les données du TP depuis OneDrive
3. Se familiariser avec le logiciel QGIS
4. Visualiser des couches géographiques
5. Sauvegarder un projet QGIS sur SWITCHdrive
6. Éditer l’apparence d’une couche
7. Calculer la distance entre 2 éléments
8. Ouvrir et éditer des tables attributaires
9. Empaqueter un projet QGIS (geopackage + rasters + zip) pour la remise
10. Exploration des systèmes de coordonnées et projections

Ce TP n’aurait pas été possible sans les ressources listées ci-dessous:

* _TP1 du cours “Géomatique et SIG” de Privat-docent Dr. Marj Tonini_
* _Les tutoriels en ligne [“QGIS Training Manual”](https://docs.qgis.org/3.40/en/docs/training_manual/index.html)_

Commençons sans plus tarder!

## 1\. Utiliser les machines virtuelles de l’UNIL

1a) La première étape est d’**ouvrir le logiciel _VMware Horizon Client_**. Si tu travailles sur un poste des salles informatiques, le logiciel devrait déjà être installé et il suffit de cliquer sur l’icône du logiciel (copiée ci-dessous à toutes fins utiles). Si tu travailles sur ton propre ordinateur, il te faudra d’abord installer le logiciel en suivant les instructions du premier paragraphe “Installation du logiciel _VMware Horizon Client_” [à ce lien](https://wiki.unil.ch/ci/books/salles-informatiques-des-facult%C3%A9s/page/vdi-acces).

<img src="https://wp.unil.ch/dawn/files/2022/09/1200x630wa-1024x538.png" width="250">

1b) La deuxième étape est de te connecter en suivant les instructions “Connexion à une machine virtuelle” [au même lien](https://wiki.unil.ch/ci/books/salles-informatiques-des-facult%C3%A9s/page/vdi-acces), copiées ci-dessous à toutes fins utiles:

* Clique sur “Nouveau serveur”
* Entre l’adresse : `vdi.unil.ch`
* Connecte-toi avec tes identifiants **UNIL**
* Entre tes identifiants UNIL dans le client _VMware_
* Double-clique sur la machine virtuelle pour t’y connecter

1c) Tu devrais maintenant avoir un visuel de ton poste de travail similaire à la capture d’écran ci-dessous. N’hésite pas à sortir du mode “plein écran” en cliquant sur le bouton “Fullscreen” comme démontré ci-dessous.

<details>
<summary>Tutoriel</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_1.gif>
</details>

## 2\. Télécharger les données du TP depuis OneDrive

Télécharge les données du TP sur ta machine virtuelle en utilisant [cet hyperlien](https://unils-my.sharepoint.com/:f:/g/personal/ayoub_fatihi_unil_ch/IgDD5wH1DzKtTp1vLVbGrsfoAWbEkhSnB92HPaI1e0EiBu0?e=4EmmQr)

<!-- #TODO! change to only tp1 data later -->

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_2-1.gif>
</details>

## 3\. Se familiariser avec le logiciel QGIS

3a) Ouvre le logiciel QGIS depuis ta machine virtuelle ou localement.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_2.gif>
</details>

:::{note} Installer QGIS localement
Si tu préfères travailler directement sur ton propre ordinateur plutôt que sur une machine virtuelle UNIL, tu peux installer QGIS localement.

1. Télécharge QGIS depuis le site officiel : <https://qgis.org/fr/site/forusers/download.html>
2. Choisis la version adaptée à ton système d’exploitation (Windows, macOS ou Linux).
3. Lance l’installateur téléchargé.
4. Garde les options d’installation par défaut.
5. Une fois l’installation terminée, ouvre QGIS Desktop.
:::

3b) Ouvre un _nouveau projet vide_ pour te familiariser avec l’interface de QGIS.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_4.gif>
</details>

3c) N’hésite pas à t’amuser avec à ajouter des couches (Explorateur > XYZ Tiles > OpenStreetMap). Et puis, rends-toi au Géopolis. Quelles sont les coordonnées?

<details>
<summary>Solution</summary>
<br>
Les cordonnées du Géopolis sont: ~ 46.5265078, 6.5794063
</details>

## 4\. Visualiser des couches géographiques

Maintenant que tout est bien installé, nous sommes enfin prêt à charger et manipuler nos données géographiques! Nous allons travailler sur une carte contenant les lacs, les villes, les routes, et la topographie suisse.

![](https://wp.unil.ch/dawn/files/2022/09/Lausanne-1024x576.jpeg)

Aerial view of Leman lake – Lausanne city in Switzerland  
Par [Samuel B.](https://stock.adobe.com/ch_fr/contributor/200820058/samuel-b?load_type=author&prev_url=detail)

4a) Ouvre le projet nommé `tp1_main_prj` ([fichier de projet](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/project_files.html#working-with-project-files)) situé dans le geopackage `tp1.geopackage` après le connecter à partir de l'explorateur. Prends la bonne habitude dès maintenant de consulter la documentation de QGIS en ligne, par exemple en utilisant [cet hyperlien](https://docs.qgis.org/3.40/en/docs/training_manual/index.html).

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_5.gif>
</details>

4b) Explore les propriétés des fichiers [vecteurs](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_vector/vector_properties.html) / [rasters](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_raster/raster_properties.html) de chaque couche en effectuant un clic droit sur chaque couche avant de sélectionner “Properties”.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_7.gif>
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

Maintenant que nous avons un moyen facile et fiable d’enregistrer notre projet, il est temps de rendre notre carte magnifique!

![](https://wp.unil.ch/dawn/files/2022/09/AdobeStock_222755735-1024x1024.jpeg)

Hand drawing Switzerland maps with hand lettering. Illustration. EPS 10.  
Par [angkanasu](https://stock.adobe.com/ch_fr/contributor/204890139/angkanasu?load_type=author&prev_url=detail)

6a) Ajuste l’étendue de ta carte, par exemple en utilisant la documentation [à ce lien](https://docs.qgis.org/3.40/en/docs/user_manual/print_composer/composer_items/composer_map.html#extents).

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_10.gif>
</details>

6b) Fait apparaître le nom des villes sur la carte en utilisant l’[Onglet Étiquettes](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/vector_properties.html#labels-properties) à partir de la fenêtre propriétés de la couche “Towns” pour faire apparaître le champ “ID1”. N’hésite pas à personaliser ta carte!

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_11.gif>
</details>

6c) Affiche le nom des lacs suisse avec une taille de police plus petite que pour les villes.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_12.gif>
</details>

6d) Agrandis la taille des symboles représentant les villes et change leurs couleurs en utilisant l'[Onglet Symbologie](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/vector_properties.html#symbology-properties).

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_13.gif>
</details>

6e) Épaissis la ligne séparant les cantons et change la couleur de remplissage pour mieux les faire apparaître.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_14.gif>
</details>

6f) De même, change la couleur et l’épaisseur des routes pour mieux les faire apparaître.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_15.gif>
</details>

6g) Joue avec les propriétés de la couche “HillShadeCH” pour améliorer ta carte, et [modifie sa transparence](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_raster/raster_properties.html#transparency-properties) (par exemple utilise une transparence de 50%).

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_16.gif>
</details>

6h) Ajuste l’ordre des couches en les glissant les unes par dessus les autres pour mettre en valeur les informations qui t’intéressent le plus.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_17.gif>
</details>

6i) Tu peux maintenant réajuster l’[étendue de ta carte](https://pro.arcgis.com/fr/pro-app/latest/help/mapping/properties/set-a-custom-full-extent.htm) pour l’admirer dans toute sa splendeur. Qu’est-ce qui a changé dans ta légende?

<details>
<summary>Solution</summary>
Les couleurs ont été mises à jour.
</details>

6j) N’oublie pas de sauvegarder ton projet et de le transférer sur OneDrive car ce serait dommage de perdre cette belle carte.

<details>
<summary>Solution</summary>
Voir réponse à la question 5c
</details>

## 7\. Calculer la distance entre 2 éléments

7a) Activer le _snapping_
Avant de mesurer précisément une distance, il est utile d’activer le **snapping** afin que le curseur “s’accroche” automatiquement aux villes ou aux objets géographiques.

1. Ouvre le menu **Projet > Options de snapping…** (ou clique sur l’icône aimant 🧲 dans la barre d’outils).
2. Active le snapping pour les couches souhaitées (par exemple `Towns` et `Lakes`).
3. Choisis :
   * **Type** : Sommet (_Vertex_)
   * **Tolérance** : par exemple `10 pixels`
4. Clique sur **OK**.

<details>
<summary>Solution</summary>
* Vérifie que l’icône 🧲 est activée.
* Lorsque tu approches le curseur d’une ville ou d’un bord de lac, un petit marqueur apparaît automatiquement.
</details>

7b) Calculer la distance entre deux éléments

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
<img src=[https://wp.unil.ch/dawn/files/2022/09/TP1_20.gif>](https://wp.unil.ch/dawn/files/2022/09/TP1_20.gif>)
Exemples de distances :
* Lausanne ↔ Genève : ~ 51.307 km
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

8a) Accède aux tables attributaires des villes et cantons en passant par la [table d'attributs](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html) et classe les villes/cantons par ordre alphabétique puis par ordre de population.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_19.gif>
</details>

8b) En utilisant l’[outil de mesure](https://docs.qgis.org/3.40/fr/docs/user_manual/map_views/map_view.html#measuring) calcule les distances entre les villes indiquées sur Moodle.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_20.gif>
</details>

Tu peux ajouter (ou effacer) des champs dans une table attributaire. Les champs peuvent être de type différent:

* numérique (“short/long integer”, “float/double”, etc.),
* alphanumérique (“text”),
* date/heure (“dates”),
* etc.

Il est possible de calculer des valeurs de champs grâce à deux outils auxquels tu peux accéder avec un clic droit sur le champ en question:

* “[Field Calculator](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html#using-the-field-calculator)”: Utilise une formule à entrer pour effectuer un calculs généraux (multiplication, addition, etc.) ou relatives à la géométrie des objets (surface, périmètre, centroïde, etc.)

8c) Utilise “Field Calculator” pour créer un nouveau champ avec la longueur des routes suisses dans la table attributaire de la couche “Roads”.

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_21.gif>
</details>

8d) Examine les [statistiques](https://docs.qgis.org/3.40/fr/docs/training_manual/vector_analysis/spatial_statistics.html#follow-along-basic-statistics) de la longueur des routes.
<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP1_22.gif>
</details>

8e) Effectue une sauvegarde finale de ton projet. N’oublie pas de finir de répondre aux questions du “Quiz\_TP1” sur Moodle si tu souhaites obtenir la note maximale.

## 9\. Empaquetage du projet pour la remise

:::{important}
Pour rendre ton projet sur Moodle, un simple fichier `.qgz` ne suffit pas : il ne contient que les **références** aux couches, pas les données elles-mêmes. Tu dois **empaqueter** ton projet (projet + données) dans un seul fichier `.zip`.
:::

Voici la marche à suivre, que tu réutiliseras pour tous les TPs :

**9a) Sauvegarde le projet dans un geopackage**

Au lieu d'un fichier `.qgz`, sauvegarde ton projet **dans** un geopackage `.gpkg` : menu `Projet > Sauvegarder vers > Geopackage…`. Donne-lui un nom comme `nom_prenom_TP1.gpkg`. Le projet QGIS et toutes les couches vectorielles seront stockés dans ce fichier unique.

<details>
<summary>Astuce</summary>
Le geopackage (<code>.gpkg</code>) est un conteneur : il peut regrouper plusieurs couches vectorielles <strong>et</strong> ton projet QGIS dans un seul fichier. C'est le format recommandé pour la remise.
</details>
<br>

**9b) Ajoute les rasters**

Si ton projet utilise des couches **raster** (fichiers `.tif`, `.asc`, etc.), le geopackage ne peut pas les contenir. Place-les dans le même dossier que ton `.gpkg`.

**9c) Compresse le tout en `.zip`**

Sélectionne ton `.gpkg` et les fichiers `.tif` associés, puis compresse-les en un seul fichier `.zip` (clic droit > Compresser, ou `Ctrl+clic > Compresser` sur macOS). Nomme l'archive `nom_prenom_TP1.zip`.

**9d) Dépose le `.zip` sur Moodle** avant la semaine prochaine.

:::{note}
**Récapitulatif de l'empaquetage :**

1. `Projet > Sauvegarder vers > Geopackage` → fichier `.gpkg` (projet + vecteurs)
2. Copier les `.tif` à côté du `.gpkg` (s'il y a des rasters)
3. Sélectionner le tout → compresser en `.zip`
4. Déposer le `.zip` sur Moodle
:::

## 10\. Exploration des systèmes de coordonnées et projections

Dans cet exercice, tu vas afficher et explorer différentes projections cartographiques afin d’étudier les distorsions induites au niveau de la direction, des surfaces et des distances.

Ouvre le projet nommé `tp1_crs_prj` ([fichier de projet](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/project_files.html#working-with-project-files)) situé dans le geopackage `tp1.geopackage` après le connecter à partir de l'explorateur. QGIS devrait te proposer une carte du monde depuis l’espace avec des cercles verts ([les ellipses de Tissot](https://en.wikipedia.org/wiki/Tissot%27s_indicatrix)).

Maintenant, réponds aux questions du “Quiz\_TP1” sur Moodle. Tu peux reprendre le test autant de fois que tu le souhaites.

Pour changer le système de projection de la carte initiale, suis les instructions [de la documentation](https://docs.qgis.org/3.40/fr/docs/gentle_gis_introduction/coordinate_reference_systems.html#now-you-try) pour accéder aux systèmes de coordonnées (_Coordinate system_), tape le nom ou le code EPSG de la projection souhaitée dans la barre de recherche ou cherche manuellement la projection souhaitée depuis la liste.

Projection à essayer:

* 4326
* 54009
* 54030
* 3857

<details>
<summary>Solution</summary>
<img src=https://wp.unil.ch/dawn/files/2022/09/TP2_new_projection-7.gif>
</details>
