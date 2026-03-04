# How-To: GitHub Branch Protection fuer `main`

## Ziel
Schutz von `main`, damit nur gepruefte Aenderungen gemerged werden.

## Einstellungen in GitHub
Pfad: `Repository -> Settings -> Branches -> Add branch protection rule`

Empfohlene Rule fuer `main`:
- Branch name pattern: `main`
- Require a pull request before merging: aktiviert
- Require approvals: `1`
- Dismiss stale pull request approvals when new commits are pushed: aktiviert
- Require status checks to pass before merging: aktiviert
- Required status checks: `test` (CI-Job)
- Require conversation resolution before merging: aktiviert
- Do not allow bypassing the above settings: aktiviert (falls Team-Policy)

## Hinweis
Nach Aktivierung kann niemand mehr direkt nach `main` pushen (ausser explizit erlaubte Rollen).
