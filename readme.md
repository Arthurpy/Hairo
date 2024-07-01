# HAIRO

## Introduction

HAIRO est une application web développée pour aider les étudiants en première année de médecine à optimiser leur apprentissage. Elle offre des fonctionnalités de révision, d'organisation et d'entraînement sur des QCM, intégrant une IA pour personnaliser l'expérience d'apprentissage.

## Table des Matières

- [Installation](#installation)
- [Usage](#usage)
- [Fonctionnalités](#fonctionnalités)
- [Dépendances](#dépendances)
- [Configuration](#configuration)
- [Contributeurs](#contributeurs)

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
    python3 -m venv env
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
    npm install
    npm run dev
    ```

    Le front-end sera accessible à `http://localhost:5173/`.

## Usage

Après avoir lancé les serveurs backend et frontend, accédez à `http://localhost:5173/` sur votre navigateur pour utiliser l'application.

## Fonctionnalités

- Révision interactive basée sur des QCM.
- Outils d'organisation des sessions de révision.
- IA d'assistance pour des suggestions personnalisées.

## Dépendances

- Vue.js
- Django
- Autres bibliothèques listées dans `requirements.txt` pour le backend et `package.json` pour le frontend.

## Configuration

La configuration par défaut devrait suffire pour un lancement local.

## Contributeurs
Arthur Py
Ayman Tebini
Pierre Bouillard

