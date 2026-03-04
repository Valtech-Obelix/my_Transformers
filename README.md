# my_Transformer

Python-Projekt mit Basis-Setup (Packaging, Linting, Tests, CI) analog zu `my_OnCall_Manager`.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .[dev]
pytest
```

## Struktur

- `src/my_transformer/` Anwendungscode
- `tests/` Test-Suite
- `docs/how_to/` Team-How-Tos
- `docs/how_to/` Team-How-Tos (PR-Schutz derzeit nicht aktiviert — Einzelentwickler)
- `scripts/` Hilfsskripte

## CI

Bei Push/PR laeuft GitHub Actions mit:
- `ruff check .`
- `pytest`

Workflow-Datei: `.github/workflows/ci.yml`

## Branch-Schutz

Der Pull-Request-Schutz ist aktuell nicht aktiviert, da derzeit nur ein Entwickler am Projekt arbeitet. Details und Anleitung: [docs/how_to/How-To_GitHub_Branch_Protection.md](docs/how_to/How-To_GitHub_Branch_Protection.md).

## Branching Workflow

Vor Beginn der Umsetzung eines Use Case immer einen neuen Branch anlegen. Nach Abschluss des Use Case den Branch in `main` mergen und anschließend einen Tag erstellen.

Empfohlenes Vorgehen:

- **Branch erstellen:** `git checkout -b feature/<kurze-beschreibung>`
- **Arbeiten & committen:** lokale Commits wie gewohnt erstellen
- **Merge in main:** Pull Request öffnen und nach Review in `main` mergen
- **Taggen:** nach Merge auf `main` taggen, z.B. `git tag -a vX.Y.Z -m "Release vX.Y.Z"` und `git push --tags`

Hinweis: Da das Projekt aktuell nur von einer Person gepflegt wird, ist der PR-Schutz deaktiviert — trotzdem hilft diese Regel, Änderungen sauber zu organisieren und Releases nachvollziehbar zu machen.
