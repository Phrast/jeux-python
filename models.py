class Perso:
    def __init__(self, nom, attaque, defense, pv):
        self.nom = nom
        self.attaque = attaque
        self.defense = defense
        self.pv = pv
        self.pv_max = pv

    def est_vivant(self):
        return self.pv > 0

    def subir_degats(self, degats):
        degats_reels = max(0, degats - self.defense)
        self.pv = max(0, self.pv - degats_reels)
        return degats_reels

    def attaquer(self, cible):
        degats = cible.subir_degats(self.attaque)
        return degats

    def __str__(self):
        return f"{self.nom} - ATQ:{self.attaque} DEF:{self.defense} PV:{self.pv}/{self.pv_max}"


class Hero(Perso):
    pass


class Monstre(Perso):
    pass
