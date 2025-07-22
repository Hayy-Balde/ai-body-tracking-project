# Système de Détection et Visualisation de Pose Corporelle en Temps Réel

![Image du projet en action](assets/Capture_d_écran_2025-07-22_à_08.09.56.png)
*(Remplacez ceci par une capture d'écran de votre projet final ou une image représentative dès que possible. Pour l'instant, j'ai mis l'image que vous avez fournie en exemple.)*

## Table des matières

- [Système de Détection et Visualisation de Pose Corporelle en Temps Réel](#système-de-détection-et-visualisation-de-pose-corporelle-en-temps-réel)
  - [Table des matières](#table-des-matières)
  - [1. À propos du Projet](#1-à-propos-du-projet)
  - [2. Fonctionnalités Actuelles](#2-fonctionnalités-actuelles)
  - [3. Technologies Utilisées](#3-technologies-utilisées)
  - [4. Prérequis](#4-prérequis)
  - [5. Installation](#5-installation)
  - [6. Utilisation](#6-utilisation)
  - [7. Structure du Projet](#7-structure-du-projet)
  - [8. Prochaines Étapes / Améliorations Futures](#8-prochaines-étapes--améliorations-futures)
  - [9. Contribution](#9-contribution)
  - [10. Licence](#10-licence)
  - [11. Contact](#11-contact)

---

## 1. À propos du Projet

Ce projet vise à développer un système de détection et de visualisation de la pose corporelle humaine en temps réel. En utilisant la vision par ordinateur et des techniques d'intelligence artificielle, l'objectif est de capturer les mouvements d'une personne via une webcam et de les représenter visuellement, potentiellement sous forme d'un "clone" ou d'un squelette animé.

Ce projet est conçu comme un parcours d'apprentissage personnel pour maîtriser les concepts fondamentaux de la vision par ordinateur et de l'apprentissage automatique avec Python.

## 2. Fonctionnalités Actuelles

*(Mettez à jour cette section au fur et à mesure que vous progressez. Voici ce que vous avez déjà fait ou ce que vous êtes en train de faire)*

* **Phase 1 - Fondamentaux Python :**
    * Compréhension et application des concepts de base de Python (variables, boucles, conditions, fonctions, listes, dictionnaires).
    * Réalisation réussie de 5 exercices fondamentaux en Python.
    * Mise en place de la gestion de version avec Git et GitHub.
* **Phase 2 - Introduction à OpenCV (en cours) :**
    * Installation et vérification d'OpenCV.
    * Chargement et affichage d'images.
    * Lecture et affichage de flux vidéo depuis un fichier.
    * Accès et affichage du flux vidéo en direct depuis une webcam.
    * Maîtrise des conversions de couleur (BGR vers RGB).
    * Capacité à dessiner des formes (lignes, cercles, rectangles) et du texte sur des images.

*(Exemples de fonctionnalités futures à ajouter ici une fois réalisées :)*
* Détection de pose corporelle en temps réel à l'aide de MediaPipe.
* Visualisation du squelette de pose détecté sur le flux vidéo.
* Création d'une représentation stylisée du squelette (le "clone") dans une fenêtre séparée.
* Lissage des mouvements pour une visualisation plus fluide.

## 3. Technologies Utilisées

* **Python 3.x**
* **OpenCV (`opencv-python`)** : Bibliothèque open source pour la vision par ordinateur.
* **MediaPipe (`mediapipe`)** : Framework de Google pour la construction de pipelines de ML pour le traitement des données multimodales (sera intégré dans les prochaines phases).
* **Numpy** : (Utilisé implicitement par OpenCV pour la manipulation d'images).
* **Git** : Système de contrôle de version.
* **GitHub** : Plateforme d'hébergement de dépôts Git.

## 4. Prérequis

Avant de pouvoir exécuter ce projet, assurez-vous d'avoir les éléments suivants installés :

* [Python 3.x](https://www.python.org/downloads/) (recommandé Python 3.8+)
* `pip` (généralement inclus avec Python)

## 5. Installation

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/VotreNomUtilisateur/NomDeVotreDepot.git](https://github.com/VotreNomUtilisateur/NomDeVotreDepot.git)
    cd NomDeVotreDepot
    ```
    *(N'oubliez pas de remplacer `VotreNomUtilisateur` et `NomDeVotreDepot` par les vôtres !)*

2.  **Installer les dépendances :**
    ```bash
    pip install opencv-python mediapipe numpy
    ```
    *(Vous pouvez ajouter un `requirements.txt` plus tard pour automatiser cela, mais pour l'instant, listez-les ici.)*

## 6. Utilisation

*(Cette section sera mise à jour au fur et à mesure que le projet avance. Pour l'instant, vous pouvez mentionner comment exécuter les scripts des exercices.)*

Pour exécuter les scripts d'exemple de la phase 2.1 :

* **Pour l'affichage d'image (`image_viewer.py`) :**
    ```bash
    python image_viewer.py
    ```
    *(Assurez-vous d'avoir une image nommée `ma_photo.jpg` dans le même dossier ou d'ajuster le chemin dans le script.)*

* **Pour la lecture vidéo (`video_player.py`) :**
    ```bash
    python video_player.py
    ```
    *(Assurez-vous d'avoir une vidéo nommée `ma_video.mp4` dans le même dossier ou d'ajuster le chemin dans le script.)*

* **Pour le flux webcam (`webcam_stream.py`) et le dessin (`webcam_draw.py`) :**
    ```bash
    python webcam_stream.py
    # ou
    python webcam_draw.py
    ```
    *(Assurez-vous que votre webcam est connectée et fonctionnelle.)*

## 7. Structure du Projet

├── README.md
├── requirements.txt         # Fichier des dépendances (à créer plus tard)
├── exercices_python_bases/  # Dossier pour les exercices de la Phase 1.1
│   ├── exercice1.py
│   ├── exercice2.py
│   ├── exercice3.py
│   ├── exercice4.py
│   └── exercice5.py
├── phase2_opencv_mediapipe/ # Dossier pour la Phase 2
│   ├── image_viewer.py
│   ├── video_player.py
│   ├── webcam_stream.py
│   └── webcam_draw.py
├── assets/                  # Dossier pour les images du README, captures d'écran, etc.
│   └── Capture_d_écran_2025-07-22_à_08.09.56.png
└── # ... autres fichiers et dossiers à venir


## 8. Prochaines Étapes / Améliorations Futures

*(Liste des fonctionnalités et améliorations que vous prévoyez d'implémenter, tirées de votre workflow.)*

* Intégrer la détection de pose MediaPipe pour un suivi corporel précis.
* Développer une interface utilisateur simple pour contrôler le flux vidéo et les options de visualisation.
* Implémenter le "clonage" corporel en temps réel sur un arrière-plan neutre.
* Explorer la visualisation 3D des points clés du corps.
* Optimiser les performances pour un traitement en temps réel fluide.

## 9. Contribution

Ce projet est principalement un effort d'apprentissage personnel. Cependant, si vous avez des suggestions ou des améliorations, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## 10. Licence

Ce projet est sous licence [MIT License](LICENSE).

## 11. Contact

Mamadou Oury Baldé - [Votre Profil GitHub](https://github.com/Hayy-Baldé) - [Votre E-mail (optionnel)](mailto:mamadou62351@gmail.com)

---