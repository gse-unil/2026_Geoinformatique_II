# TP2 : Sélection, jointures et relations

## Introduction

Ce TP n’aurait pas été possible sans les ressources listées ci-dessous:

* _TP4 du cours “Géomatique et SIG” du Privat-docent Dr. Marj Tonini_

Nos objectifs pédagogiques sont les suivants:

1. Effectuer des requêtes attributaires (sélection par expression)
2. Effectuer des requêtes spatiales (sélection par localisation)
3. Réaliser des jointures attributaires et spatiales entre tables et couches
4. Comprendre les relations entre tables et couches spatiales
5. Créer une mise en page cartographique (_Print Layout_) et exporter une carte au format PDF

## 1\. Télécharger les données du TP

Pour la partie suivante, télécharge les données du TP depuis OneDrive sur ta machine virtuelle en utilisant [cet hyperlien](https://unils-my.sharepoint.com/:f:/g/personal/ayoub_fatihi_unil_ch/IgDD5wH1DzKtTp1vLVbGrsfoAWbEkhSnB92HPaI1e0EiBu0?e=4EmmQr).

## 2\. Requêtes attributaires et requêtes spatiales

Lorsque l’on travaille avec des fichiers de données volumineux, il est indispensable de pouvoir sélectionner les informations qui nous intéressent. Cela est possible en interrogeant les fichiers avec des [requêtes SQL](https://docs.qgis.org/3.40/fr/docs/user_manual/expressions/expression.html). Elles peuvent être de nature [attributaire](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html#working-with-the-attribute-table) – e.g., sélectionne les bâtiments qui ont au moins cinq étages – ou [spatiale](https://docs.qgis.org/3.40/fr/docs/user_manual/introduction/qgis_gui.html#edit) – e.g., sélectionne les bâtiments qui se trouve dans la région métropolitaine de Montréal. Dans cette partie du TP, tu vas te familiariser avec les requêtes SQL, qui sont particulièrement utiles pour extraire ces informations. Dans l’exercice suivant, on va effectuer à nouveau quelques tâches sur les requêtes dans le cadre de ce cours.

Ouvre un nouveau projet et nomme-le à ta discrétion. Ensuite, charge le geopackage  « tp2.gpkg » dans ton explorateur et importe toutes les couches suivantes : `Communes`, `geology_VD`, et `LI_Accident_tecto`.

À l’aide de l’outil [Select Features by Value](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html#filtering-features), dans la couche « geology\_VD », sélectionne la « Nappe de Morcles (Chaine des Aravis incl.) »

Lorsque la sélection fonctionne :
* zoome sur les entités sélectionnées ;
* observe leur répartition spatiale ;
* vérifie combien d’objets ont été sélectionnés.

<details>
<summary>Astuce</summary>
Explore d’abord la table attributaire pour comprendre le champ qui contient la description tectonique du polygone représenté (dans ce cas LEG_TEC_3).
</details>
<br>

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/nappe_morclessss.mp4></iframe>
</details>
<br>

Maintenant on passe aux [expressions](https://docs.qgis.org/3.44/en/docs/user_manual/expressions/expression.html). Les expressions permettent de construire des requêtes plus précises dans QGIS. Elles sont utilisées dans les sélections, les filtres et les calculs attributaires:

* **Sélections simples** : Sélectionner une unité précise

```sql
"LEG_TEC_3" = 'Nappe de Morcles (Chaine des Aravis incl.)'
```

* **Sélections multiples** : Sélectionner plusieurs types d’accidents tectoniques

```sql
"PRODUCTIV" IN (
  'Peu productifs, dans les moraines',
  'Productif, a productivite variable ou faible'
)
```

* **Sélection par intervalle** : Sélectionner les entités dont la surface est comprise entre 300 et 1000 m²

```sql
"AREA" >= 300 AND "AREA" <= 1000
```

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/nappe_morclessss.mp4></iframe>
</details>
<br>

Tu peux maintenant répondre aux 5 premières questions du quiz moodle (première page).

---

Bienvenu.e à nouveau! Maintenant, tu apprendras à effectuer une requête basée sur les caractéristiques spatiales d’une entité.

* Charge dans ton projet le fichier « Communes ».
* Sélectionne les accidents tectoniques de type « Chevauchement principal alpin (certain) » ou « (probable) ».
* Pour terminer, effectue requête spatiale pour ne retenir, parmi les accidents tectoniques sélectionnés, seulement ceux qui se trouvent sur le territoire vaudois (représenté par la couche « Communes »).
  * Pour ce-faire, découvre à travers la documentation en ligne comment utiliser l’outil [Sélection par localisation](https://docs.qgis.org/3.40/en/docs/user_manual/processing_algs/qgis/vectorselection.html#extract-by-location).

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

Ce type de jointure est le plus utilisé. Une [jointure attributaire](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#joining-features-between-two-layers) ajoute des données d’une table à une autre table, à la suite des colonnes existantes. L’opération se base sur un champ (ou attribut) commun aux deux tables appelé clé ou identifiant. Le nom ou la valeur de chaque entité du champ clé doit être le même d’une table à l’autre. En revanche, on peut joindre indifféremment des tables d’attributs appartenant à des couches de nature différente (couches géographiques, table Excel (\*.xls), table au format DBF (\*.dbf), texte ASCII en colonnes (\*.txt), Microsoft Access (\*.accdb), etc.)

Pour apprendre à effectuer une jointure spatiale, on te propose une table comportant le nombre de véhicules pour 1’000 habitants par commune en 2010. L’objectif de l’exercice est de joindre cette table à la couche des communes pour pouvoir visualiser spatialement l’ensemble des données.

Pour cet exercice, charge les couches `Communes` et `VoiturePlus` . À l’aide de [Jointures](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#joining-features-between-two-layers) à partir des propriétés de la couche, effectue la jointure attributaire entre la couche « Communes\_VD » et la table « VoituresPlus » en utilisant les champs « NAME » et « Communes » comme constituants de la clé primaire.

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/join-1.mp4></iframe>
</details>
<br>

Tu peux maintenant répondre à la question 7 (deuxième page du quiz).

### 3.2 Jointures spatiales

Contrairement aux jointures attributaires, qui peuvent être effectuées dans tous les systèmes de gestion de bases de données, les [jointures spatiales](https://docs.qgis.org/3.40/fr/docs/user_manual/processing_algs/qgis/vectorgeneral.html#join-attributes-by-location) sont propres aux SIG. Elles permettent de mettre en relation des couches de données géographiques sur la base de leurs géométries et de la localisation des leurs entités spatiales.

Pour illustrer l’utilisation des jointures spatiales, tu vas déterminer le nom de la commune sur laquelle se trouve chaque bâtiment du campus de l’UNIL.

Pour cet exercice, charge la couche « BatimentsUNIL » dans ton projet. À l’aide de l’outil `Join attributes by location` effectue une jointure spatiale sur la couche des bâtiments de l’UNIL en choisissant comme couche à joindre (contenant l’information spatiale) la couche « Communes ».

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/spatial_join.mp4></iframe>
</details>
<br>

Bravo! Tu peux maintenant continuer sur le quiz moodle (question 8).

### 3.3 Relations

Les [relations](https://docs.qgis.org/3.44/en/docs/user_manual/working_with_vector/joins_relations.html#setting-relations-between-multiple-layers) reposent également sur l'existence d'un champ commun aux tables à lier, mais, cette fois-ci, aucune donnée n'est annexée dans la table de la couche de base. Contrairement aux jointures attributaires (un-à-un), les relations permettent des liens de type **un-à-plusieurs (1-N)** ou **plusieurs-à-plusieurs (N-N)**, ce qui les rend bien plus flexibles pour représenter la réalité du terrain.

Pour ces exercices, charge la géodatabase « Cadastres » dans ton projet. Elle contient trois tables : `Parcelles`, `Proprietaires`, et `Proprietaire_Parcelle` (table intermédiaire reliant les deux premières via les champs `NO_IMM` et `NO_PROPRI`).

#### 3.3.1 Relations un-à-plusieurs (1-N)

Une relation 1-N permet d'associer **une entité parente** à **plusieurs entités enfants**. Dans notre exemple, une parcelle peut apparaître plusieurs fois dans la table `Proprietaire_Parcelle` — une fois par propriétaire qui la détient. La couche `Parcelles` est donc la couche **parente** (clé primaire `NO_IMM`), et `Proprietaire_Parcelle` est la couche **enfant** (clé étrangère `NO_IMM`).

Pour créer cette relation dans QGIS :

1. **Double-clique** sur la couche `Parcelles` dans le panneau des couches pour ouvrir ses **Propriétés**, puis navigue vers l'onglet **Jointures**.
2. Clique sur le bouton **+** en bas du panneau pour ajouter une nouvelle jointure, et remplis les paramètres suivants :
   * **Couche de jointure** : `Proprietaire_Parcelle`
   * **Champ de jointure** : `NO_IMM`
   * **Champ cible** : `NO_IMM`
3. Valide avec **OK**, puis ferme les propriétés de la couche.
4. Ouvre la **table attributaire** de la couche `Parcelles` (clic droit sur la couche > **Ouvrir la table attributaire**). Tu constateras que les colonnes de `Proprietaire_Parcelle` ont été ajoutées à la suite de celles de `Parcelles` pour chaque parcelle correspondante. Explore les lignes pour vérifier que les données des propriétaires apparaissent bien.

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/relations.mp4></iframe>
</details>
<br>

#### 3.3.2 Relations plusieurs-à-plusieurs (N-N)

Lorsque plusieurs entités d'une couche peuvent être associées à plusieurs entités d'une autre, on parle de relation N-N. Dans notre exemple : plusieurs propriétaires peuvent posséder conjointement une même parcelle, et un même propriétaire peut détenir plusieurs parcelles. Une simple jointure attributaire ne retiendrait qu'un seul propriétaire par parcelle. La relation N-N s'appuie sur la **table intermédiaire** `Proprietaire_Parcelle` pour naviguer dans les deux sens.

Le but de cet exercice est de visualiser, pour une parcelle appartenant à plusieurs propriétaires, la liste complète de ces propriétaires. Pour ce faire, il faut créer **deux relations** en chaîne à partir des propriétés du projet :

1. Ouvre **Projet > Propriétés > Relations**, puis clique sur **+** pour créer la première relation (déjà définie en 3.3.1 si tu l'as faite) :
   * **Couche référencée** : `Parcelles`, champ `NO_IMM`
   * **Couche référençante** : `Proprietaire_Parcelle`, champ `NO_IMM`
   * Nom : `Parcelles_vers_PP`
2. Crée une deuxième relation :
   * **Couche référencée** : `Proprietaires`, champ `NO_PROPRI`
   * **Couche référençante** : `Proprietaire_Parcelle`, champ `NO_PROPRI`
   * Nom : `Proprietaires_vers_PP`
3. Active l'outil **Identifier les entités** et clique sur une parcelle. Dans le panneau qui s'ouvre, développe la section **Parcelles_vers_PP** : tu verras la liste des entrées de la table intermédiaire, et pour chacune, les informations du propriétaire associé via la deuxième relation.

<details>
<summary>Solution</summary>
<iframe src=https://wp.unil.ch/dawn/files/2022/10/relations.mp4></iframe>
</details>
<br>

Youhou! Tu peux maintenant finir le quiz moodle.

## 4\. Mise en page cartographique : _Print Layout_

Tu as déjà visualisé et stylisé des couches dans QGIS. Maintenant, tu vas apprendre à **mettre en page** ta carte pour l'exporter en PDF — une compétence que tu réutiliseras dans tous les TP suivants et dans ton projet individuel.

:::{important}
Le [_Print Layout_](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/overview_composer.html#overview-of-the-print-layout) est l'espace de QGIS dédié à la **mise en page** : c'est ici que tu ajoutes titre, légende, échelle, flèche du nord, et que tu exportes ta carte au format PDF ou image.
:::

4a) Ouvre un _Print Layout_ : menu `Projet > Nouvelle mise en page` (ou `Ctrl+P`). Donne-lui un nom, par exemple "Carte_VD".

4b) Ajoute une **carte** : clique sur l'outil ![map](https://docs.qgis.org/3.40/en/_images/mActionAddMap.png) _Ajouter une carte_, puis dessine un rectangle dans la page. Ta carte QGIS apparaît dans ce cadre.

<details>
<summary>Astuce</summary>
Si ta carte apparaît trop petite ou décalée, utilise l'outil <em>Déplacer le contenu</em> (main 🖐️) pour la recentrer, et la molette pour zoomer/dézoomer à l'intérieur du cadre.
</details>
<br>

4c) Ajoute les **éléments d'habillage** essentiels en utilisant les icônes de la barre d'outils latérale :

| Élément | Icône | Où |
|---------|-------|-----|
| [Légende](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_legend.html) | ![legend](https://docs.qgis.org/3.40/en/_images/mActionAddLegend.png) | Barre latérale |
| [Échelle](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_scalebar.html) | ![scalebar](https://docs.qgis.org/3.40/en/_images/mActionScaleBar.png) | Barre latérale |
| [Flèche du nord](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_arrow.html) | ![arrow](https://docs.qgis.org/3.40/en/_images/mActionArrow.png) | Barre latérale |
| Titre | ![label](https://docs.qgis.org/3.40/en/_images/mActionLabel.png) | Barre latérale |

<details>
<summary>Astuce — Titre</summary>
Le titre est un élément de texte : double-clique dessus pour éditer son contenu dans le panneau de propriétés (onglet <em>Propriétés de l'élément</em>).
</details>
<br>

4d) Personnalise ta carte :
* Ajuste la [légende](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_legend.html) : renomme ou masque les couches inutiles (décoche "Auto-update" et modifie manuellement).
* Choisis un [style d'échelle](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_scalebar.html) lisible (par exemple "Box" ou "Line Ticks").
* Vérifie que les **sources des données** sont indiquées (petit texte en bas de la carte).

4e) **Exporte** ta carte au format PDF : menu `Mise en page > Exporter > Exporter au format PDF` (ou l'icône équivalente). Choisis un emplacement sur ton OneDrive.

:::{note}
**Checklist d'habillage cartographique** — à vérifier avant chaque export de carte dans ce cours :

- ☑ Titre descriptif
- ☑ Légende lisible et à jour
- ☑ Échelle graphique
- ☑ Flèche du nord
- ☑ Ton nom + date
- ☑ Source des données
- ☑ Couleurs cohérentes ([ColorBrewer](https://colorbrewer2.org/) recommandé)
:::
