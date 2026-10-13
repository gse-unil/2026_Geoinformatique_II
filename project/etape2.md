# Projet individuel - Etape II : Site web, GeoPackage et chaîne de pré-traitements

Cette étape (semaine 7) comporte trois volets : publier ton site web (portfolio & projet), créer et structurer ton GeoPackage, puis construire ta chaîne de pré-traitements. Elle ne fait pas l'objet d'un rendu intermédiaire, mais **ton site web est le support du rendu final** : il accueillera ton rapport et ton notebook Python maître — autant bien le configurer dès maintenant.

## 1. Créer ton site web (portfolio & projet)

Tu vas forker un modèle prêt à l'emploi, le personnaliser, puis le mettre en ligne gratuitement via GitHub Pages.

La configuration se fera sur GitHub Pages. Toutefois, si vous préférez éviter d’avoir un répertoire GitHub public, vous pouvez utiliser GitLab comme alternative (voir les détails plus bas).

### Objectifs pédagogiques

* Configurer GitHub Pages
* Personnaliser un site avec Markdown
* Intégrer un notebook Jupyter comme page du site
* Comprendre la chaîne : fichier `.md` ou `ipynb` → Jupyter Book → site publié

### Concepts clés

* **Markdown** : langage de mise en forme simple (titres avec `#`, listes avec `-`, gras avec `**`). Les fichiers `.md` sont la base du site. [Plus d'information](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet).
* **Jupyter notebook**: Un fichier `.ipynb` est un document Jupyter Notebook utilisé pour le calcul interactif, qui combine du code en direct, des équations, des visualisations et du texte explicatif. [Plus d'information](https://jupyter.org/try-jupyter/lab/).
* **GitHub Pages** : service gratuit de GitHub qui héberge et publie automatiquement un site statique depuis un répertoire. [Plus d'informations](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).
* **Jupyter Book (MyST)** : outil qui transforme des fichiers Markdown et des notebooks Jupyter en site web structuré. Le fichier `myst.yml` contrôle la navigation. [Plus d'information](https://jupyterbook.org).

### Étapes

**1. Forker le [modèle](https://github.com/gse-unil/2026_modele_portfolio)** : Crée ta propre copie du répertoire sur ton compte GitHub.

**2. Activer les workflows**
Onglet *Actions* → cliquer sur *"I understand my workflows, go ahead and enable them"*.

**3. Activer GitHub Pages**
*Settings* → *Pages* → source : **GitHub Actions**.

**4. Personnaliser le contenu**

| Fichier | Contenu |
|---|---|
| `content/apropos.md` | Ta page de présentation |
| `content/img/ma_photo.png` | Ta photo (remplacer le fichier) |
| `content/portfolio.md` | Tes réalisations |
| `content/mon_projet.ipynb` | Ton projet d'analyse |

**5. Mettre à jour la navigation**
Éditer `myst.yml` pour ajouter/retirer des pages de la table des matières.

**6. Publier**
Chaque `commit` déclenche automatiquement la mise à jour du site. L'URL est visible dans *Settings → Pages*.

Les étapes complètes pour réaliser ce projet sont disponibles dans le README du [modèle](https://github.com/gse-unil/2026_modele_portfolio).

### Check-list du site

Au rendu final, ton site doit remplir les points suivants :

| Point | Détail |
|---|---|
| Répertoire configuré | Fork, Actions et Pages activés, site accessible |
| Page *À propos* | Présentation personnelle complète |
| Page *Portfolio* | Contenu pertinent et mis en forme |
| Projet intégré | Notebook maître visible et fonctionnel sur le site, rapport et lien vers le projet empaqueté sur la page projet |
| Navigation | `myst.yml` cohérent avec les pages présentes |
| Qualité Markdown | Mise en forme soignée, pas de contenu brut |

### Optionnel : GitLab (portfolio privé)

Alternative à GitHub si vous ne souhaitez pas de répertoire public.

* Importer le repo GitHub dans GitLab via **Repository by URL**
* Mettre le projet en **Private**
* Activer **Pages → Only project members**
* Ajouter les enseignant·e·s dans **Members (role: Reporter)**

Les étapes complètes pour réaliser ce projet sont disponibles dans le README du [modèle](https://github.com/gse-unil/2026_modele_portfolio).

## 2. Créer et structurer ton GeoPackage

Structure les couches de données dans **une seule geodatabase (GeoPackage, `.gpkg`)**, avec des couches préfixées selon leur rôle :
- `source_` : données sources intactes avant traitement (p. ex. `source_communes`) ;
- `temp_` : résultats intermédiaires et versions de travail (p. ex. `temp_communes_clip`) ;
- `input_` : données utilisées comme entrée de la régression ou de la classification, résultant de la chaîne de pré-traitements (p. ex. `input_votations`) ;
- `results_` : données finales résultant de l'analyse et utilisées pour l'habillage de la carte (p. ex. `results_temperature`).

Les **rasters** (MNT, orthophotos, etc.) sont conservés comme fichiers GeoTIFF à côté du GeoPackage, et zippés lors de l'empaquetage ([étape IV](etape4.md)).

Pour chaque jeu de données, note dès maintenant la source (URL), la licence, la date de téléchargement, le système de coordonnées et la résolution / l'échelle : ces informations iront dans ton `README` et dans ton rapport.

## 3. Construire ta chaîne de pré-traitements

La chaîne de pré-traitements passe des données brutes au **tableau d'analyse** : une ligne par observation, une colonne par variable (la variable à expliquer et les variables explicatives). Elle doit inclure au minimum **trois traitements**, couvrant au moins **deux** catégories d'outils (voir l'[étape I](etape1.md)), et être automatisée, au choix :
- dans QGIS, avec le **Modeleur graphique** (fichier `.model3`) ;
- en Python, dans la première partie de ton notebook maître (voir l'[étape III](etape3.md)).

Vérifie bien que :
- chaque traitement fonctionne ;
- les données intermédiaires sont enregistrées dans le GeoPackage (couches `temp_`), et le tableau d'analyse dans une couche `input_` ;
- la chaîne est logique, justifiée et reproductible.

Une chaîne courte mais justifiée et documentée vaut mieux qu'une chaîne longue et fragile.
