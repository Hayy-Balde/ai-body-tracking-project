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
annuaires = {} # Commencer avec un annuaire vide pour une nouvelle utilisation

def ajouter_contact(contacts_dict, nom, numero):
    # Validation basique du nom et numéro
    if not nom.strip():
        print("Le nom du contact ne peut pas être vide.")
        return
    if not numero.strip():
        print("Le numéro de téléphone ne peut pas être vide.")
        return
    
    contacts_dict[nom.strip()] = numero.strip() # Utiliser .strip() pour enlever les espaces inutiles
    print(f"Contact '{nom.strip()}' ajouté/mis à jour.")

def rechercher_contact(contacts_dict, nom) :
    if not contacts_dict: # Plus pythonique que len(contacts_dict) > 0
        print("Annuaire vide.")
        return

    nom_recherche = nom.strip()
    if nom_recherche in contacts_dict: # Méthode plus directe pour vérifier l'existence de la clé
        print(f"Le numéro de {nom_recherche} est : {contacts_dict[nom_recherche]}")
    else:
        print(f"'{nom_recherche}' introuvable dans l'annuaire.")
    
def supprimer_contact(contacts_dict, nom) :
    if not contacts_dict:
        print("Annuaire vide, aucune contact à supprimer.")
        return
        
    nom_a_supprimer = nom.strip()
    if nom_a_supprimer in contacts_dict:
        del contacts_dict[nom_a_supprimer] # ou contacts_dict.pop(nom_a_supprimer)
        print(f"Contact '{nom_a_supprimer}' supprimé.")
    else:
        print(f"'{nom_a_supprimer}' est absent de l'annuaire.")
    
def afficher_annuaire(contacts_dict) :
    print("\n--- Annuaire ---")
    if not contacts_dict:
        print("L'annuaire est vide.")
    else:
        for k, v in contacts_dict.items():
            print(f"{k} : {v}")
    print("----------------")

while True :
    print("\n\nBienvenue dans l'annuaire téléphonique !")
    print("================= MENU =================")
    print("1. Ajouter/Mettre à jour un contact")
    print("2. Rechercher un contact")
    print("3. Supprimer un contact")
    print("4. Afficher tous les contacts")
    print("5. Quitter")
    print("========================================")

    choix_str = input("Faites un choix : ")

    if not choix_str.isdigit():
        print("\nChoix invalide. Veuillez entrer un nombre entre 1 et 5.")
        continue # Retourne au début de la boucle

    choix = int(choix_str)

    if choix == 1:
        nom = input("Nom du contact : ")
        numero = input("Numéro de téléphone : ")
        ajouter_contact(annuaires, nom, numero)

    elif choix == 2:
        nom = input("Nom du contact à rechercher : ")
        rechercher_contact(annuaires, nom)

    elif choix == 3:
        nom = input("Nom du contact à supprimer : ")
        supprimer_contact(annuaires, nom)

    elif choix == 4:
        afficher_annuaire(annuaires)

    elif choix == 5:
        print("Au revoir !")
        break # Utiliser 'break' pour sortir proprement de la boucle 'while True'
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")