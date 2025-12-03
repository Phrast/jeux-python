from models import *
from db_init import *
import random


def get_tous_personnages():
    """Recupere tous les perso"""
    personnages = []
    for data in personnages_table.find():
        perso = Hero(data["nom"], data["attaque"], data["defense"], data["pv"])
        personnages.append(perso)
    return personnages


def get_monstre_aleatoire():
    """Recupere un monstre aleatoire"""
    monstres = []
    for data in monstres_table.find():
        monstre = Monstre(data["nom"], data["attaque"], data["defense"], data["pv"])
        monstres.append(monstre)
    return random.choice(monstres)


def save_score(nom, vagues):
    """save le score"""
    scores_table.insert_one({
        "joueur": nom,
        "vagues": vagues
    })


def get_scores():
    """Recupere les 3 meilleurs"""
    data = scores_table.find()
    data = data.sort("vagues", -1)
    data = data.limit(3)
    scores = []
    for score in data:
        scores.append(score)
    return scores


def afficher_scores():
    """affiche le meilleur score"""
    print("\nMeuilleur Score :")
    scores = get_scores()

    if len(scores) == 0:
        print("Aucun score enregistre.")
        return

    i = 1
    for score in scores:
        print(f"{i}. {score['joueur']} - {score['vagues']} vagues")
        i = i + 1


def afficher_equipe(equipe):
    """Affiche l'equipe"""
    print("\nVotre equipe :")
    if len(equipe) == 0:
        print("Aucun personnage selectionne.")
    else:
        i = 1
        for perso in equipe:
            print(f"{i}. {perso}")
            i = i + 1


def afficher_personnages(persos):
    """Affiche la liste des persos"""
    print("\nPersonnages disponibles :")
    i = 1
    for perso in persos:
        print(f"{i}. {perso}")
        i = i + 1


