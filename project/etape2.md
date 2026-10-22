# Projet individuel - Etape II : Création du site web

Cette étape (semaine 7) contient la création et la publication de ton site web (portfolio & projet). Elle ne fait pas l'objet d'un rendu intermédiaire, mais **ton site web est le support du rendu final** : il accueillera ton rapport, ton notebook Python maître, ton géopackage et ton portfolio de compétence — autant bien le configurer dès maintenant.

Pour créer ton site web, tu vas forker un modèle prêt à l'emploi, le personnaliser, puis le mettre en ligne gratuitement via GitHub Pages.

La configuration se fera sur GitHub Pages. Toutefois, si vous préférez éviter d’avoir un répertoire GitHub public, vous pouvez utiliser GitLab comme alternative (voir les détails plus bas).

## 1. Objectifs pédagogiques

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

### 3.1 - Créer un compte Github
Pour commencer, la première étape est de créer un compte [github](https://github.com/).

### 3.2 - Forker le modèle

La première étape consiste à forker le [modèle](https://github.com/gse-unil/2026_modele_portfolio), en suivant la procédure ci-dessous. Cette manipulation te permets de créer ta propre copie du répertoire sur ton compte GitHub. 

<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/projet/etape_II.gif>


### 3.3 - Activer les workflows

Quand tu forkes un projet, les tâches automatiques sont bloquées par défaut pour des raisons de sécurité. Activer les workflows permet de relancer ces automatisations sur ton fork. Pour cela, clique sur l'onglet *Actions* puis sur *"I understand my workflows, go ahead and enable them"*.

### 3.4 - Activer GitHub Pages

Activer GitHub Pages te permet d'indiquer à GitHub que c’est lui qui doit mettre ton site en ligne automatiquement, sans que tu aies à le faire manuellement. Pour cela, clique sur *Settings* → *Pages* → source : **GitHub Actions**.

### 3.7 - Publier le site web

Pour l'instant, ton site n’est pas encore en ligne. Pour le publier, tu dois effectuer une première modification dans le répertoire (par exemple en ajoutant ton nom et prénom) puis la sauvegarder avec un premier `commit`, comme montré dans la vidéo ci-dessous. Tu pourras ensuite accéder à ton site via l’URL disponible dans *Settings* → *Pages*. Si tes modifications n’apparaissent pas immédiatement, c’est tout à fait normal : le déploiement peut prendre quelques minutes.

<img loading="lazy" src=https://raw.githubusercontent.com/gse-unil/materials_for_2026_Geoinformatique_II/refs/heads/main/projet/etape2-commit.gif>

### 3.8 - Personnaliser le contenu

La structure du site web est la suivante : 

| Fichier | Contenu |
|---|---|
| `content/apropos.md` | Page de présentation |
| `content/img/ma_photo.png` | Photo (optionnelle) |
| `content/competences.md` | Portfolio de compétences |
| `content/projet.ipynb` | Notebook maitre Python |
| `content/rapport_final.md` | Notebook maitre Python |

Tous les fichiers devront être édités pour le rendu final. Tu peux dès maintenant: 
- Ajouter ton portfolio de compétences créé dans le précédent cours en remplacent le fichier "portfolio.pdf";
- Modifier le fichier `apropos.md` pour remplir ta page de présentation ;
- Ajouter ta photo en remplacant le fichier ma_photo.png (cette étape est optionnelle). 

N'oublie pas de sauvegarder tes modifications en effectuant des `commit` qui déclencheront automatiquement la mise à jour du site.


### 3.9 - Mettre à jour la table des matières (optionel)
Pour modifier la table des matières, il faut éditer le fichier `myst.yml`, qui contient initialement la structure suivante:
```
toc:
    - file: content/apropos.md
    - file: content/portfolio.md
    - file: content/mon_projet.ipynb
```

Si tu souhaites ajouter une page additionnelle (pour inclure des annexes de ton rapport par exemple), tu peux créer un fichier `content/nom_du_fichier` et l'ajouter dans myst.yml, afin d'obtenir la structure suivante:

```
toc:
    - file: content/apropos.md
    - file: content/portfolio.md
    - file: content/mon_projet.ipynb
    - file: content/nom_du_fichier
```



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

## Optionnel : utiliser GitLab pour un portfolio plus privé

Si tu préfères ne pas avoir un répertoire GitHub public, tu peux dupliquer le modèle de portfolio sur GitLab et restreindre l’accès au répertoire ainsi qu’au site web aux seules personnes invitées.

### 1. Créer un compte GitLab

Créer un compte sur : <https://gitlab.com>

### 2. Dupliquer le modèle de portfolio sur GitLab

1. Dans GitLab, cliquer sur **New project**
2. Sélectionner **Import project**
3. Choisir **Repository by URL**
4. Coller l’URL du répertoire : `https://github.com/gse-unil/2026_modele_portfolio.git`
5. Choisir un nom de projet (par exemple : `portfolio`)
6. Définir la visibilité du répertoire sur : `Private`
7. Cliquer sur **Create project**

### 3. Restreindre l’accès au site web

Pour que seules les personnes autorisées puissent accéder au portfolio :

1. Aller dans **Settings → General**
2. Ouvrir **Visibility, project features, permissions**
3. Vérifier que la visibilité du projet est définie sur : `Private`
4. Dans la section **Pages**, choisir : `Only project members`

### 4. Ajouter les enseignant·e·s au projet

Pour permettre aux enseignant·e·s d’accéder au portfolio :

1. Aller dans **Manage → Members**
2. Cliquer sur **Invite members**
3. Ajouter les identifiants GitLab ou adresses email fournis par les enseignant·e·s
4. Attribuer le rôle : `Reporter`


