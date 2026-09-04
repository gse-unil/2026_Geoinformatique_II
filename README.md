# Géoinformatique II (UNIL, autumn 2026)

Official repository for the "Géoinformatique II" course, autumn semester 2026 at UNIL.

The site is built with [Jupyter Book 2 / MyST](https://jupyterbook.org/stable) and published
on GitHub Pages: <https://gse-unil.github.io/2026_Geoinformatique_II/>

## Setup

**Deployment is automatic.** Every push to `main` runs
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml), which resolves the Moodle
placeholders into the `_build/src` mirror, runs `jupyter-book build --html` from that
mirror, and publishes the result to Pages. `BASE_URL` is derived from the repository name.
One-time step per repository: set **Settings > Pages > Source** to **GitHub Actions**.

**The important part is filling in [`_config/.env`](_config/.env).** It is the single source
of truth for Moodle links, so no page contains a hardcoded `moodle.unil.ch` URL, only
placeholders like `[Quiz TP3]({{ MOODLE_QUIZ_TP3 }})`. Yearly update: copy the activity URLs
from the new Moodle course into the keys `MOODLE_URL`, `MOODLE_QUIZ_TPn` (QGIS quiz),
`MOODLE_CODERUNNER_TPn` (Python), and `MOODLE_RENDU_*` (submissions), check the build
locally, then commit and push. If a quiz and its CodeRunner are merged into one Moodle
activity, put the same URL in both keys. The note *"accès réservé aux étudiant·e·s UNIL"* is
appended to every Moodle link at build time, so never write it by hand.

**Local build** with [uv](https://docs.astral.sh/uv/):

```bash
uv venv && uv pip install -r requirements.txt   # creates .venv/bin/jupyter-book
./scripts/build_site.sh --strict                # build_site.sh finds .venv on its own
cd _build/src/_build/html && python3 -m http.server 8000   # http://localhost:8000
```

`--strict` fails the build when a referenced placeholder is empty. Run it before every push.

> ⚠️ The workflow does **not** pass `--strict`, so an empty key does not fail the deploy and
> the raw text `{{ MOODLE_QUIZ_TP2 }}` ends up visible on the published site. That is the
> current state for all of TP2, CodeRunner TP1/TP3/TP4, quiz TP4, and the TP1 and TP5
> submissions. Either fill the keys in, or add `--strict` to the *Resolve Moodle links* step.

**Overriding a link without a commit.** `MOODLE_*` variables defined under GitHub
*Settings > Secrets and variables > Actions > **Variables*** take precedence over
`_config/.env`. They hold public URLs, so use Variables and not Secrets. Re-run the workflow
to apply them.

## Check every year

| Item | Why |
|---|---|
| `_config/.env` | new Moodle activity IDs |
| `myst.yml` (`toc`) | a file that is not listed never shows up on the site |
| Notebook badges | the Colab and Kaggle links embed `gse-unil/2026_Geoinformatique_II/blob/main`, and the Renku launcher has to be recreated (see [`docs/cloud-badges.md`](docs/cloud-badges.md)) |
| OneDrive data link | hardcoded in the pages; the data itself is not in the repo (see `.gitignore`) |
| `environment.yml`, `requirements-cloud.txt` | keep in sync with what the notebooks actually import |
| Repository name | renaming it changes `BASE_URL`, and therefore the site URL |

## Good to know

- `_build/` is a build artifact, ignored by git and wiped on every build. Never commit it.
- `_config/.env` is committed on purpose (public URLs only). Keep secrets out of it.
- `pyproject.toml` and `uv.lock` are gitignored, for the local `uv` environment only.
- The workflow only runs on `main`. Nothing is published from a branch or a pull request.

## Contributing

Check the [contributing guide](.github/CONTRIBUTING.md).
