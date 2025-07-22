import cv2

# 1. Créer un objet VideoCapture pour la webcam
# L'argument 0 indique la webcam par défaut.
# Si vous avez plusieurs webcams, essayez 1, 2, etc.
cap = cv2.VideoCapture(0)

# 2. Vérifier si la webcam a été ouverte correctement
if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la webcam.")
    print("Vérifiez que la webcam est connectée et que les pilotes sont à jour.")
    exit()

# 3. Boucler pour lire les frames de la webcam en continu
while True:
    ret, frame = cap.read()

    if not ret:
        print("Erreur : Impossible de recevoir une frame (peut-être la caméra est déconnectée?).")
        break

    # Convertir la frame de BGR (OpenCV par défaut) en RGB
    # MediaPipe et d'autres bibliothèques d'IA attendent souvent le format RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 4. Afficher la frame capturée
    # Ici, vous pourriez traiter 'frame_rgb' avec MediaPipe ou d'autres modèles.
    # Pour l'instant, affichons la version RGB (elle aura la même apparence visuelle)
    cv2.imshow('Flux Webcam (BGR)', frame) # L'original en BGR
    cv2.imshow('Flux Webcam (RGB)', frame_rgb) # La version convertie en RGB

    # 5. Attendre 1 ms. Si la touche 'q' est pressée, sortir de la boucle.
    # 0xFF est un masque pour capturer la touche ASCII.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 6. Libérer l'objet VideoCapture
cap.release()

# 7. Détruire toutes les fenêtres
cv2.destroyAllWindows()

print("Script terminé.")