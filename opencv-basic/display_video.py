import cv2

# 1. Spécifiez le chemin de votre vidéo
video_path = "../assets/videos/video1.mp4" # Remplacez par le nom de votre fichier vidéo

# 2. Créer un objet VideoCapture
# Le chemin du fichier vidéo est passé en argument.
cap = cv2.VideoCapture(video_path)

# 3. Vérifier si la vidéo a été ouverte correctement
if not cap.isOpened():
    print(f"Erreur : Impossible d'ouvrir la vidéo à l'emplacement '{video_path}'.")
    print("Vérifiez le chemin du fichier et le format de la vidéo.")
    exit() # Quitter le programme si la vidéo ne peut pas être ouverte

# 4. Boucler pour lire les frames une par une
while True:
    # cap.read() retourne deux valeurs :
    #   - ret : un booléen (True si la frame a été lue avec succès, False sinon)
    #   - frame : la frame lue (une matrice NumPy)
    ret, frame = cap.read()

    # Si 'ret' est False, cela signifie que la fin de la vidéo a été atteinte
    # ou qu'il y a eu une erreur de lecture.
    if not ret:
        print("Fin de la vidéo ou erreur de lecture.")
        break

    # 5. Afficher la frame dans une fenêtre
    cv2.imshow('Ma Vidéo', frame)

    # 6. Attendre une touche pour une courte durée (ex: 25 ms)
    # Ceci contrôle la vitesse de lecture de la vidéo.
    # Si 'q' (ou une autre touche) est pressée, la boucle s'arrête.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 7. Libérer l'objet VideoCapture (fermer le fichier vidéo)
cap.release()

# 8. Détruire toutes les fenêtres créées par OpenCV
cv2.destroyAllWindows()

print("Script terminé.")


