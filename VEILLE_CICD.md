Voici ton **livrable en Markdown**, clair, structuré, prêt à déposer dans ton repo.

---

# Mission 1 – Comprendre CI/CD

## 1. Qu'est-ce que la CI (Continuous Integration) ?

La pratique de l'**intégration continue (CI)** consiste à intégrer automatiquement et régulièrement les modifications de code dans un référentiel de code source partagé.

### Objectifs :

* Détecter les erreurs le plus tôt possible
* Réduire les conflits de merge
* Garantir que la base de code reste fonctionnelle
---

## 2. Quels problèmes résout-elle ?

* **Conflits d’intégration tardive** : éviter la situation où les développeurs intègrent des gros blocs de code après plusieurs jours/semaines.
* **Régressions non détectées** : grâce aux tests automatisés lancés à chaque push.
* **Perte de temps en débogage** : détection précoce → correction plus rapide et moins coûteuse.
* **Manque de visibilité** : les pipelines CI offrent une vision claire de l’état du projet (succès/échecs).

---

## 3. Quels sont les principes clés ?

* **Intégrations fréquentes**
* **Automatisation** (build, tests, linting, contrôle qualité)
* **Feedback rapide** (l'équipe est informée immédiatement en cas d’erreur)
* **Source code centralisé** (un dépôt unique : GitHub, GitLab, Bitbucket)
* **Tests systématiques** (un code non testé n'est jamais intégré)

---

## 4. Trois exemples d’outils de CI

1. **GitHub Actions**
2. **GitLab CI/CD**
3. **Jenkins**

Autres possibles : CircleCI, TravisCI, Azure Pipelines.

---

## 5. Qu’est-ce que le CD (Continuous Delivery / Continuous Deployment) ?

Le **CD** est l’étape qui suit la CI.
Elle consiste à automatiser la livraison ou le déploiement du logiciel.

### Deux niveaux existent :

### a) Continuous Delivery

Le pipeline prépare automatiquement l’application pour la mise en production (build + tests + packaging + staging).
**Le déploiement en production est manuel, mais prêt en un clic.**

### b) Continuous Deployment

Le pipeline va **jusqu'à déployer automatiquement en production** dès que tous les contrôles sont passés.

---

## 6. Différence entre Continuous Delivery et Continuous Deployment

| Aspect                    | Continuous Delivery           | Continuous Deployment         |
| ------------------------- | ----------------------------- | ----------------------------- |
| Déploiement en production | Manuel                        | Automatique                   |
| Objectif                  | Être toujours prêt à déployer | Déployer dès que c’est valide |
| Niveau d’automatisation   | Élevé mais pas total          | Total                         |

---

## 7. Risques et bénéfices du CD

### Bénéfices :

* Déploiements plus rapides
* Moins d’erreurs humaines
* Feedback plus rapide côté utilisateurs
* Amélioration continue du produit
* Rythme de livraison stable et prévisible

### Risques :

* En Continuous Deployment :

  * risque de déployer automatiquement une fonctionnalité mal conçue
  * nécessité d’avoir des tests extrêmement robustes
* Environnement complexe à gérer (monitoring, rollback, logs, alerting)

---

## 8. Pourquoi CI/CD est important ?

### a) Impact sur la qualité du code

* Tests automatisés → meilleure stabilité
* Détection rapide des bugs → moins de régressions
* Code plus propre grâce au linting et formatage

### b) Impact sur la vitesse de développement

* Build + tests + déploiement automatisés
* Gain de temps : les développeurs se concentrent sur le code, pas sur l’opérationnel
* Livraison plus fréquente → time-to-market plus court

### c) Impact sur la collaboration en équipe

* Réduit les conflits de merge
* Pipeline transparent pour toute l’équipe
* Facilite le pair programming et les revues de code
* Encourage les bonnes pratiques partagées

---

## Ressources utilisées

* Red Hat – *Qu’est-ce que la CI/CD ?*
* YouTube – *GitHub Actions Tutorial (30min)*


---

Voici ton **livrable Markdown complet** pour la Mission 2 — prêt à être déposé dans ton repo.

---

# Mission 2 – Maîtriser **uv**

## 1. Qu’est-ce que **uv** ?

**uv** est un outil moderne développé par **Astral** (l’équipe derrière `ruff`) qui remplace plusieurs outils Python classiques :

* gestion d’environnement virtuels
* gestion des dépendances
* installation ultra rapide
* build backend
* exécution de commandes Python

Il est conçu pour être **extrêmement rapide**, grâce à une implémentation en Rust, avec un fonctionnement très proche de Bun pour JavaScript.

**uv = pip + virtualenv + pip-tools + poetry (partiellement) + build backend**

---

## 2. En quoi est-ce différent de pip / poetry / pipenv ?

| Fonctionnalité          | pip     | pipenv  | poetry  | uv                                    |
| ----------------------- | ------- | ------- | ------- | ------------------------------------- |
| Gestion des dépendances | Basique | Oui     | Oui     | Oui (très rapide, résolution moderne) |
| Lockfile                | Non     | Oui     | Oui     | Oui (`uv.lock`)                       |
| Virtualenv              | Externe | Oui     | Oui     | Oui                                   |
| Build backend           | Non     | Non     | Oui     | Oui                                   |
| Vitesse                 | Lente   | Moyenne | Moyenne | **Extrêmement rapide (Rust)**         |
| Support pyproject.toml  | Limité  | Oui     | Oui     | Oui                                   |

### Ce qui distingue **uv**

* Plus rapide que **pip** (jusqu’à 100× selon la doc)
* Plus simple et plus léger que **poetry**
* Plus fiable que **pipenv**
* Utilise un **lockfile moderne** (déploiement plus fiable)
* Compatible **pyproject.toml**, donc standard

---

## 3. Quels sont les avantages ?

* **Installation ultra rapide**

* **Gestion complète des environnements** (création, activation, isolation)

* **Support natif de pyproject.toml**

* **Résolution des dépendances optimisée**

* **Build backend intégré** (comme Poetry)

* **Intégration GitHub Actions prête à l’emploi**

* **Commandes cohérentes et simples** :

  * `uv add`
  * `uv remove`
  * `uv lock`
  * `uv run`

* Compatible avec tous les projets Python existants sans migration lourde.

---

## 4. Comment uv fonctionne avec **pyproject.toml** ?

`pyproject.toml` devient le fichier unique de configuration : dépendances, build backend, métadonnées.

### a) Structure du fichier

Exemple simplifié :

```toml
[project]
name = "my_app"
version = "0.1.0"
dependencies = [
    "requests",
    "pydantic>=2.0"
]

[project.optional-dependencies]
dev = [
    "pytest",
    "ruff"
]

[build-system]
requires = ["uv-build>=0.1"]
build-backend = "uv_build.backend"
```

---

### b) Gestion des dépendances

uv utilise deux fichiers :

* **pyproject.toml** → déclaratif
* **uv.lock** → généré automatiquement, contient les versions exactes

Commandes associées :

```
uv add requests
uv add pytest --dev
uv remove requests
uv lock
```

Les dépendances sont classées par sections :

* `dependencies`
* `optional-dependencies.dev`
* `optional-dependencies.docs`
* `optional-dependencies.test`, etc.

---

### c) Build backend

uv fournit un backend de build compatible PEP 517 :

```toml
[build-system]
requires = ["uv-build"]
build-backend = "uv_build.backend"
```

Il permet :

* création de wheels (`uv build`)
* gestion des métadonnées
* compatibilité packaging

---

## 5. Comment utiliser uv dans **GitHub Actions** ?

uv a une intégration officielle.
Elle permet :

* installation rapide de Python
* installation/chargement du cache
* exécution de tests ou commandes

---

### a) Installation

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v1
```

Avec Python intégré :

```yaml
- name: Set up Python + uv
  uses: astral-sh/setup-python@v1
  with:
    python-version: "3.12"
```

---

### b) Cache des dépendances

uv a un cache interne, activable automatiquement :

```yaml
- name: Cache uv dependencies
  uses: actions/cache@v3
  with:
    path: ~/.cache/uv
    key: ${{ runner.os }}-uv-${{ hashFiles('uv.lock') }}
```

---

### c) Exécution de commandes

Installer les dépendances :

```yaml
- name: Install dependencies
  run: uv sync
```

Lancer une commande :

```yaml
- name: Run tests
  run: uv run pytest
```

Lancer ton app :

```yaml
- name: Run app
  run: uv run python main.py
```

Build de l’application :

```yaml
- name: Build the project
  run: uv build
```

---

## Exemple complet de workflow GitHub Actions

```yaml
name: CI

on:
  push:
    branches: ["main"]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v1

      - name: Cache uv dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/uv
          key: ${{ runner.os }}-uv-${{ hashFiles('uv.lock') }}

      - name: Install dependencies
        run: uv sync

      - name: Run tests
        run: uv run pytest
```

---

## Ressources utilisées

* uv documentation
* uv GitHub Integration
* uv Build Backend
* uv Tutorial (vidéo officielle)

---
Voici ton **livrable Markdown complet** pour la Mission 3 – prêt à déposer dans ton repo.

---

# Mission 3 – Comprendre Semantic Release

## 1. Qu’est-ce que le versionnage sémantique (SemVer) ?

Le **versionnage sémantique** (Semantic Versioning ou **SemVer**) est une méthode standardisée pour numéroter les versions d’un logiciel.
Il suit le format :

```
MAJOR.MINOR.PATCH
```

### Signification des niveaux :

* **MAJOR** : changements incompatibles (breaking changes)
* **MINOR** : nouvelles fonctionnalités rétro-compatibles
* **PATCH** : corrections de bugs, modifications mineures sans impact fonctionnel

---

### Quand bumper chaque niveau ?

| Niveau    | Quand l’incrémenter ?                                                            | Exemples                               |
| --------- | -------------------------------------------------------------------------------- | -------------------------------------- |
| **MAJOR** | Changement non rétrocompatible, suppression d’une fonctionnalité, refactor lourd | API modifiée, format de données changé |
| **MINOR** | Ajout d’une nouvelle fonctionnalité compatible                                   | Nouveau endpoint, nouvelle feature     |
| **PATCH** | Correction d’un bug, amélioration mineure                                        | Fix d’erreur, correction de typo       |

---

## 2. Qu’est-ce que **Conventional Commits** ?

**Conventional Commits** est une convention standardisée pour écrire des messages de commits structurés afin de permettre l’automatisation du versionnage, des changelogs et des releases.

Format général :

```
type(scope): message court
```

Exemples :

```
feat(api): add user endpoint
fix(auth): prevent token expiration bug
docs: update README
```

---

### Types de commits les plus courants

| Type         | Signification                               |
| ------------ | ------------------------------------------- |
| **feat**     | Nouvelle fonctionnalité                     |
| **fix**      | Correction d’un bug                         |
| **docs**     | Documentation                               |
| **style**    | Formatage, linting, sans impact sur le code |
| **refactor** | Refactoring sans changement fonctionnel     |
| **perf**     | Amélioration des performances               |
| **test**     | Ajout / modif de tests                      |
| **chore**    | Maintenance, tâches non liées aux features  |

---

### Impact sur le versionnage SemVer

| Type de commit                                     | Effet                       |
| -------------------------------------------------- | --------------------------- |
| **feat**                                           | Bump *MINOR*                |
| **fix**                                            | Bump *PATCH*                |
| **BREAKING CHANGE** (footer dans le commit ou `!`) | Bump *MAJOR*                |
| Tous les autres types                              | Pas d’impact sur la version |

Exemple d’un commit majeur :

```
feat(core)!: change auth flow
```

ou :

```
refactor: rework data model

BREAKING CHANGE: new schema not compatible with previous versions
```

---

## 3. Comment fonctionne **python-semantic-release** ?

`python-semantic-release` est un outil qui automatise :

* Le versionnage SemVer
* La génération du `CHANGELOG.md`
* La création de releases GitHub
* Le bump de version dans le projet
* Le packaging et la publication (optionnel)

---

## 4. Configuration dans **pyproject.toml**

Exemple minimal :

```toml
[tool.semantic_release]
version_variable = "package/__init__.py:__version__"
upload_to_pypi = false
upload_to_release = true
changelog_file = "CHANGELOG.md"
commit_parser = "conventional"
```

### Points importants :

* `version_variable` : indique où est stockée la version
* `commit_parser = "conventional"` : active Conventional Commits
* `upload_to_release = true` : crée des releases GitHub
* `changelog_file` : fichier généré automatiquement

---

## 5. Génération du CHANGELOG

Lors d’un release automatique :

1. Analyse de tous les commits depuis la dernière version
2. Classification par type (`feat`, `fix`, `docs`, etc.)
3. Création ou mise à jour d’un fichier `CHANGELOG.md`

Format classique :

```
## v1.4.0 (2025-01-10)

### Features
- add new API endpoint

### Fixes
- fix auth timeout error
```

---

## 6. Création des releases GitHub

`python-semantic-release` peut automatiquement créer une release GitHub lorsque :

* Le workflow GitHub Actions s’exécute
* Les commits sont conformes aux règles Conventional Commits
* Une nouvelle version est détectée

Exemple de configuration dans GitHub Actions :

```yaml
- name: Python Semantic Release
  uses: python-semantic-release/python-semantic-release@v9
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
```

Le workflow va :

* Bumper la version (MAJOR/MINOR/PATCH)
* Commiter le bump (`ci: release version x.x.x`)
* Générer le changelog
* Créer une release GitHub

---

## Ressources utilisées

* Documentation Conventional Commits
* Conventional Commits Gist
* Python Semantic Release

---
Voici la **section complète à ajouter dans ton fichier `VEILLE_CICD.md`** pour la Mission 5.
Tu peux copier-coller telle quelle.

---

# Mission 5 – MkDocs & GitHub Pages

## 1. Comment MkDocs génère de la documentation ?

**MkDocs** est un générateur statique de documentation écrit en Python.
Il transforme un dossier contenant des fichiers **Markdown** en un site web statique HTML/CSS/JS.

### Fonctionnement général

1. Tu écris ta documentation en `.md` dans un dossier (souvent `docs/`).
2. Tu configures le site via un fichier `mkdocs.yml`.
3. MkDocs génère le site via :

   ```
   mkdocs build
   ```
4. Un dossier `site/` est produit → prêt à être déployé.

### Caractéristiques importantes

* Organisation de la navigation via `mkdocs.yml`
* Intégration Markdown simple
* Live server pour prévisualiser :

  ```
  mkdocs serve
  ```
* Compatible avec des thèmes (y compris Material)
* Extensible via des plugins (mkdocstrings, search, i18n, etc.)

---

## 2. Comment déployer sur GitHub Pages ?

MkDocs peut déployer automatiquement sur GitHub Pages.

### Deux méthodes :

#### 1) **Commande intégrée**

```
mkdocs gh-deploy
```

Cette commande :

* construit le site
* pousse automatiquement le HTML dans la branche `gh-pages`
* configure GitHub Pages

#### 2) **Via GitHub Actions** (recommandé)

Exemple workflow officiel :

```yaml
name: Deploy MkDocs

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install mkdocs-material mkdocstrings

      - name: Build and deploy
        run: mkdocs gh-deploy --force
```

### Configuration GitHub Pages

Dans **Settings → Pages** :

* Définir la source : `gh-pages`
* Optionnel : domaine custom

---

## 3. Qu’est-ce que mkdocstrings ?

**mkdocstrings** est un plugin MkDocs permettant de générer automatiquement la documentation API à partir du code source, un peu comme Sphinx mais plus simple.

### Capabilités

* Analyse automatique du code Python (ou autres langages)
* Génère une documentation lisible depuis les docstrings
* S’intègre parfaitement au thème Material
* Mise à jour automatique à chaque commit

### Exemple d’utilisation dans un fichier `.md`

```markdown
# API Reference

::: package.module.function_name
```

### Configuration dans `mkdocs.yml`

```yaml
plugins:
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: google
            show_source: false
```

Ainsi, si tes fonctions/classes contiennent des docstrings, elles seront directement intégrées dans le site.

---

## 4. Résumé

| Élément          | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| **MkDocs**       | Génère un site statique à partir de Markdown                 |
| **Déploiement**  | GitHub Pages via `gh-deploy` ou GitHub Actions               |
| **mkdocstrings** | Génère la documentation API automatiquement à partir du code |

---
