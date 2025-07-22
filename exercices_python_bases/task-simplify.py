"""
Exercice 3 : Gestionnaire de Tâches Simplifié
Objectif : Utiliser les listes, les boucles while et les entrées utilisateur pour créer un menu interactif.

Description :
Créez un programme de gestion de tâches très simple. Le programme doit afficher un menu à l'utilisateur et lui permettre d'effectuer les actions suivantes jusqu'à ce qu'il choisisse de quitter :

Ajouter une tâche : Demander le nom de la tâche et l'ajouter à une liste.

Afficher les tâches : Lister toutes les tâches numérotées.

Supprimer une tâche : Demander le numéro de la tâche à supprimer et la retirer de la liste.

Quitter : Mettre fin au programme.

Gérez les cas où l'utilisateur entre un numéro de tâche invalide.

Exemple d'exécution :

Bienvenue dans le gestionnaire de tâches !

Menu :
1. Ajouter une tâche
2. Afficher les tâches
3. Supprimer une tâche
4. Quitter

Votre choix : 1
Entrez le nom de la tâche : Faire les courses
Tâche 'Faire les courses' ajoutée.

Votre choix : 1
Entrez le nom de la tâche : Appeler Jean
Tâche 'Appeler Jean' ajoutée.

Votre choix : 2
Vos tâches :
1. Faire les courses
2. Appeler Jean

Votre choix : 3
Entrez le numéro de la tâche à supprimer : 1
Tâche 'Faire les courses' supprimée.

Votre choix : 2
Vos tâches :
1. Appeler Jean

Votre choix : 4
Au revoir !
"""
tasks = []

while True:
    print("\n\n============= Gestionnaire de Tâches Simplifié =============")
    print("============================ MENU ==========================")
    print("\n 1. Ajouter une tâche")
    print(" 2. Afficher les tâches")
    print(" 3. Supprimer une tâche")
    print(" 4. Quitter \n")

    choix_str = input("Faites un choix : ")

    if not choix_str.isdigit():
        print("\nChoix invalide. Veuillez entrer un nombre entre 1 et 4.")
        continue # Retourne au début de la boucle

    choix = int(choix_str)
    print("\n") # Ligne vide pour espacer l'affichage

    if choix == 1:
        task = input("Entrez le nom de la tâche : ")
        if task.strip(): # S'assurer que la tâche n'est pas vide
            tasks.append(task.strip())
            print(f"Tâche '{task.strip()}' ajoutée.")
        else:
            print("Le nom de la tâche ne peut pas être vide.")
    elif choix == 2:
        if not tasks: # Equivalent à len(tasks) < 1
            print("Aucune tâche disponible.")
        else:
            print("Vos tâches :")
            for k, v in enumerate(tasks, start=1):
                print(f"{k}. {v}")
    elif choix == 3:
        if not tasks:
            print("Aucune tâche à supprimer.")
            continue
        
        print("Tâches actuelles :")
        for k, v in enumerate(tasks, start=1):
            print(f"{k}. {v}")

        index_str = input("Entrez le numéro de la tâche à supprimer : ")
        if not index_str.isdigit():
            print("Index invalide. Veuillez entrer un nombre.")
        else:
            index = int(index_str)
            if 1 <= index <= len(tasks):
                removed_task = tasks.pop(index - 1)
                print(f"Tâche '{removed_task}' supprimée.")
            else:
                print("Numéro de tâche inexistant.")
    elif choix == 4:
        print("Au revoir !")
        break # Utiliser 'break' pour sortir proprement de la boucle 'while True'
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")