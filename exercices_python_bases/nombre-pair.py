"""
Exercice 2 : Générateur de Nombres Pairs
Objectif : Utiliser les boucles for et les conditions.

Description :
Écrivez un programme qui demande à l'utilisateur un nombre entier N. Le programme doit ensuite afficher tous les nombres pairs de 1 à N (inclus).

Exemple d'exécution :

Entrez un nombre entier : 10

Nombres pairs jusqu'à 10 :
2
4
6
8
10
Entrez un nombre entier : 7

Nombres pairs jusqu'à 7 :
2
4
6
"""
while True:
    nombre_str = input("Entrez un nombre entier : ")
    if not nombre_str.isdigit():
        print("Entrée invalide. Veuillez entrer un nombre entier.")
    else:
        nombre = int(nombre_str)
        if nombre < 1:
            print("Veuillez entrer un nombre supérieur ou égal à 1.")
        else:
            break

if nombre == 1:
    print("Pas de nombre pair jusqu'à 1.")
else:
    print(f"Nombres pairs jusqu'à {nombre} :")
    for i in range(2, nombre + 1, 2): # Commencer à 2 et avancer par pas de 2
        print(i)