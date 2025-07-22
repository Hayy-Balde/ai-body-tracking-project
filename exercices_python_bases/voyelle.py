"""
Exercice 4 : Compteur de Voyelles
Objectif : Utiliser les fonctions, les chaînes de caractères et les boucles.

Description :
Écrivez une fonction nommée compter_voyelles qui prend une chaîne de caractères (un mot ou une phrase) en argument. La fonction doit retourner le nombre de voyelles (a, e, i, o, u, y, en majuscules ou minuscules) présentes dans la chaîne.

En dehors de la fonction, demandez à l'utilisateur d'entrer une phrase, puis utilisez votre fonction pour afficher le nombre de voyelles dans cette phrase.

Exemple d'exécution :

Entrez une phrase : Bonjour le monde
La phrase contient 5 voyelles.
Entrez une phrase : PythOn
La phrase contient 2 voyelles.
"""
def compter_voyelles(text):
    voyelles = "aeiouy" # Peut être une chaîne, pas besoin d'un tuple
    compteur = 0
    text_lower = text.lower() # Convertir la phrase entière une seule fois

    for char in text_lower:
        if char in voyelles:
            compteur += 1
    
    return compteur # La fonction retourne le compteur, elle n'affiche pas

phrase = input("Entrez une phrase : ") # Pas besoin de str()
nombre_de_voyelles = compter_voyelles(phrase)
print(f"La phrase contient {nombre_de_voyelles} voyelle(s).")