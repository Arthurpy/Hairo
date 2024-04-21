# HAIRO

## Introduction

HAIRO est une application web développée pour aider les étudiants en première année de médecine à optimiser leur apprentissage. Elle offre des fonctionnalités de révision, d'organisation et d'entraînement sur des QCM, intégrant une IA pour personnaliser l'expérience d'apprentissage.

## Table des Matières

- [Installation](#installation)
- [Usage](#usage)
- [Fonctionnalités](#fonctionnalités)
- [Dépendances](#dépendances)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Exemples](#exemples)
- [Dépannage](#dépannage)
- [Contributeurs](#contributeurs)
- [Licence](#licence)

## Installation

### Prérequis

Vous devez avoir installé sur votre machine :
- Node.js
- npm ou yarn
- Python 3
- pip
- virtualenv (optionnel mais recommandé)

### Installation Locale

1. **Cloner le dépôt**

    ```bash
    git clone https://github.com/votreusername/HAIRO.git
    cd HAIRO
    ```

2. **Configurer et lancer le backend**

    Naviguez dans le dossier du backend et créez un environnement virtuel :

    ```bash
    cd back/Hairo_Back
    python -m venv env
    source env/bin/activate  # Sur Windows utilisez `env\Scripts\activate`
    ```

    Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

    Lancez le serveur Django :

    ```bash
    python manage.py runserver
    ```

3. **Configurer et lancer le frontend**

    Ouvrez un nouveau terminal, naviguez vers le dossier racine du projet, puis :

    ```bash
    npm install  # ou `yarn install` si vous utilisez yarn
    npm run serve  # ou `yarn serve`
    ```

    Le front-end sera accessible à `http://localhost:8080/`.

## Usage

Après avoir lancé les serveurs backend et frontend, accédez à `http://localhost:8080/` sur votre navigateur pour utiliser l'application.

## Fonctionnalités

- Révision interactive basée sur des QCM.
- Outils d'organisation des sessions de révision.
- IA d'assistance pour des suggestions personnalisées.

## Dépendances

- Vue.js
- Django
- Autres bibliothèques listées dans `requirements.txt` pour le backend et `package.json` pour le frontend.

## Configuration

La configuration par défaut devrait suffire pour un lancement local. Pour le déploiement ou des configurations avancées, veuillez consulter la documentation technique supplémentaire.

## Documentation

La documentation complète est disponible dans les dossiers `/docs` pour plus de détails sur l'architecture et l'utilisation.

## Exemples

Pour voir comment utiliser les différentes fonctionnalités, veuillez consulter les scénarios d'utilisation dans `/examples`.

## Dépannage

Pour tout problème lors de l'installation ou de l'exécution, veuillez vérifier les logs et les erreurs courantes dans la section `/troubleshooting`.

## Contributeurs

Listez ici tous ceux qui ont contribué au projet.

## Licence

Spécifiez ici le type de licence sous laquelle le projet est distribué, par exemple MIT, GPL, etc.
