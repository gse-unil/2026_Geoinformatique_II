# Projet individuel - Etape II : Création du site web

Cette étape (semaine 7) contient la création et la publication de ton site web (portfolio & projet). Elle ne fait pas l'objet d'un rendu intermédiaire, mais **ton site web est le support du rendu final** : il accueillera ton rapport, ton notebook Python maître, ton géopackage et ton portofolio de comptétence — autant bien le configurer dès maintenant.

Pour créer ton site web, tu vas forker un modèle prêt à l'emploi, le personnaliser, puis le mettre en ligne gratuitement via GitHub Pages.

La configuration se fera sur GitHub Pages. Toutefois, si vous préférez éviter d’avoir un répertoire GitHub public, vous pouvez utiliser GitLab comme alternative (voir les détails plus bas).

## 1.Objectifs pédagogiques

* Configurer GitHub Pages
* Personnaliser un site avec Markdown
* Intégrer un notebook Jupyter comme page du site
* Comprendre la chaîne : fichier `.md` ou `ipynb` → Jupyter Book → site publié

## 2. Concepts clés

* **Markdown** : langage de mise en forme simple (titres avec `#`, listes avec `-`, gras avec `**`). Les fichiers `.md` sont la base du site. [Plus d'information](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet).
* **README** : fichier texte qui explique à quoi sert un projet et comment l’utiliser.
* **Jupyter notebook**: Un fichier `.ipynb` est un document Jupyter Notebook utilisé pour le calcul interactif, qui combine du code en direct, des équations, des visualisations et du texte explicatif. [Plus d'information](https://jupyter.org/try-jupyter/lab/).
* **GitHub Pages** : service gratuit de GitHub qui héberge et publie automatiquement un site statique depuis un répertoire. [Plus d'informations](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).
* **Jupyter Book (MyST)** : outil qui transforme des fichiers Markdown et des notebooks Jupyter en site web structuré. Le fichier `myst.yml` contrôle la navigation. [Plus d'information](https://jupyterbook.org).

## 3. Étapes

### 3.1 - Forker le modèle

La première étape consiste à forker le [répertoire source](https://github.com/gse-unil/2026_modele_portfolio). Cette manipulation te permets de créer ta propre copie du répertoire sur ton compte GitHub, et la marche à suivre est expliquée dans la vidéo présente dans le README du modèle.

### 3.2 - Activer les workflows

Quand tu forkes un projet, les tâches automatiques sont bloquées par défaut pour des raisons de sécurité. Activer les workflows permet de relancer ces automatisations sur ton fork. Pour cela, clique sur l'onglet *Actions* puis sur *"I understand my workflows, go ahead and enable them"*.

### 3.3 - Activer GitHub Pages

Activer GitHub Pages te permets d'indiquer à GitHub que c’est lui qui doit mettre ton site en ligne automatiquement, sans que tu aies à le faire manuellement. pour cela, clique sur *Settings* → *Pages* → source : **GitHub Actions**.

### 3.4 - Personnaliser le contenu

La structure du site web est la suivante : 

| Fichier | Contenu |
|---|---|
| `content/apropos.md` | Page de présentation |
| `content/img/ma_photo.png` | Photo (optionnelle) |
| `content/competences.md` | Portofolio de compétences |
| `content/projet.ipynb` | Notebook maitre Python |
| `content/rapport_final.md` | Notebook maitre Python |

Toutes les fichiers devront être édité pour le rendu final. Tu peux dès maintenant : 
- Ajouter ton portofolio de compétences (AJOUTER COMMENT) créé dans le précédant cours ;
- Modifier le fichier apropos.md pour remplir ta page de présentation ;
- Ajouter ta photo en remplacant le fichier ma_photo.png (cette étape est optionnelle). 


### 3.5 - Mettre à jour la table des natières
Pour éditer la table des matières, édites le fichier `myst.yml` en suivant les instructions fournies dans le README du [modèle](https://github.com/gse-unil/2026_modele_portfolio).

### 3.5 - Plublier le site web
Pour publier et mettre à jour le site web, il faut faire suavegarder tes modification à travers des `commit`, ce qui déclenche automatiquement la mise à jour du site. L'URL du site web est visible dans *Settings → Pages*.

## Check-list du site

Au rendu final, ton site doit remplir les points suivants :

| Point | Détail |
|---|---|
| Répertoire configuré | Fork, Actions et Pages activés, site accessible |
| Page *À propos* | Présentation personnelle complète |
| Page *Portfolio* | Contenu pertinent et mis en forme |
| Projet intégré | Notebook maître visible et fonctionnel sur le site, rapport et lien vers le projet empaqueté sur la page projet |
| Navigation | `myst.yml` cohérent avec les pages présentes |
| Qualité de la mise en page | Mise en forme soignée |

## Optionnel : GitLab (portfolio privé)

Alternative à GitHub si vous ne souhaitez pas de répertoire public.

* Importer le repo GitHub dans GitLab via **Repository by URL**
* Mettre le projet en **Private**
* Activer **Pages → Only project members**
* Ajouter les enseignant·e·s dans **Members (role: Reporter)**

Les étapes complètes pour réaliser ce projet sont disponibles dans le README du [modèle](https://github.com/gse-unil/2026_modele_portfolio).



