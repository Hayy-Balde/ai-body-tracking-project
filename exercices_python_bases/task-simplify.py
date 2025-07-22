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
    print("\n 2. Afficher les tâches")
    print("\n 3. Supprimer une tâche")
    print("\n 4. Quitter \n\n")

    choix = input("Faites un choix : ")

    if choix.isdigit():
        choix = int(choix)
        print("\n\n")
        if choix == 1 :
            print("Votre choix 1")
            task = str(input("Entrez le nom de la tâche : "))
            tasks.append(task)
            print("Tâche '", task, "' ajoutée.")
        elif choix == 2 :
            print("Votre choix 2")
            if(len(tasks) < 1):
                print("Aucune tache disponible.")
            else:
                print("Vos taches : ")
                for k, v in enumerate(tasks, start=1):
                    print(k, ". ", v)
        elif choix == 3 :
            print("Votre choix 3")
            index = input("Entrez le numéro de la tâche à supprimer : ")

            if not index.isdigit():
                print("Index invalide")
            else:
                index = int(index)
                if index < 1 or index > len(tasks):
                    print("Index Inexistant")
                else:
                    task = tasks[index-1]
                    tasks.pop(index-1)
                    print("Tâche '", task, "' supprimée.")

        elif choix == 4:
            print("Bye Bye!!")
            exit(0)
        else:
            print("Choix invalide")

    else :
        print("Choix Invalide \n")