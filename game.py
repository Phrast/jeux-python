from models import *
import random
import time
from utils import *

def equipe_vivante(equipe):
    """on check si un perso est toujours vivant dans l'équipe"""

    for perso in equipe:
        if perso.est_vivant():
            return True
    return False


def personnages_vivants(equipe):
    """return les perso en vie"""

    vivants = []
    for perso in equipe:
        if perso.est_vivant():
            vivants.append(perso)
    return vivants


def afficher_etat_combat(equipe, monstre, vague):
    """Affiche l'etat du combat"""

    print(f"\nVague : {vague}")
    print(f"\nMonstre: {monstre}")
    print("\nEquipe:")
    for perso in equipe:
        if perso.est_vivant():
            print(f"  Vivant : {perso}")
        else:
            print(f"  Mort : {perso.nom}")


def combat_tour(equipe, monstre):
    """fait une manche"""

    print("\nVotre tour : ")
    for perso in equipe:
        if perso.est_vivant() and monstre.est_vivant():
            degats = perso.attaquer(monstre)
            print(f"{perso.nom} attaque {monstre.nom} et inflige {degats} degats!")

    if not monstre.est_vivant():
        print(f"\n{monstre.nom} est mort!")
        return True

    print("\nTour du monstre : ")
    vivants = personnages_vivants(equipe)
    if vivants:
        cible = random.choice(vivants)
        degats = monstre.attaquer(cible)
        print(f"{monstre.nom} attaque {cible.nom} et inflige {degats} degats!")

        if not cible.est_vivant():
            print(f"{cible.nom} est mort!")

    if not equipe_vivante(equipe):
        return False


def creer_equipe():
    """creer l'equipe de 3 personnages"""
    disponibles = get_tous_personnages()
    equipe = []

    print("\nCréez votre equipe")
    print("Selectionnez 3 personnages pour votre equipe.")

    while len(equipe) < 3 and disponibles:

        afficher_personnages(disponibles)

        # choix
        print(f"\nPersonnage {len(equipe) + 1}/3")
        while True:
            try:
                choix = int(input("Entrez le numero du personnage: "))
                if choix >= 1 and choix <= len(disponibles):
                    break
                else:
                    print(f"Entrez un nombre entre 1 et {len(disponibles)}.")
            except:
                print("Entree invalide. Entrez un nombre.")

        # retire de dispo et ajoute à l'équipe
        perso_choisi = disponibles.pop(choix - 1)
        equipe.append(perso_choisi)
        print(f"\n{perso_choisi.nom} a rejoint votre equipe!")

    afficher_equipe(equipe)

    return equipe


def lancer_combat(equipe, nom_joueur):
    """Lance la logique de jeux """
    vague = 0
    
    print("Début du combat")

    while equipe_vivante(equipe):
        vague += 1

        monstre = get_monstre_aleatoire()
        afficher_etat_combat(equipe, monstre, vague)

        while True:
            resultat = combat_tour(equipe, monstre)

            if resultat == True: 
                print(f"\nVague {vague} terminee! prochaine manche")
                time.sleep(1)
                break

            elif resultat == False:
                print(" Perdu")
                print(f"\nVous avez survecu {vague - 1} vagues!")

                # -1 car il perd avant la fin de la manche
                save_score(nom_joueur, vague - 1)

                afficher_scores()
                break

            print(f"\n Etats du jeux")
            print(f"Monstre: {monstre.pv}/{monstre.pv_max}")
            for perso in equipe:
                if perso.est_vivant():
                    print(f"{perso.nom}: {perso.pv}/{perso.pv_max}")

            time.sleep(2)

    return