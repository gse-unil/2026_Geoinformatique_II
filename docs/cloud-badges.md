# Exécuter les TPs Python dans le cloud — badges Colab / Kaggle / Renku

Chaque notebook des TPs Python (`tps/python/tp-py01.ipynb` … `tps/python/tp-py04.ipynb`,
ainsi que `tps/python/project_example_landslides.ipynb`) commence par une cellule contenant trois badges :

| Badge | Service | Cible du lien |
|-------|---------|---------------|
| <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" width="130"> | Google Colab | ouvre le notebook GitHub dans Colab |
| [![Open in Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/kernels/welcome?src=https://github.com/gse-unil/2026_Geoinformatique_II/blob/main/tps/python/tp-py01.ipynb) | Kaggle | importe le notebook GitHub dans l'éditeur Kaggle |
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

## 1. Colab — lien direct

Le badge Colab est un simple lien markdown vers
`https://colab.research.google.com/github/gse-unil/2026_Geoinformatique_II/blob/main/tps/python/<notebook>.ipynb`
— aucun entretien, rien à configurer. Si le notebook est renommé ou déplacé,
mettre à jour le lien à la main dans la cellule badge.

## 2. Kaggle — manuel (pas de badge officiel)

**État des lieux vérifié (août 2026) :** Kaggle n'offre **pas** de badge/lien officiel
« Open in Kaggle » équivalent à Colab. La mécanique officielle d'import est uniquement
dans l'interface : dans l'éditeur de notebook, *File → Open Upload Notebook → GitHub*
(texte présent dans le code de l'application Kaggle), puis coller l'URL du notebook
GitHub. Une URL « profonde » du type `kaggle.com/kernels/welcome?src=…` n'est **pas**
documentée et n'est pas fiable (elle crée un scratchpad sans importer le contenu).

Le badge Kaggle inséré dans les notebooks pointe donc vers cette URL d'import non
documentée : **il faut le tester**. Si Kaggle le casse, le lien reste correct :
`https://github.com/gse-unil/2026_Geoinformatique_II/blob/main/tps/python/tp-py01.ipynb`.

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
4. **Coller le lien dans les notebooks** : remplacer l'URL du badge Renku dans la
   cellule badge des 5 notebooks (actuellement `https://renkulab.io`) par le lien de
   lancement (`https://renkulab.io/p/<namespace>/<slug>/sessions/<launcherId>/start`).
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

- [x] Badges insérés dans les 5 notebooks (Colab lien direct, Kaggle + Renku liens)
- [x] Lien Renku statique dans les 5 notebooks (à mettre à jour quand le launcher existe)
- [ ] Tester le badge Kaggle une fois dans un navigateur (lien non documenté)
- [ ] Vérifier le badge Renku dans un navigateur (lien du launcher)
- [ ] (Option) Déposer `requirements-cloud.txt` et les données dans le projet Renku
