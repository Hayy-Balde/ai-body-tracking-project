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

def compter_voyelles(words):
    voyelles = ('a','e','i','o','u','y')
    compteur = 0
    for i in voyelles:
        compteur += words.lower().count(i)

    print(f"La phrase contient {compteur} voyelle.s.")


phrase = str(input("Entrez une phrase : "))
compter_voyelles(phrase)