"""
Exercice 5 : Annuaire Téléphonique Simple
Objectif : Utiliser les dictionnaires et les fonctions.

Description :
Créez un programme qui gère un annuaire téléphonique simple en utilisant un dictionnaire. Le dictionnaire stockera des noms comme clés et des numéros de téléphone comme valeurs.

Votre programme doit définir les fonctions suivantes :

ajouter_contact(annuaire, nom, numero) : Ajoute un nouveau contact ou met à jour un contact existant.

rechercher_contact(annuaire, nom) : Affiche le numéro de téléphone d'un contact donné, ou un message si le contact n'est pas trouvé.

supprimer_contact(annuaire, nom) : Supprime un contact de l'annuaire.

afficher_annuaire(annuaire) : Affiche tous les contacts de l'annuaire.

Utilisez un menu interactif (comme dans l'exercice 3) pour permettre à l'utilisateur d'utiliser ces fonctions.

Exemple d'exécution :

Bienvenue dans l'annuaire téléphonique !

Menu :
1. Ajouter/Mettre à jour un contact
2. Rechercher un contact
3. Supprimer un contact
4. Afficher tous les contacts
5. Quitter

Votre choix : 1
Nom du contact : Alice
Numéro de téléphone : 0612345678
Contact Alice ajouté/mis à jour.

Votre choix : 1
Nom du contact : Bob
Numéro de téléphone : 0798765432
Contact Bob ajouté/mis à jour.

Votre choix : 4
Annuaire :
Alice : 0612345678
Bob : 0798765432

Votre choix : 2
Nom du contact à rechercher : Alice
Le numéro de Alice est : 0612345678

Votre choix : 2
Nom du contact à rechercher : Charlie
Contact Charlie non trouvé.

Votre choix : 3
Nom du contact à supprimer : Bob
Contact Bob supprimé.

Votre choix : 4
Annuaire :
Alice : 0612345678

Votre choix : 5
Au revoir !

"""
annuaires = dict({
    "balde" : '1234',
    'sory' : "423"
})

def ajouter_contact(annuaires, nom, numero):
    annuaires[nom] = numero
    print(f"Contact {nom} ajouté/mis à jour.")

def rechercher_contact(annuaires, nom) :
    if len(annuaires) > 0 :
        if nom in annuaires.keys():
            ligne = annuaires[nom]
            print(f"Le numéro de {nom} est : {ligne}")
        else:
            print(f"{nom} introuvable dans l'annuaire")
    else:
        print("Annuaire vide")
    

def supprimer_contact(annuaires, nom) :
    if nom in annuaires.keys():
        annuaires.pop(nom)
        print(f"Contact {nom} supprimé.")
    else:
        print(f"Ce {nom} est absent de l'annuaire")
    
def afficher_annuaire(annuaires) :
    print("Annuaire : ")
    if len(annuaires) > 0 :
        for k,v in annuaires.items():
            print(f"{k} : {v}")
    else:
        print("Annaire Vide")

while True :
    print("\n\nBienvenue dans l'annuaire téléphonique ! ")
    print("================= BMENU =================\n")
    print("1. Ajouter/Mettre à jour un contact\n")
    print("2. Rechercher un contact\n")
    print("3. Supprimer un contact\n")
    print("4. Afficher tous les contacts\n")
    print("5. Quitter\n\n")

    choix = input("Faites un choix : ")

    if choix.isdigit() and (0 < int(choix) < 6) :
        choix = int(choix)
        if choix == 1:
            print("Votre Choix : 1")
            nom = str(input("Nom du contact : "))
            numero = str(input("Numéro de téléphone : "))
            ajouter_contact(annuaires, nom, numero)

        elif choix == 2:
            print("Votre Choix : 2")
            nom = str(input("Nom du contact à rechercher : "))
            rechercher_contact(annuaires, nom)

        elif choix == 3:
            print("Votre Choix : 3")
            nom = str(input("Nom du contact à supprimer : "))
            supprimer_contact(annuaires, nom)

        elif choix == 4:
            print("Votre Choix : 4")
            afficher_annuaire(annuaires)

        elif choix == 5:
            print("Votre Choix : 5")
            print("Au revoir !")
            exit(0)
    else:
        print("Choix Invalide")