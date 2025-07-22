import cv2
import numpy as np # OpenCV utilise NumPy pour les images

# Créer une image noire vide (une toile) de 500x500 pixels (hauteur, largeur)
# np.zeros() crée une matrice remplie de zéros (noir),
# (500, 500, 3) pour hauteur, largeur, et 3 canaux de couleur (BGR)
# dtype=np.uint8 signifie que les valeurs des pixels sont des entiers non signés de 0 à 255
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

# 1. Dessiner une ligne : cv2.line(image, point_début, point_fin, couleur, épaisseur)
# Les couleurs sont en BGR : (Bleu, Vert, Rouge)
# Ex: (255, 0, 0) pour le Bleu, (0, 255, 0) pour le Vert, (0, 0, 255) pour le Rouge
cv2.line(canvas, (50, 50), (450, 50), (0, 255, 0), 5) # Ligne verte horizontale

# 2. Dessiner un cercle : cv2.circle(image, centre, rayon, couleur, épaisseur)
# Épaisseur -1 pour remplir le cercle
cv2.circle(canvas, (250, 250), 75, (0, 0, 255), -1) # Cercle rouge rempli

# 3. Dessiner un rectangle : cv2.rectangle(image, coin_sup_gauche, coin_inf_droit, couleur, épaisseur)
cv2.rectangle(canvas, (100, 350), (400, 450), (255, 0, 0), 3) # Rectangle bleu

# 4. Dessiner du texte : cv2.putText(image, texte, origine, police, taille_police, couleur, épaisseur, type_ligne)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, 'Bonjour OpenCV!', (50, 200), font, 1, (255, 255, 255), 2, cv2.LINE_AA) # Texte blanc

# Afficher l'image avec les dessins
cv2.imshow('Dessins OpenCV', canvas)

# Attendre une touche pour quitter
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Script de dessin terminé.")