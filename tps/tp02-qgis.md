# Requêtes attributaires

#TODO!

# Sélection, jointures et relations

[almost ready - needs alternative to `relates`]

## Introduction

Ce TP n’aurait pas été possible sans les ressources listées ci-dessous:

* _TP4 du cours “Géomatique et SIG” du Privat-docent Dr. Marj Tonini_

## 1\. Télécharger les données du TP

Pour la partie suivante, télécharge les données du TP depuis OneDrive sur ta machine virtuelle en utilisant [cet hyperlien](https://unils-my.sharepoint.com/:f:/g/personal/tom_beucler_unil_ch/Ett_32gi9rBEq6Sq0OPY5VIB0n5U2Y_3cpc-uX05fA3DtA?e=gm2gkF).

## 2\. Requêtes attributaires et requêtes spatiales

Lorsque l’on travaille avec des fichiers de données volumineux, il est indispensable de pouvoir sélectionner les informations qui nous intéressent. Cela est possible en interrogeant les fichiers avec des [requêtes SQL](https://docs.qgis.org/3.40/fr/docs/user_manual/expressions/expression.html). Elles peuvent être de nature [attributaire](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html#working-with-the-attribute-table) – e.g., sélectionne les bâtiments qui ont au moins cinq étages – ou [spatiale](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/qgis_gui.html#edit) – e.g., sélectionne les bâtiments qui se trouve dans la région métropolitaine de Montréal. Dans cette partie du TP, tu vas te familiariser avec les requêtes SQL, qui sont particulièrement utiles pour extraire ces informations. Dans l’exercice suivant, on va effectuer à nouveau quelques tâches sur les requêtes (cf. [TP3](https://wp.unil.ch/dawn/sig_tp3/)).

Ouvre un nouveau projet et nomme-le à ta discrétion. Ensuite, charge la geopackage  « Geology\_VD.gdb » dans ton projet et importe toutes les couches présentes. À l’aide de l’outil [Select By Attributes](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html#filtering-features), dans la couche « geology\_VD », sélectionne la « Nappe de Morcles (Chaine des Aravis incl.) »

<details>
<summary>Astuce</summary>
Explore d’abord la table attributaire pour comprendre le champ qui contient la description tectonique du polygone représenté (dans ce cas d’ordre 3).
</details>
<br>

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/nappe_morclessss.mp4></iframe>
</details>
<br>

Tu peux maintenant répondre aux 5 premières questions du quiz moodle (première page).

---

Bienvenu.e à nouveau! Maintenant, tu apprendras à effectuer une requête basée sur les caractéristiques spatiales d’une entité. Charge dans ton projet le fichier « Communes ». Sélectionne les accidents tectoniques de type « Chevauchement principal alpin (certain) » ou « (probable) ». Pour terminer, effectue requête spatiale pour ne retenir, parmi les accidents tectoniques sélectionnés, seulement ceux qui se trouvent sur le territoire vaudois (représenté par la couche « Communes »). Pour ce-faire, découvre à travers la documentation en ligne comment utiliser l’outil [Sélection par localisation](https://docs.qgis.org/3.40/en/docs/user_manual/processing_algs/qgis/vectorselection.html#extract-by-location).

<details>
<summary>Astuce</summary>
Utilise le Selection Type « Select subset from the current selection »
</details>
<br>

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/nappes_vaud.mp4></iframe>
</details>
<br>


## 3\. Jointures et Relations

Félicitations, maintenant que tu es un.e expert.e en requêtes attributaires et spatiales dans QGIS, c’est le moment de passer [aux jointures et aux relations](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#connecting-and-editing-data-across-layers).

Les données que nous utilisons peuvent provenir de sources différentes. Il est possible de les afficher sur une carte unique, même si ces données proviennent de différentes tables, à une condition : qu’il y ait une relation entre les tables. Généralement, les données statistiques sont disponibles sous forme de tableaux ou de données textuelles. Il va falloir joindre ces données à celles géographiques pour pouvoir les représenter dans une carte. Les jointures de tables attributaires (relation entre éléments un-à-un et/ou plusieurs-à-un), les jointures spatiales et les relations (relation entre éléments plusieurs-à-plusieurs) sont des opérations qui répondent à cette problématique en structurant l’information.

### 3.1 Jointures de tables attributaires

Ce type de jointure est le plus utilisé. Une [jointure attributaire](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#joining-features-between-two-layers) ajoute des données d’une table à une autre table, à la suite des colonnes existantes. L’opération se base sur un champ (ou attribut) commun aux deux tables appelé clé ou identifiant. Le nom ou la valeur de chaque entité du champ clé doit être le même d’une table à l’autre. En revanche, on peut joindre indifféremment des tables d’attributs appartenant à des couches de nature différente (couches géographiques, table Excel (\*.xls), table au format DBF (\*.dbf), texte ASCII en colonnes (\*.txt), Microsoft Access (\*.accdb), etc.

Pour apprendre à effectuer une jointure spatiale, on te propose une table comportant le nombre de véhicules pour 1’000 habitants par commune en 2010. L’objectif de l’exercice est de joindre cette table à la couche des communes pour pouvoir visualiser spatialement l’ensemble des données.

Pour cet exercice, charge la géodatabase « VoituresTourisme\_VD.gdb » dans ton projet et importe toutes les couches présentes. À l’aide de [Jointures](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#joining-features-between-two-layers) à partir des propriétés de la couche, effectue la jointure attributaire entre la couche « Communes\_VD » et la table « VoituresPlus » en utilisant les champs « NAME » et « Communes » comme constituants de la clé primaire.

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/join-1.mp4></iframe>
</details>
<br>

Tu peux maintenant répondre à la question 7 (deuxième page du quiz).

### 3.2 Jointures spatiales

Contrairement aux jointures attributaires, qui peuvent être effectuées dans tous les systèmes de gestion de bases de données, les [jointures spatiales](https://docs.qgis.org/3.40/fr/docs/user_manual/processing_algs/qgis/vectorgeneral.html#join-attributes-by-location) sont propres aux SIG. Elles permettent de mettre en relation des couches de données géographiques sur la base de leurs géométries et de la localisation des leurs entités spatiales.

Pour illustrer l’utilisation des jointures spatiales, tu vas déterminer le nom de la commune sur laquelle se trouve chaque bâtiment du campus de l’UNIL.

Pour cet exercice, charge la géodatabase « Campus.gdb » dans ton projet et importe toutes les couches présentes. À l’aide de l’outil `Join attributes by location` effectue une jointure spatiale sur la couche des bâtiments de l’UNIL en choisissant comme couche à joindre (contenant l’information spatiale) la couche « Communes\_VD ».

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/spatial_join.mp4></iframe>
</details>
<br>

Bravo! Tu peux maintenant continuer sur le quiz moodle (question 8).

### 3.3 Relations

Les [relations](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_vector/joins_relations.html#setting-relations-between-multiple-layers) reposent également sur l’existence d’un champ commun aux tables à lier, mais, cette fois-ci, aucune donnée n’est annexée dans la table de la couche de base. Les relations permettent des liens de type « plusieurs à plusieurs » (souvent symbolisé « n à n »).

Par exemple, imaginez que vous disposiez d’une couche de parcelles et d’une table de leur(s) propriétaire(s) : plusieurs propriétaires pouvant posséder conjointement des parcelles. Avec une relation, la sélection d’une des parcelles dans la couche des parcelles entrainerait automatiquement la sélection de tous les propriétaires se partageant ladite parcelle. Une simple jointure attributaire ne retiendrait qu’un seul propriétaire par bâtiment. Néanmoins, les relations nécessitent généralement l’utilisation d’une table intermédiaire qui stocke des « clés étrangères », c’est-à-dire l’information permettant de répondre à une question du type : quelle(s) parcelle(s) appartien(nen)t à quel(s) propriétaire(s) ?

Le but de cet exercice est de visualiser, pour une parcelle appartenant à plusieurs propriétaires, la liste des propriétaires. Pour ce-faire, il est nécessaire de [créer une relation](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_vector/joins_relations.html#setting-relations-between-multiple-layers) entre les données des bases (« Parcelles » et « Propriétaires ») et la table intermédiaire. Pour ce faire, charge la géodatabase « Cadastres », ouvre la table « Proprietaire\_Parcelle », à l’aide de [Jointures](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#joining-features-between-two-layers) à partir des propriétés de la couche, crée 2 jointures.

1. La première jointure doit relier la couche « Parcelles » à la table « Propriétaire\_Parcelle » sur la base du champ « NO\_IMM ».
2. La deuxièmedoit relier la table des propriétaires à la table « Propriétaire\_Parcelle » sur la base du champ « NO\_PROPRI ».

<!-- Depuis la couche « Parcelles », il est désormais possible d’avoir accès aux informations liées à ces relation en cliquant une parcelle et en explorant le pop-up qui s’ouvre. Pour [afficher les données associées](https://pro.arcgis.com/fr/pro-app/latest/help/data/tables/view-related-data.htm), il suffit de sélectionner une entité dans un tableaux et – depuis le menu latéral – cliquer sur « Related Data ». -->

[No such thing in QGIS, only joins are used and you can use queries as in previous lessons to find the info you are looking for]

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/relations.mp4></iframe>
</details>
<br>

Youhou! Tu peux maintenant finir le quiz moodle.

Félicitations, le TP est terminé ! Tu es désormais prêt.e à créer un projet à partir de zéro. C’est ce que tu feras la semaine prochaine lors du TP5, c’est-à-dire :

<!-- ![](https://wp.unil.ch/dawn/files/2022/10/showtime.jpg) -->

<!-- _“[It’s Showtime](https://knowyourmeme.com/memes/its-showtime)” par shevyrolet_ -->
