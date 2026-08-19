#!/usr/bin/env python3
"""Résout les placeholders ``{{ MOODLE_* }}`` dans les sources MyST.

Copie ``content/``, ``tps/`` et ``myst.yml`` vers ``_build/src`` (miroir de
build), puis remplace chaque ``{{ NOM }}`` par la valeur définie dans :

1. les variables d'environnement ``MOODLE_*`` (priorité la plus haute) ;
2. ``_config/moodle.env`` (fichier source de vérité, commité).

Blocs conditionnels (ligne masquée si la variable est vide/non définie) :

    <!-- MOODLE:if MOODLE_CODERUNNER_TP2 -->
    | ... | [CodeRunner TP2]({{ MOODLE_CODERUNNER_TP2 }}) | ... |
    <!-- MOODLE:endif -->

Usage:
    python scripts/resolve_moodle_links.py [--strict]

``--strict`` : échoue dès qu'un placeholder référencé n'est pas défini
(recommandé en CI — le déploiement ne doit pas publier de liens vides).
Sans ``--strict`` : avertissement, le placeholder est laissé tel quel dans
le miroir afin que l'auteur·rice le voie lors du build local.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIRS = ["content", "tps"]
CONFIG = ROOT / "_config" / "moodle.env"
MIRROR = ROOT / "_build" / "src"

# Fichiers dans lesquels on résout les placeholders (les autres sont copiés tels quels).
TEXT_EXTS = {".md", ".yml", ".yaml", ".ipynb", ".html", ".txt"}

PLACEHOLDER = re.compile(r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}")
BLOCK_START = re.compile(r"<!--\s*MOODLE:if\s+([A-Za-z_][A-Za-z0-9_]*)\s*-->")
BLOCK_END = re.compile(r"<!--\s*MOODLE:endif\s*-->")


def load_values() -> dict[str, str]:
    """Valeurs : _config/moodle.env, surchargées par l'environnement."""
    values: dict[str, str] = {}
    if CONFIG.exists():
        for raw in CONFIG.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            key, _, val = line.partition("=")
            values[key.strip()] = val.strip()
    for key, val in os.environ.items():
        if key.startswith("MOODLE_"):
            values[key] = val
    return values


def resolve_text(text: str, values: dict[str, str], strict: bool,
                 warnings: list[str], errors: list[str]) -> str:
    """Résout blocs conditionnels puis placeholders simples."""

    # --- Blocs conditionnels (non imbriqués) ---
    out: list[str] = []
    i = 0
    while i < len(text):
        m = BLOCK_START.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i:m.start()])
        var = m.group(1)
        end = BLOCK_END.search(text, m.end())
        if not end:
            warnings.append(f"bloc MOODLE:if {var} sans MOODLE:endif")
            out.append(text[m.start():])
            i = m.end()
            continue
        body = text[m.end():end.start()]
        val = values.get(var, "")
        if val:
            out.append(body)
        else:
            # Un bloc MOODLE:if vide est un choix assumé : la ligne est masquée
            # (par ex. quiz théorique et CodeRunner fusionnés → pas de ligne
            # CodeRunner séparée). Jamais bloquant, même en --strict.
            warnings.append(f"MOODLE:if {var} : variable vide, bloc masqué")
        i = end.end()

    text = "".join(out)

    # --- Placeholders simples ---
    def repl(m: re.Match) -> str:
        var = m.group(1)
        val = values.get(var, "")
        if val:
            return val
        msg = f"placeholder {var} non défini"
        if strict:
            errors.append(msg)
        else:
            warnings.append(f"{msg}, laissé tel quel")
        return m.group(0)

    return PLACEHOLDER.sub(repl, text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="échoue si un placeholder est vide/non défini")
    args = parser.parse_args()

    values = load_values()

    # 1. Purge et copie du miroir de build
    if MIRROR.exists():
        shutil.rmtree(MIRROR)
    MIRROR.mkdir(parents=True)
    for src in SRC_DIRS:
        shutil.copytree(ROOT / src, MIRROR / src)
    shutil.copy2(ROOT / "myst.yml", MIRROR / "myst.yml")

    # 2. Résolution des placeholders dans les fichiers texte
    warnings: list[str] = []
    errors: list[str] = []
    n_resolved = 0
    for path in sorted(MIRROR.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTS:
            continue
        if path.name == "myst.yml":
            continue  # déjà copié, résolu ci-dessous
        original = path.read_text(encoding="utf-8")
        resolved = resolve_text(original, values, args.strict, warnings, errors)
        if resolved != original:
            path.write_text(resolved, encoding="utf-8")
            n_resolved += 1

    # myst.yml (aucun placeholder attendu, mais résolu par symétrie)
    yml = MIRROR / "myst.yml"
    original = yml.read_text(encoding="utf-8")
    resolved = resolve_text(original, values, args.strict, warnings, errors)
    if resolved != original:
        yml.write_text(resolved, encoding="utf-8")

    # 3. Rapport
    for w in warnings:
        print(f"ℹ  {w}", file=sys.stderr)
    for e in errors:
        print(f"✖ {e}", file=sys.stderr)
    print(f"✔ Miroir prêt : {MIRROR} ({n_resolved} fichiers résolus, "
          f"{len(values)} variables chargées)")
    if args.strict and errors:
        print("✖ Build strict : placeholders manquants détectés.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
