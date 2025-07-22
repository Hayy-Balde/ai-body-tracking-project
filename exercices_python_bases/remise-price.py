"""
Exercice 1 : Calculateur de Prix Total avec Remise
Objectif : Utiliser les variables, les entrées utilisateur, les opérateurs arithmétiques et les conditions.

Description :
Écrivez un programme qui demande à l'utilisateur :

Le prix unitaire d'un article.

La quantité d'articles achetés.

Le programme doit ensuite calculer le prix total. Si le prix total dépasse 100 euros, appliquez une remise de 10%. Affichez le prix total avant et après remise (s'il y a lieu).

Exemple d'exécution :

Entrez le prix unitaire de l'article : 15.50
Entrez la quantité : 3

Prix total avant remise : 46.50 euros
Prix total après remise : 46.50 euros (aucune remise appliquée)
Entrez le prix unitaire de l'article : 25
Entrez la quantité : 5

Prix total avant remise : 125.00 euros
Prix total après remise : 112.50 euros (remise de 10% appliquée)
"""

price = input("Entrez le prix de l'article : ")

# if not price.isdigit() or float(price) < 1:
#     print("Prix invalide")
#     exit(0)

quantite = input("Entrez la quantité souhaité : ")

if not quantite.isdigit() or float(quantite) < 1 :
    print("Quantité invalide")
    exit(0)

total_price = float(price) * float(quantite)
print("Prix Total avant remise ", total_price, " euros")

if total_price > 100 :
    print("Prix total après remise ", total_price - total_price * 0.1, " euros")
else :
    print("Prix total après remise ", total_price, " euros (aucune remise appliquée)")
