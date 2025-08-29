# Pavement Planner

[![CI](https://github.com/example/pavement-planner/actions/workflows/ci.yml/badge.svg)](https://github.com/example/pavement-planner/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Eina de planificació de conservació de ferms amb Python i PySide6.

## Característiques
- Importació de dades d'auscultació i trànsit
- Projecció d'observacions sobre l'eix de referència
- Càlcul d'índexs i segmentació dinàmica
- Priorització multicriteri i optimització amb pressupost
- GUI d'escriptori amb PySide6

## Requisits
- Python 3.11+
- Dependències a `requirements.txt`

## Instal·lació
```bash
git clone <repo-url>
cd pavement-planner
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Execució
```bash
python -m src.app
```

## Dades d'exemple
Al directori `sample_data/` hi ha fitxers CSV bàsics per provar el flux.

## Tests
```bash
pytest -q
```

## Lint i format
```bash
black .
ruff check .
mypy src/core
```

## Empaquetat
- Windows: `scripts/package_win.bat`
- Linux: `scripts/package_linux.sh`

## Configuració
Paràmetres per defecte a `src/data/config_default.yaml`.

## Contribució
Vegeu `CONTRIBUTING.md` i `CODE_OF_CONDUCT.md`.

## Llicència
MIT
