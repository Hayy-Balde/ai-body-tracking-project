# Documentation Technique - Projet de Détection de Pose Corporelle

Ce document fournit des détails techniques approfondis, des explications conceptuelles et des notes de développement pour le "Système de Détection et Visualisation de Pose Corporelle en Temps Réel". Il complète le `README.md` en fournissant plus de contexte sur les choix techniques et le fonctionnement interne.

---

## Table des matières

- [Documentation Technique - Projet de Détection de Pose Corporelle](#documentation-technique---projet-de-détection-de-pose-corporelle)
  - [Table des matières](#table-des-matières)
  - [1. Objectif Général et Philosophie du Projet](#1-objectif-général-et-philosophie-du-projet)
  - [2. Concepts Fondamentaux de Python](#2-concepts-fondamentaux-de-python)
    - [Gestion des Entrées Utilisateur](#gestion-des-entrées-utilisateur)
    - [Structures de Données Clés](#structures-de-données-clés)
    - [Principes de POO (si applicable)](#principes-de-poo-si-applicable)
  - [3. Introduction à la Vision par Ordinateur (OpenCV)](#3-introduction-à-la-vision-par-ordinateur-opencv)
    - [Flux d'Image et de Vidéo](#flux-dimage-et-de-vidéo)
    - [Format BGR vs RGB](#format-bgr-vs-rgb)
    - [Opérations de Dessin](#opérations-de-dessin)
  - [4. Détection de Pose avec MediaPipe](#4-détection-de-pose-avec-mediapipe)
    - [Vue d'ensemble de MediaPipe Pose](#vue-densemble-de-mediapipe-pose)
    - [Architecture du Modèle (simplifiée)](#architecture-du-modèle-simplifiée)
    - [Interprétation des Landmarks](#interprétation-des-landmarks)
    - [Considérations sur la Performance](#considérations-sur-la-performance)
  - [5. Méthodes de "Clonage Corporel"](#5-méthodes-de-clonage-corporel)
    - [Représentation 2D du Squelette](#représentation-2d-du-squelette)
    - [Transformation de Coordonnées](#transformation-de-coordonnées)
    - [Options de Visualisation 3D (futur)](#options-de-visualisation-3d-futur)
  - [6. Gestion de Version (Git \& GitHub)](#6-gestion-de-version-git--github)
    - [Workflow de Commit](#workflow-de-commit)
    - [Bonnes Pratiques de Branches (futur)](#bonnes-pratiques-de-branches-futur)
  - [7. Dépannage et Problèmes Communs](#7-dépannage-et-problèmes-communs)
  - [8. Ressources et Références](#8-ressources-et-références)

---

## 1. Objectif Général et Philosophie du Projet

Ce projet est conçu pour être un guide pas à pas dans l'apprentissage de la vision par ordinateur et de l'IA appliquée à la détection de pose. Chaque étape est documentée pour comprendre non seulement le "comment", mais aussi le "pourquoi". L'objectif est de construire un système robuste, mais la priorité est donnée à la compréhension des concepts sous-jacents.

## 2. Concepts Fondamentaux de Python

### Gestion des Entrées Utilisateur

Lors des exercices de base, nous avons mis l'accent sur la robustesse des entrées utilisateur. Plutôt que d'utiliser `exit(0)` en cas d'erreur d'entrée, la stratégie adoptée consiste à utiliser des boucles `while True` avec des blocs `try-except` (pour les conversions de type) ou des vérifications `isdigit()`/`strip()` combinées à `continue` pour re-demander une entrée valide.

* **Exemple (tiré de l'exercice 1 amélioré) :**
    ```python
    while True:
        price_str = input("Entrez le prix unitaire de l'article : ")
        try:
            price = float(price_str)
            if price <= 0:
                print("Le prix doit être un nombre positif.")
            else:
                break
        except ValueError:
            print("Prix invalide. Veuillez entrer un nombre.")
    ```

### Structures de Données Clés

* **Listes (`list`) :** Utilisées pour des collections ordonnées et modifiables (ex: la liste des tâches dans le gestionnaire de tâches).
    * `append()` pour ajouter un élément.
    * `pop()` pour supprimer par index.
    * `enumerate()` pour obtenir l'index et la valeur lors de l'itération.
* **Dictionnaires (`dict`) :** Utilisés pour des collections non ordonnées de paires clé-valeur (ex: l'annuaire téléphonique).
    * Accès par clé : `annuaire[nom]`.
    * Vérification d'existence : `if nom in annuaire:`.
    * Itération sur clés/valeurs : `annuaire.items()`.

### Principes de POO (si applicable)

*(Cette section pourrait être développée si vous décidez d'introduire des classes pour organiser votre code OpenCV/MediaPipe, par exemple, une classe `PoseEstimator` ou `WebcamStream`.)*

## 3. Introduction à la Vision par Ordinateur (OpenCV)

### Flux d'Image et de Vidéo

OpenCV représente les images et les frames vidéo comme des tableaux NumPy.
* **`cv2.imread()` :** Lit une image depuis un fichier. Retourne `None` si l'image n'est pas trouvée ou est corrompue.
* **`cv2.VideoCapture()` :** Gère la lecture de vidéos ou l'accès à la webcam.
    * Argument entier (ex: `0`) pour la webcam par défaut.
    * Argument chaîne (chemin de fichier) pour une vidéo.
    * Méthodes clés : `isOpened()` (vérifier si la source est prête), `read()` (lire une frame).

### Format BGR vs RGB

OpenCV charge les images par défaut dans l'ordre des canaux Bleu, Vert, Rouge (BGR). La plupart des autres bibliothèques de traitement d'image ou d'IA (comme MediaPipe) s'attendent à l'ordre Rouge, Vert, Bleu (RGB). La conversion est effectuée via `cv2.cvtColor(image, cv2.COLOR_BGR2RGB)`. Cette conversion est cruciale pour l'interopérabilité des bibliothèques.

### Opérations de Dessin

Les fonctions `cv2.line()`, `cv2.circle()`, `cv2.rectangle()`, et `cv2.putText()` sont essentielles pour la visualisation des résultats d'analyse (points clés, boîtes englobantes, annotations).
* Les couleurs sont spécifiées en BGR : `(B, G, R)`.
* Les coordonnées sont des tuples `(x, y)`.
* `thickness` (épaisseur) de `-1` remplit la forme.

## 4. Détection de Pose avec MediaPipe

### Vue d'ensemble de MediaPipe Pose

MediaPipe Pose est une solution d'apprentissage automatique qui permet de détecter 33 points clés (landmarks) sur le corps humain en temps réel. Elle est optimisée pour la performance sur divers appareils.

### Architecture du Modèle (simplifiée)

*(Décrivez ici brièvement comment MediaPipe fonctionne à haut niveau, sans entrer dans les détails mathématiques complexes. Par exemple :)*
MediaPipe Pose utilise un modèle de machine learning léger et efficace. Il se compose généralement de deux étapes :
1.  **Détection du corps :** Localise la région du corps dans l'image.
2.  **Estimation des points clés :** À l'intérieur de cette région, un modèle plus fin prédit la position des 33 points clés du corps (nez, épaules, coudes, poignets, hanches, genoux, chevilles, etc.) ainsi que leur visibilité et leur plausibilité 3D (profondeur relative).

### Interprétation des Landmarks

Chaque landmark retourné par MediaPipe a des propriétés :
* `x` et `y` : Coordonnées normalisées (entre 0.0 et 1.0) par rapport à la largeur et la hauteur de l'image.
* `z` : Coordonnée de profondeur relative au "centre" de la personne. (0.0 pour le centre du torse, valeurs positives plus éloignées de la caméra, valeurs négatives plus proches).
* `visibility` : Score de confiance (entre 0.0 et 1.0) indiquant la probabilité que le landmark soit visible.

### Considérations sur la Performance

*(Discutez ici des facteurs qui peuvent affecter les performances, comme la résolution de la caméra, la puissance de calcul, etc.)*

## 5. Méthodes de "Clonage Corporel"

### Représentation 2D du Squelette

L'idée du "clone corporel" consiste à prendre les coordonnées des landmarks et à les projeter sur une surface de dessin propre (une image noire ou un fond unifié). Cela permet de visualiser les mouvements du squelette sans le bruit de l'arrière-plan de la caméra.

### Transformation de Coordonnées

Les coordonnées des landmarks MediaPipe sont normalisées (0-1). Pour les dessiner sur une image de pixels spécifique, elles doivent être mises à l'échelle : `pixel_x = landmark.x * image_width`, `pixel_y = landmark.y * image_height`.

### Options de Visualisation 3D (futur)

*(Si vous vous aventurez dans la 3D, détaillez ici les bibliothèques envisagées, les défis de projection 3D, etc.)*

## 6. Gestion de Version (Git & GitHub)

### Workflow de Commit

Pour ce projet, un workflow de commit discipliné est encouragé :
1.  **Modifier le code.**
2.  **Vérifier les changements :** `git status`.
3.  **Ajouter les fichiers à l'index :** `git add .` (ou des fichiers spécifiques).
4.  **Commiter avec un message clair :** `git commit -m "Description concise des changements"`.
5.  **Pousser vers GitHub :** `git push origin main`.

### Bonnes Pratiques de Branches (futur)

*(Si vous commencez à utiliser des branches pour des fonctionnalités spécifiques, expliquez ici votre stratégie : ex: `feature/nom-fonctionnalite`, `bugfix/description-bug`, puis `git merge` ou `git rebase`.)*

## 7. Dépannage et Problèmes Communs

* **`ModuleNotFoundError: No module named 'cv2'` :** Indique qu'OpenCV n'est pas installé ou que votre environnement Python n'est pas le bon. Solution : `pip install opencv-python`.
* **`cv2.VideoCapture(0)` ne fonctionne pas :** La webcam n'est pas accessible.
    * Vérifiez que la webcam n'est pas utilisée par une autre application.
    * Vérifiez les permissions de votre système d'exploitation pour l'accès à la caméra.
    * Essayez différents indices de caméra (1, 2, etc.) si vous avez plusieurs caméras.
* **Performances lentes :**
    * Assurez-vous que votre modèle d'IA s'exécute sur le GPU si disponible (plus avancé).
    * Réduisez la résolution de la webcam pour un traitement plus rapide (ex: `cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)`).

## 8. Ressources et Références

* [Documentation Officielle OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
* [Documentation Officielle MediaPipe Solutions (Python)](https://google.github.io/mediapipe/solutions/pose.html)
* [Tutoriels YouTube sur OpenCV et MediaPipe](https://www.youtube.com/results?search_query=python+opencv+mediapipe+tutorial)
* [Stack Overflow](https://stackoverflow.com/) pour les questions de programmation.
* [Git Documentation](https://git-scm.com/doc)
* [GitHub Guides](https://guides.github.com/)

---