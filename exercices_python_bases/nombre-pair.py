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

nombre = input("Entrez un nomre entier : ")

if not nombre.isdigit():
    print("Entrez un nombre valide")
    exit(0)

if int(nombre) < 1 :
    print("Entrez un nombre superieur a 0")
    exit(0)

if int(nombre) == 1 :
    print("Pas de nombre pair")
    exit(0)


print(f"Nombres pairs jusqu'à {nombre} :")
for i in range(1, int(nombre) + 1):
    if i % 2 == 0:
        print(i)