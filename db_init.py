from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]

personnages_table = db["personnages"]
monstres_table = db["monstres"]
scores_table = db["scores"]

def init_database():
    """on injecte les monstres et les personnages"""

    # on vide les collections avant car problème de pile a venir sans doute
    personnages_table.delete_many({})
    monstres_table.delete_many({})

    #on crée les heroes
    liste_perso = [
        {"nom": "Guerrier", "attaque": 15, "defense": 10, "pv": 100},
        {"nom": "Mage", "attaque": 20, "defense": 5, "pv": 80},
        {"nom": "Archer", "attaque": 18, "defense": 7, "pv": 90},
        {"nom": "Voleur", "attaque": 22, "defense": 8, "pv": 85},
        {"nom": "Paladin", "attaque": 14, "defense": 12, "pv": 110},
        {"nom": "Sorcier", "attaque": 25, "defense": 3, "pv": 70},
        {"nom": "Chevalier", "attaque": 17, "defense": 15, "pv": 120},
        {"nom": "Moine", "attaque": 19, "defense": 9, "pv": 95},
        {"nom": "Berserker", "attaque": 23, "defense": 6, "pv": 105},
        {"nom": "Chasseur", "attaque": 16, "defense": 11, "pv": 100}
    ]

    #on crée les monstres
    liste_monstres = [
        {"nom": "Gobelin", "attaque": 10, "defense": 5, "pv": 50},
        {"nom": "Orc", "attaque": 20, "defense": 8, "pv": 120},
        {"nom": "Dragon", "attaque": 35, "defense": 20, "pv": 300},
        {"nom": "Zombie", "attaque": 12, "defense": 6, "pv": 70},
        {"nom": "Troll", "attaque": 25, "defense": 15, "pv": 200},
        {"nom": "Spectre", "attaque": 18, "defense": 10, "pv": 100},
        {"nom": "Golem", "attaque": 30, "defense": 25, "pv": 250},
        {"nom": "Vampire", "attaque": 22, "defense": 12, "pv": 150},
        {"nom": "Loup-garou", "attaque": 28, "defense": 18, "pv": 180},
        {"nom": "Squelette", "attaque": 15, "defense": 7, "pv": 90}
    ]

    # on les injecte
    personnages_table.insert_many(liste_perso)
    monstres_table.insert_many(liste_monstres)

    print("Base de donnees initialisee!")


init_database()
