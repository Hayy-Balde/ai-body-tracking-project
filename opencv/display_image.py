import cv2

# 1. Spécifiez le chemin de votre image
# Assurez-vous que 'mon_image.jpg' est dans le même dossier que ce script,
# ou indiquez le chemin complet (ex: 'C:/Users/VotreNom/Images/mon_image.jpg')
image_path = '../assets/images/mee.png' # Remplacez par le nom de votre image

# 2. Lire l'image
# cv2.imread() charge l'image dans une matrice NumPy.
# Si le chemin est incorrect ou l'image est corrompue, 'img' sera None.
img = cv2.imread(image_path)

# 3. Vérifier si l'image a été chargée correctement
if img is None:
    print(f"Erreur : Impossible de charger l'image à l'emplacement '{image_path}'.")
    print("Vérifiez le chemin du fichier et assurez-vous qu'il existe.")
else:
    # 4. Afficher l'image dans une fenêtre
    # Le premier argument est le nom de la fenêtre (arbitraire).
    # Le second argument est la matrice de l'image.
    cv2.imshow('Ma Première Image', img)

    # 5. Attendre qu'une touche soit pressée pour fermer la fenêtre
    # 0 signifie attendre indéfiniment. Un nombre (ex: 1000) attendrait 1000 ms (1 seconde).
    cv2.waitKey(0)

    # 6. Détruire toutes les fenêtres créées par OpenCV
    cv2.destroyAllWindows()

print("Script terminé.")