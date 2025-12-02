from models import *
from db_init import *
import random


def get_tous_personnages():
    """Recupere tous les perso"""
    personnages = []
    for p in personnages_table.find():
        perso = Personnage(p["nom"], p["attaque"], p["defense"], p["pv"])
        personnages.append(perso)
    return personnages


def get_monstre_aleatoire():
    """Recupere un monstre aleatoire"""
    monstres = []
    for m in monstres_table.find():
        monstre = Monstre(m["nom"], m["attaque"], m["defense"], m["pv"])
        monstres.append(monstre)
    return random.choice(monstres)