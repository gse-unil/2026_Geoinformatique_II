#!/usr/bin/env bash
# Construit le site : résout les placeholders Moodle puis lance Jupyter Book.
# Usage : ./scripts/build_site.sh [--strict]
#   --strict : échoue si un lien Moodle est vide/non défini (recommandé en CI).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 scripts/resolve_moodle_links.py "$@"

JB="${JUPYTER_BOOK:-}"
if [ -z "$JB" ]; then
  if command -v jupyter-book >/dev/null 2>&1; then
    JB="jupyter-book"
  elif [ -x "$ROOT/.venv/bin/jupyter-book" ]; then
    JB="$ROOT/.venv/bin/jupyter-book"
  else
    echo "jupyter-book introuvable (installez-le ou définissez JUPYTER_BOOK)" >&2
    exit 1
  fi
fi

# Le build doit s'exécuter depuis _build/src : c'est là que vit le miroir
# (sources copiées + placeholders résolus + myst.yml). Lancer jupyter-book
# depuis la racine du dépôt construirait les sources non résolues.
cd "$ROOT/_build/src"
"$JB" build --html
echo "✔ Site construit dans $ROOT/_build/src/_build/html"
