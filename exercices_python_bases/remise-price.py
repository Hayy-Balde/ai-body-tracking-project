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
while True:
    price_str = input("Entrez le prix unitaire de l'article : ")
    try:
        price = float(price_str)
        if price <= 0:
            print("Le prix doit être un nombre positif.")
        else:
            break # Sortir de la boucle si le prix est valide
    except ValueError:
        print("Prix invalide. Veuillez entrer un nombre.")

while True:
    quantite_str = input("Entrez la quantité : ")
    try:
        quantite = int(quantite_str)
        if quantite <= 0:
            print("La quantité doit être un nombre entier positif.")
        else:
            break # Sortir de la boucle si la quantité est valide
    except ValueError:
        print("Quantité invalide. Veuillez entrer un nombre entier.")

total_price_before_discount = price * quantite
print(f"Prix total avant remise : {total_price_before_discount:.2f} euros") # Formatage à 2 décimales

if total_price_before_discount > 100:
    total_price_after_discount = total_price_before_discount * 0.9
    print(f"Prix total après remise : {total_price_after_discount:.2f} euros (remise de 10% appliquée)")
else:
    total_price_after_discount = total_price_before_discount
    print(f"Prix total après remise : {total_price_after_discount:.2f} euros (aucune remise appliquée)")