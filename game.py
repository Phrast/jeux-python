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


def tour_joueur(equipe, monstre):
    """Tour equipe"""

    print("\nVotre tour : ")
    for perso in equipe:
        if perso.est_vivant() and monstre.est_vivant():
            degats = perso.attaquer(monstre)
            print(f"{perso.nom} attaque {monstre.nom} et inflige {degats} degats!")


def tour_monstre(equipe, monstre):
    """Tour monstre"""

    print("\nTour du monstre : ")
    vivants = personnages_vivants(equipe)
    if vivants:
        cible = random.choice(vivants)
        degats = monstre.attaquer(cible)
        print(f"{monstre.nom} attaque {cible.nom} et inflige {degats} degats!")

        if not cible.est_vivant():
            print(f"{cible.nom} est mort!")


def combat_tour(equipe, monstre):
    """fait un tour"""

    tour_joueur(equipe, monstre)

    if not monstre.est_vivant():
        print(f"\n{monstre.nom} est mort!")
        return True #pour jouer vague

    tour_monstre(equipe, monstre)

    if not equipe_vivante(equipe):
        return False #pour jouer vague


def choisir_personnage(disponibles):
    """choix joueur"""

    while True:
        try:
            choix = int(input("Entrez le numero du personnage: "))
            if choix >= 1 and choix <= len(disponibles):
                return choix
            else:
                print(f"Entrez un nombre entre 1 et {len(disponibles)}.")
        except:
            print("Entree invalide. Entrez un nombre.")


def ajouter_a_equipe(disponibles, equipe, choix):
    """ajoute le perso a l'equipe et enleve de dispo"""

    perso_choisi = disponibles.pop(choix - 1)
    equipe.append(perso_choisi)
    print(f"\n{perso_choisi.nom} a rejoint votre equipe!")


def creer_equipe():
    """creer l'equipe de 3 personnages"""
    disponibles = get_tous_personnages()
    equipe = []

    print("\nCréez votre equipe")
    print("Selectionnez 3 personnages pour votre equipe.")

    while len(equipe) < 3 and disponibles:

        afficher_personnages(disponibles)

        print(f"\nPersonnage {len(equipe) + 1}/3")
        choix = choisir_personnage(disponibles)
        ajouter_a_equipe(disponibles, equipe, choix)

    afficher_equipe(equipe)

    return equipe


def victoire_manche_message(vague):
    """message de win"""

    print(f"\nVague {vague} terminee! prochaine manche")
    time.sleep(1)


def defaite(nom_joueur, vague):
    """gere la defaite d'un joueur"""

    print(" Perdu")
    print(f"\nVous avez survecu {vague - 1} vagues!")
    save_score(nom_joueur, vague - 1)
    afficher_scores()


def afficher_etat_jeu(equipe, monstre):
    """Affiche les PV du monstre et de l'equpe"""

    print(f"\n Etats du jeux")
    print(f"Monstre: {monstre.pv}/{monstre.pv_max}")
    for perso in equipe:
        if perso.est_vivant():
            print(f"{perso.nom}: {perso.pv}/{perso.pv_max}")
    time.sleep(2)


def jouer_vague(equipe, monstre, vague, nom_joueur):
    """boucle de tour pour faire la vague"""

    while True:
        resultat = combat_tour(equipe, monstre) #True le monstre est en vie False si l'equipe est morte

        if resultat == True:
            victoire_manche_message(vague)
            return True #pour lancer combat

        elif resultat == False:
            defaite(nom_joueur, vague)
            return False #pour lancer combat

        afficher_etat_jeu(equipe, monstre)


def lancer_combat(equipe, nom_joueur):
    """Lance la logique de jeux"""
    vague = 0

    print("Début du combat")

    while equipe_vivante(equipe):
        vague += 1
        monstre = get_monstre_aleatoire()
        afficher_etat_combat(equipe, monstre, vague)

        if not jouer_vague(equipe, monstre, vague, nom_joueur):
            break
            