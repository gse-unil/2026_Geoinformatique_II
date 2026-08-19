# Contributing to 2026_Geoinformatique_II

## Setup (local)

This project is built with [Jupyter Book](https://jupyterbook.org/stable).

### 1. Install dependencies

More info [here](https://jupyterbook.org/stable/get-started/install/).

```bash
# create env ...
mamba install -c conda-forge "jupyter-book"
# or
# pip install "jupyter-book>=2.0.0"
```

### 2. Clone the repository

```bash
git clone https://github.com/gse-unil/2026_Geoinformatique_II.git
cd 2026_Geoinformatique_II
```

### 4. Run locally

```bash
./scripts/build_site.sh        # résout les liens Moodle puis construit le site
# ou, sans le script :
python3 scripts/resolve_moodle_links.py && jupyter-book build --html ./_build/src
```

Le site est construit dans `_build/src/_build/html` (le miroir `_build/src` contient
les sources avec les liens Moodle résolus).

## Adding Content

* Use Markdown (.md) or Jupyter notebooks (.ipynb)
* Add content to the relevant section
* Include exercises when appropriate
* For the table of contents:
  * Add new files to the `myst.yml` toc section

## Moodle links (annual update)

**All Moodle links live in `_config/moodle.env`** — never hardcode a
`moodle.unil.ch/...` URL in a page. In the sources, reference links with
placeholders:

```markdown
[Quiz_TP3]({{ MOODLE_QUIZ_TP3 }})
```

To update the links at the start of a new semester:

1. Open the new Moodle course and copy the activity URLs (quiz, CodeRunner, assignments).
2. Edit `_config/moodle.env` and paste the new URLs. Leave a key empty if the
   activity does not exist.
3. Verify locally: `./scripts/build_site.sh --strict` must succeed without warnings.
4. Commit and push — the GitHub Actions deployment rebuilds and publishes the site.

Environment variables (`MOODLE_*`, set in GitHub → Settings → Secrets and
variables → Actions → Variables) override `_config/moodle.env` without a commit.
