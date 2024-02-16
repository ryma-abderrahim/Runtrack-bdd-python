# Fichier zoo.py
from animal import AnimalManager
from cage import CageManager

def menu_principal():
    print("Menu Principal:")
    print("1. Gérer les animaux")
    print("2. Gérer les cages")
    print("3. Afficher tous les animaux")
    print("4. Calculer la superficie totale de toutes les cages")
    print("5. Quitter")

def main():
    animal_manager = AnimalManager()
    cage_manager = CageManager()

    while True:
        menu_principal()
        choix = input("Choisissez une option: ")

        if choix == "1":
            gestion_animaux(animal_manager, cage_manager)
        elif choix == "2":
            gestion_cages(cage_manager)
        elif choix == "3":
            animal_manager.afficher_animaux()
        elif choix == "4":
            cage_manager.calculer_superficie_totale()
        elif choix == "5":
            animal_manager.fermer_connexion()
            cage_manager.fermer_connexion()
            break
        else:
            print("Option invalide.")

def gestion_animaux(animal_manager, cage_manager):
    print("Gestion des Animaux:")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    choix = input("Choisissez une option: ")

    if choix == "1":
        animal_id=("ID de l'animal: ")
        nom = input("Nom de l'animal: ")
        race = input("Race de l'animal: ")
        cage_id = int(input("ID de la cage: "))
        date_naissance = input("Date de naissance de l'animal (YYYY-MM-DD): ")
        pays_origine = input("Pays d'origine de l'animal: ")
        animal_manager.ajouter_animal(animal_id,nom, race, cage_id, date_naissance, pays_origine)
    elif choix == "2":
        animal_id = int(input("ID de l'animal à supprimer: "))
        animal_manager.supprimer_animal(animal_id)
    elif choix == "3":
        animal_id = int(input("ID de l'animal à modifier: "))
        nom = input("Nouveau nom de l'animal: ")
        race = input("Nouvelle race de l'animal: ")
        cage_id = int(input("Nouvel ID de la cage: "))
        date_naissance = input("Nouvelle date de naissance de l'animal (YYYY-MM-DD): ")
        pays_origine = input("Nouveau pays d'origine de l'animal: ")
        animal_manager.modifier_animal(animal_id, nom, race, cage_id, date_naissance, pays_origine)
    else:
        print("Option invalide.")

def gestion_cages(cage_manager):
    print("Gestion des Cages:")
    print("1. Ajouter une cage")
    print("2. Supprimer une cage")
    print("3. Modifier une cage")
    choix = input("Choisissez une option: ")

    if choix == "1":
        superficie = float(input("Superficie de la cage (en m²): "))
        capacite_max = int(input("Capacité maximale de la cage: "))
        cage_manager.ajouter_cage(superficie, capacite_max)
    elif choix == "2":
        cage_id = int(input("ID de la cage à supprimer: "))
        cage_manager.supprimer_cage(cage_id)
    elif choix == "3":
        cage_id = int(input("ID de la cage à modifier: "))
        superficie = float(input("Nouvelle superficie de la cage (en m²): "))
        capacite_max = int(input("Nouvelle capacité maximale de la cage: "))
        cage_manager.modifier_cage(cage_id, superficie, capacite_max)
    else:
        print("Option invalide.")

if __name__ == "__main__":
    main()