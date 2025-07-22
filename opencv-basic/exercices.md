**Veuillez créer un nouveau fichier Python pour chaque exercice (ou au moins regrouper ceux qui sont logiques ensemble) et nommez-les de manière significative.**

-----

### **Exercices Pratiques pour la Section 2.1 : Introduction à OpenCV**

#### **Exercice 2.1.1 : Vérification de l'Installation OpenCV**

  * **Objectif :** Confirmer que `opencv-python` est correctement installé.
  * **Tâche :**
    1.  Ouvrez votre terminal/invite de commande.
    2.  Exécutez la commande d'installation : `pip install opencv-python`.
    3.  Une fois l'installation terminée, ouvrez un interpréteur Python (tapez `python` ou `python3`).
    4.  Dans l'interpréteur, importez OpenCV et affichez sa version :
        ```python
        import cv2
        print(cv2.__version__)
        ```
    5.  Assurez-vous qu'un numéro de version s'affiche sans erreur.

#### **Exercice 2.1.2 : Affichage d'une Image**

  * **Objectif :** Charger et afficher une image.
  * **Tâche :**
    1.  Créez un nouveau fichier Python nommé `image_viewer.py`.
    2.  Placez une image (ex: `ma_photo.jpg`) dans le même dossier que ce script.
    3.  Écrivez le code Python pour :
          * Charger `ma_photo.jpg` (ou le nom de votre image).
          * Afficher l'image dans une fenêtre nommée "Ma Photo".
          * Attendre une touche avant de fermer la fenêtre.
          * Détruire toutes les fenêtres OpenCV.
  * **Vérification :** Exécutez le script, une fenêtre avec votre image devrait apparaître et se fermer après avoir appuyé sur une touche.

#### **Exercice 2.1.3 : Lecture et Affichage d'une Vidéo**

  * **Objectif :** Lire et afficher les frames d'un fichier vidéo.
  * **Tâche :**
    1.  Créez un nouveau fichier Python nommé `video_player.py`.
    2.  Placez un fichier vidéo (ex: `ma_video.mp4`) dans le même dossier que ce script.
    3.  Écrivez le code Python pour :
          * Ouvrir le fichier vidéo (`ma_video.mp4`).
          * Boucler pour lire chaque frame.
          * Afficher chaque frame dans une fenêtre nommée "Ma Vidéo".
          * Ajouter une condition pour quitter la lecture et fermer la fenêtre si la touche 'q' est pressée.
          * Gérer la fin de la vidéo.
          * Libérer la ressource vidéo et détruire toutes les fenêtres à la fin.
  * **Vérification :** Exécutez le script, votre vidéo devrait se lancer. Appuyez sur 'q' pour la fermer.

#### **Exercice 2.1.4 : Flux Vidéo de la Webcam**

  * **Objectif :** Accéder à la webcam et afficher son flux en temps réel.
  * **Tâche :**
    1.  Créez un nouveau fichier Python nommé `webcam_stream.py`.
    2.  Écrivez le code Python pour :
          * Accéder à la webcam par défaut.
          * Vérifier si la webcam a été ouverte avec succès.
          * Boucler indéfiniment pour lire les frames de la webcam.
          * Afficher chaque frame dans une fenêtre nommée "Mon Flux Webcam".
          * Ajouter une condition pour quitter le flux si la touche 'q' est pressée.
          * Libérer la ressource webcam et détruire toutes les fenêtres.
  * **Vérification :** Exécutez le script, vous devriez voir votre propre image en direct. Appuyez sur 'q' pour fermer.

#### **Exercice 2.1.5 : Conversion de Couleur et Dessin Basique**

  * **Objectif :** Appliquer une conversion de couleur et dessiner des formes et du texte sur une image.
  * **Tâche :**
    1.  Créez un nouveau fichier Python nommé `webcam_draw.py`.
    2.  Utilisez le code de l'exercice précédent (`webcam_stream.py`) comme base.
    3.  À l'intérieur de la boucle de lecture de frames :
          * Convertissez chaque frame de BGR vers RGB (gardez la version BGR originale ou convertissez-la de nouveau en BGR si vous voulez l'afficher).
          * Dessinez un cercle rouge rempli au centre de la frame.
          * Dessinez une ligne verte traversant la frame (par exemple, de coin à coin ou horizontale).
          * Ajoutez un texte "Bonjour \!" en blanc quelque part sur la frame.
          * Affichez la frame *avec les dessins* dans la fenêtre.
  * **Vérification :** Exécutez le script. Le flux de votre webcam devrait apparaître avec le cercle, la ligne et le texte superposés.

-----

Une fois que vous avez réussi ces exercices, n'oubliez pas de mettre à jour votre checklist dans le document principal en cochant les cases de la section **2.1 Introduction à OpenCV**.
