from db_init import *
from game import *


def demander_nom():
    """Demander nom"""

    nom_joueur = input("Entrez votre nom: ")
    while not nom_joueur:
        print("Le nom ne peut pas etre vide.")
        nom_joueur = input("Entrez votre nom: ")
    return nom_joueur


def choix_menu():
    """Affiche le menu et retourne le choix"""

    print("\n1. Demarrer le jeu")
    print("2. Afficher le classement")
    print("3. Quitter")
    return input("\nVotre choix: ")


def demarrer_jeu():
    """Demarre une nouvelle partie"""

    print("\nNouvelle partie")
    nom_joueur = demander_nom()
    print(f"\nBienvenue, {nom_joueur}!")

    equipe = creer_equipe()

    print("\nVotre equipe est prete!")
    input("Appuyez sur Entree pour commencer le combat...")

    lancer_combat(equipe, nom_joueur)


def main():
    """point d'entrée"""

    init_database()

    while True:
        choix = choix_menu()

        if choix == "1":
            demarrer_jeu()

        elif choix == "2":
            afficher_scores()

        elif choix == "3":
            break

        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

if __name__ == "__main__":
    main()