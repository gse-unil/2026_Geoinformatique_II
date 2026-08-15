# TP2 : Sélection, jointures et relations

## Introduction

Ce TP n’aurait pas été possible sans les ressources listées ci-dessous :

* _TP4 du cours “Géomatique et SIG” du Privat-docent Dr. Marj Tonini_

Nos objectifs pédagogiques sont les suivants :

1. Effectuer des requêtes attributaires (sélection par expression)
2. Effectuer des requêtes spatiales (sélection par localisation)
3. Réaliser des jointures attributaires et spatiales entre tables et couches
4. Comprendre les relations entre tables et couches spatiales
5. Créer une mise en page et exporter une carte au format PDF

## 1\. Télécharger les données du TP

Pour la partie suivante, télécharge les données du TP depuis OneDrive sur ta machine virtuelle en utilisant [cet hyperlien](https://unils-my.sharepoint.com/:f:/g/personal/ayoub_fatihi_unil_ch/IgDD5wH1DzKtTp1vLVbGrsfoAWbEkhSnB92HPaI1e0EiBu0?e=4EmmQr).

## 2\. Requêtes attributaires et requêtes spatiales

Lorsque les données sont volumineuses, il faut pouvoir isoler les entités utiles. Dans QGIS, une [expression](https://docs.qgis.org/3.40/fr/docs/user_manual/expressions/expression.html) permet par exemple de sélectionner les bâtiments d'au moins cinq étages. Une [requête spatiale](https://docs.qgis.org/3.40/fr/docs/user_manual/processing_algs/qgis/vectorselection.html#extract-by-location) sélectionne plutôt les entités selon leur position par rapport à une autre couche. Tu vas pratiquer ces deux approches.

Ouvre un nouveau projet et enregistre-le. Dans le panneau **Explorateur**, repère le GeoPackage `tp2.gpkg`, développe-le, puis ajoute les couches `Communes`, `geology_VD` et `LI_Accident_tecto`.

Dans la couche `geology_VD`, utilise [**Sélectionner les entités par valeur**](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/attribute_table.html#filtering-features) pour sélectionner « Nappe de Morcles (Chaine des Aravis incl.) ».

Lorsque la sélection fonctionne :
* zoome sur les entités sélectionnées ;
* observe leur répartition spatiale ;
* vérifie combien d’objets ont été sélectionnés.

<details>
<summary>Astuce</summary>
Explore d’abord la table attributaire pour repérer le champ qui contient la description tectonique du polygone : `LEG_TEC_3`.
</details>
<br>

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp2/tp2-00001.gif>
</details>
<br>

Passe maintenant aux [expressions](https://docs.qgis.org/3.40/fr/docs/user_manual/expressions/expression.html). Elles permettent de construire des requêtes plus précises pour les sélections, les filtres et les calculs attributaires :

* **Sélection simple** : sélectionner une unité précise

```sql
"LEG_TEC_3" = 'Nappe de Morcles (Chaine des Aravis incl.)'
```

* **Sélection multiple** : sélectionner plusieurs catégories

```sql
"PRODUCTIV" IN (
  'Peu productifs, dans les moraines',
  'Productif, a productivite variable ou faible'
)
```

* **Sélection par intervalle** : sélectionner les entités dont la surface est comprise entre 300 et 1 000 m²

```sql
"AREA" >= 300 AND "AREA" <= 1000
```

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp2/tp2-00002.gif>
</details>
<br>

Tu peux maintenant répondre aux cinq premières questions du quiz Moodle (page `TP 2`).

---

Tu vas maintenant effectuer une requête fondée sur la position spatiale des entités.

* Charge dans ton projet le fichier « Communes ».
* Sélectionne les accidents tectoniques de type « Chevauchement principal alpin (certain) » ou « (probable) ».
* Enfin, effectue une requête spatiale pour ne conserver, parmi les accidents tectoniques sélectionnés, que ceux qui intersectent le territoire vaudois représenté par la couche `Communes`.
  * Utilise l'outil [**Sélection par localisation**](https://docs.qgis.org/3.40/fr/docs/user_manual/processing_algs/qgis/vectorselection.html#select-by-location).

<details>
<summary>Astuce</summary>
Choisis le mode de sélection **Sélectionner un sous-ensemble de la sélection actuelle**.
</details>
<br>

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp2/tp2-00003.gif>
</details>
<br>

## 3\. Jointures et relations

Tu sais maintenant effectuer des requêtes attributaires et spatiales. Passe aux [jointures et aux relations](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#connecting-and-editing-data-across-layers).

Les données proviennent souvent de sources différentes. Pour représenter des statistiques sur une carte, il faut les relier à une couche géographique au moyen d'une clé commune ou d'une relation spatiale. Tu vas comparer trois mécanismes : la jointure attributaire, la jointure spatiale et la relation entre tables.

### 3.1 Jointures de tables attributaires

Ce type de jointure est le plus utilisé. Une [jointure attributaire](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#joining-features-between-two-layers) ajoute des données d’une table à une autre table, à la suite des colonnes existantes. L’opération se base sur un champ (ou attribut) commun aux deux tables appelé clé ou identifiant. Le nom ou la valeur de chaque entité du champ clé doit être le même d’une table à l’autre. Les tables peuvent provenir de formats différents, à condition que QGIS puisse les lire et que les champs de jointure aient des valeurs et des types compatibles.

Pour apprendre à effectuer une jointure attributaire, utilise la table du nombre de véhicules pour 1 000 habitants par commune en 2010. L’objectif est de joindre cette table à la couche des communes afin de cartographier les valeurs.

Charge la couche `Communes` et la table `VoituresPlus`. Dans l'onglet [**Jointures**](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#joining-features-between-two-layers) des propriétés de `Communes`, ajoute une jointure avec `VoituresPlus`. Utilise `Communes` comme **champ de jointure** et `NAME` comme **champ cible**. Vérifie ensuite quelques correspondances dans la table attributaire de `Communes`.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp2/tp2-00004.gif>
</details>
<br>

Tu peux maintenant répondre à la question 7 (deuxième page du quiz).

### 3.2 Jointures spatiales

Contrairement aux jointures attributaires, qui peuvent être effectuées dans tous les systèmes de gestion de bases de données, les [jointures spatiales](https://docs.qgis.org/3.40/fr/docs/user_manual/processing_algs/qgis/vectorgeneral.html#join-attributes-by-location) sont propres aux SIG. Elles mettent en relation des couches géographiques d'après la position de leurs entités.

Pour illustrer l’utilisation des jointures spatiales, tu vas déterminer le nom de la commune sur laquelle se trouve chaque bâtiment du campus de l’UNIL.

Charge la couche `BatimentsUNIL`. Lance l'outil [**Joindre les attributs par localisation**](https://docs.qgis.org/3.40/fr/docs/user_manual/processing_algs/qgis/vectorgeneral.html#join-attributes-by-location) avec `BatimentsUNIL` comme **couche source** et `Communes` comme **couche de jointure**. Choisis le prédicat **est à l'intérieur de** et vérifie que chaque bâtiment reçoit le nom de sa commune.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp2/tp2-00005.gif>
</details>
<br>

Bravo ! Tu peux maintenant poursuivre le quiz Moodle avec la question 8.

### 3.3 Relations

Les [relations](https://docs.qgis.org/3.40/fr/docs/user_manual/working_with_vector/joins_relations.html#setting-relations-between-multiple-layers) reposent aussi sur des champs communs, mais n'ajoutent pas de colonnes à la table de base. Elles permettent de naviguer entre des enregistrements liés, notamment dans des relations **un-à-plusieurs (1-N)** ou **plusieurs-à-plusieurs (N-N)**.

Pour ces exercices, ajoute depuis le GeoPackage `Cadastres.gpkg` les tables `Parcelles`, `Proprietaires` et `Proprietaire_Parcelle`. Cette dernière est une table intermédiaire qui relie les deux premières au moyen des champs `NO_IMM` et `NO_PROPRI`.

#### 3.3.1 Relations un-à-plusieurs (1-N)

Une relation 1-N permet d'associer **une entité parente** à **plusieurs entités enfants**. Dans notre exemple, une parcelle peut apparaître plusieurs fois dans la table `Proprietaire_Parcelle` — une fois par propriétaire qui la détient. La couche `Parcelles` est donc la couche **parente** (clé primaire `NO_IMM`), et `Proprietaire_Parcelle` est la couche **enfant** (clé étrangère `NO_IMM`).

Pour créer cette relation dans QGIS :

1. Ouvre **Projet > Propriétés > Relations**, puis clique sur **+ Ajouter une relation**.
2. Donne-lui le nom `Parcelles_vers_PP` et définis :
   * **Couche référencée (parent)** : `Parcelles` ; champ `NO_IMM`
   * **Couche référençante (enfant)** : `Proprietaire_Parcelle` ; champ `NO_IMM`
3. Valide, puis active l'outil **Identifier les entités** et clique sur une parcelle.
4. Développe la relation `Parcelles_vers_PP` dans le panneau d'identification et vérifie que plusieurs enregistrements enfants peuvent être associés à une même parcelle.

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp2/tp2-00006.gif>
</details>
<br>

#### 3.3.2 Relations plusieurs-à-plusieurs (N-N)

Lorsque plusieurs entités d'une couche peuvent être associées à plusieurs entités d'une autre, on parle de relation N-N. Dans notre exemple : plusieurs propriétaires peuvent posséder conjointement une même parcelle, et un même propriétaire peut détenir plusieurs parcelles. Une simple jointure attributaire ne retiendrait qu'un seul propriétaire par parcelle. La relation N-N s'appuie sur la **table intermédiaire** `Proprietaire_Parcelle` pour naviguer dans les deux sens.

Le but de cet exercice est de visualiser, pour une parcelle appartenant à plusieurs propriétaires, la liste complète de ces propriétaires. Pour ce faire, il faut créer **deux relations** en chaîne à partir des propriétés du projet :

1. Dans **Projet > Propriétés > Relations**, conserve la relation créée en 3.3.1 :
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
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp2/tp2-00007.gif>
</details>
<br>

Tu peux maintenant terminer le quiz Moodle.

## 4\. Mise en page cartographique

Tu as déjà visualisé et stylisé des couches dans QGIS. Maintenant, tu vas apprendre à **mettre en page** ta carte pour l'exporter en PDF — une compétence que tu réutiliseras dans tous les TP suivants et dans ton projet individuel.

:::{important}
La [**Mise en page**](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/overview_composer.html#overview-of-the-print-layout) (_Print Layout_) est l'espace de QGIS dans lequel tu ajoutes un titre, une légende, une barre d'échelle et une flèche du nord, puis exportes la carte au format PDF ou image.
:::

4a) Crée une mise en page avec **Projet > Nouvelle mise en page…** et nomme-la `Carte_VD`.

4b) Ajoute une **carte** : clique sur **Ajouter une carte**, puis dessine un rectangle sur la page. Le contenu du canevas QGIS apparaît dans ce cadre.

<details>
<summary>Astuce</summary>
Si ta carte apparaît trop petite ou décalée, utilise l'outil <em>Déplacer le contenu</em> (main 🖐️) pour la recentrer, et la molette pour zoomer/dézoomer à l'intérieur du cadre.
</details>
<br>

4c) Ajoute les **éléments d'habillage** essentiels en utilisant les icônes de la barre d'outils latérale :

| Élément | Outil QGIS |
|---------|------------|
| [Légende](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_legend.html) | **Ajouter une légende** |
| [Barre d'échelle](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_scalebar.html) | **Ajouter une barre d'échelle** |
| [Flèche du nord](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_image.html#the-picture-item) | **Ajouter une image**, puis choisir une flèche du nord dans les propriétés |
| Titre | **Ajouter une étiquette** |

<details>
<summary>Astuce — Titre</summary>
Le titre est un élément de texte : double-clique dessus pour éditer son contenu dans le panneau de propriétés (onglet <em>Propriétés de l'élément</em>).
</details>
<br>

4d) Personnalise ta carte :
* Ajuste la [légende](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_legend.html) : décoche **Mise à jour auto**, puis renomme ou retire les éléments inutiles.
* Choisis un [style de barre d'échelle](https://docs.qgis.org/3.40/fr/docs/user_manual/print_composer/composer_items/composer_scalebar.html) lisible.
* Vérifie que les **sources des données** sont indiquées (petit texte en bas de la carte).

4e) **Exporte** la carte au format PDF avec **Mise en page > Exporter au format PDF…**. Enregistre le fichier sur OneDrive.

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

<details>
<summary>Solution</summary>
<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/tp2/tp2-00008.gif>
</details>
<br>
