# Exécuter les TPs Python dans le cloud — badges Colab / Kaggle / Renku

Chaque notebook des TPs Python (`tps/tp-py01.ipynb` … `tps/tp-py04.ipynb`, ainsi que
`tps/project_example_landslides.ipynb`) commence par une cellule contenant trois badges :

| Badge | Service | Cible du lien |
|-------|---------|---------------|
| <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" width="130"> | Google Colab | ouvre le notebook GitHub dans Colab |
| [![Open in Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/kernels/welcome?src=https://github.com/gse-unil/2026_Geoinformatique_II/blob/main/tps/tp-py01.ipynb) | Kaggle | importe le notebook GitHub dans l'éditeur Kaggle |
| [![Launch on Renku](https://renkulab.io/renku-badge.svg)](https://renkulab.io/p/NAMESPACE/SLUG/sessions/LAUNCHER_ID/start) | Renku (SDSC) | lance une session depuis le projet Renku du cours |

**Important — les données.** Aucun des notebooks ne télécharge ses données :
ils lisent des fichiers locaux (`tp1.gpkg`, `tp2.gpkg`, `tp3.gpkg`,
`project_landslides.gpkg`, CSVs, rasters) que les étudiant·e·s récupèrent sur le
[dossier OneDrive du cours](https://unils-my.sharepoint.com/:f:/g/personal/ayoub_fatihi_unil_ch/IgDD5wH1DzKtTp1vLVbGrsfoAWbEkhSnB92HPaI1e0EiBu0?e=4EmmQr).
Ce dossier est protégé par l'authentification UNIL : ni Colab, ni Kaggle, ni Renku ne
peuvent y accéder automatiquement. Dans chaque environnement, il faut donc **téléverser
les données une fois** dans le répertoire de travail du notebook (voir la cellule d'aide
en tête de chaque notebook).

---

## 1. Colab — automatique (GitHub Action)

Le badge Colab est maintenu automatiquement par le workflow
[`.github/workflows/colab-badges.yml`](../.github/workflows/colab-badges.yml),
basé sur [`trsvchn/colab-badge-action`](https://github.com/trsvchn/colab-badge-action) (v4) :

1. Les notebooks contiennent un **badge suivi** au format HTML
   (`<!--<badge>-->…<!--</badge>-->`) dans leur première cellule markdown.
2. À chaque `push` sur `main`, l'action vérifie tous les notebooks, met à jour le lien
   si le fichier a été renommé/déplacé (ou si la branche/répo change) et insère le badge
   dans tout notebook qui n'en aurait pas.
3. `stefanzweifel/git-auto-commit-action` pousse le résultat.

**À copier ailleurs** (autre répo) : adapter `target_repository` et `target_branch`,
et placer `{{ badge }}` dans une cellule markdown d'un notebook — l'action la remplace
par le badge. Astuce : l'action fonctionne avec le format standard `source` en liste de
lignes ; les notebooks de ce cours utilisent ce format.

## 2. Kaggle — manuel (pas de badge officiel)

**État des lieux vérifié (août 2026) :** Kaggle n'offre **pas** de badge/lien officiel
« Open in Kaggle » équivalent à Colab. La mécanique officielle d'import est uniquement
dans l'interface : dans l'éditeur de notebook, *File → Open Upload Notebook → GitHub*
(texte présent dans le code de l'application Kaggle), puis coller l'URL du notebook
GitHub. Une URL « profonde » du type `kaggle.com/kernels/welcome?src=…` n'est **pas**
documentée et n'est pas fiable (elle crée un scratchpad sans importer le contenu).

Le badge Kaggle inséré dans les notebooks pointe donc vers cette URL d'import non
documentée : **il faut le tester**. Si Kaggle le casse, le lien reste correct :
`https://github.com/gse-unil/2026_Geoinformatique_II/blob/main/tps/tp-py01.ipynb`.

**Procédure étudiante (à ajouter au TP si besoin) :**

1. Cliquer le badge Kaggle (ou copier l'URL GitHub du notebook).
2. Si demandé, se connecter / créer un compte Kaggle (compte Google ou email).
3. Dans l'éditeur : **File → Open Upload Notebook → GitHub** → coller l'URL du fichier
   `.ipynb` → *Import*.
4. Téléverser les données du TP (bouton *Upload* dans le panneau des fichiers) :
   `tp1.gpkg` / `tp2.gpkg` / `tp3.gpkg` / rasters selon le TP.
5. Exécuter la cellule *Setup* si elle existe, puis les cellules dans l'ordre.

> L'import crée une copie dans *Your Work* : les modifications ne remontent pas dans le
> répo du cours. C'est voulu — les étudiant·e·s travaillent sur leur copie.

## 3. Renku — à configurer une fois (SDSC RenkuLab)

Renku (Swiss Data Science Center) propose un **badge officiel de lancement de session**.
Il est généré par l'interface — pas besoin de l'écrire à la main :

1. **Créer le projet Renku** : sur [renkulab.io](https://renkulab.io), *New Project*,
   et importer le répo GitHub du cours
   (`https://github.com/gse-unil/2026_Geoinformatique_II`) — ou *forker* le répo puis
   créer le projet à partir du fork. Le projet doit être **public** pour que les liens
   fonctionnent pour tout le monde.
2. **Créer un session launcher** : section *Launchers* du projet → ➕ → type **Session**.
   Pour l'environnement, deux options :
   - **Global environment** : démarrage immédiat, mais les paquets (`geopandas`,
     `rasterio`, `scikit-learn`, `xgboost`, …) doivent être installés à la volée à
     chaque session (`pip install -r requirements-cloud.txt`) ;
   - **Code-based environment** : pointe Renku vers `requirements-cloud.txt`
     (ou `pyproject.toml`) du répo → environnement pré-construit, paquets prêts à
     l'emploi (recommandé pour un cours).
   Choisir une *resource class* (CPU/RAM) suffisante pour les TPs raster.
3. **Récupérer le badge** : menu du launcher → **Share session launch link** →
   *Copy Launch Badge* (markdown) ou *Copy Launch Link* (URL). L'URL a la forme :
   `https://renkulab.io/p/<namespace>/<slug>/sessions/<launcherId>/start`.
4. **Déclarer l'URL dans le fichier de variables du cours** : dans `_config/moodle.env`,
   renseigner `MOODLE_RENKU_URL=` avec le lien de lancement
   (`https://renkulab.io/p/<namespace>/<slug>/sessions/<launcherId>/start`), puis pousser.
   Les notebooks contiennent déjà le placeholder `{{ MOODLE_RENKU_URL }}` ; le script de
   build (`scripts/resolve_moodle_links.py`) le remplace au moment du déploiement. Tant
   que la valeur est vide, le lien du badge Renku pointe vers `{{ MOODLE_RENKU_URL }}` non
   résolu — penser à le renseigner avant de publier le site. Pour une surcharge ponctuelle
   sans commit, on peut aussi définir `MOODLE_RENKU_URL` comme variable GitHub Actions
   (Settings → Secrets and variables → Actions → Variables) — elle prime sur `moodle.env`.
5. **Déposer les données dans le projet Renku** : l'interface *Upload* du projet ou le
   CLI `renku dataset add`/`renku storage` ; les étudiant·e·s les retrouveront dans le
   répertoire de travail de la session.

**Limite Renku** : un badge lance **toujours le même launcher** (même environnement).
Si les TPs ont des besoins différents, créer un launcher par TP et un badge par
notebook ; l'URL du badge de chaque notebook pointe alors vers son launcher.

**Environnement minimum commun** (`requirements-cloud.txt`) :
`geopandas`, `matplotlib`, `numpy`, `pandas`, `rasterio`, `scipy`, `scikit-learn`,
`statsmodels`, `xgboost`, `sqlite3` (stdlib, présent partout).

---

## Résumé des étapes à faire

- [x] Badges insérés dans les 5 notebooks (Colab automatique, Kaggle + Renku liens)
- [x] Workflow `.github/workflows/colab-badges.yml` (Colab)
- [x] `MOODLE_RENKU_URL` dans `_config/moodle.env` (lien du badge Renku, à renseigner)
- [ ] Tester le badge Kaggle une fois dans un navigateur (lien non documenté)
- [ ] Créer le projet Renku + launcher (voir §3), renseigner `MOODLE_RENKU_URL` dans
      `_config/moodle.env`
- [ ] (Option) Déposer `requirements-cloud.txt` et les données dans le projet Renku
