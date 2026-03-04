# How-To: Branch erstellen und mergen

## Feature-Branch erstellen

```bash
git checkout main
git pull
git checkout -b feature/<ticket>_<kurzbeschreibung>
```

## Änderungen committen

```bash
git add .
git commit -m "feat: <kurze beschreibung>"
```

## Branch mergen

```bash
git checkout main
git pull
git merge --no-ff feature/<ticket>_<kurzbeschreibung>
```
