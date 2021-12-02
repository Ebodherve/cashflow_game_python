#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    from cartes_jeu.opportunite import ig_opportunite as opportunite
except:
    from model.cartes_jeu.opportunite import ig_opportunite as opportunite

from random import choice

class grande_opportunite():
    def __init__(self):
        nom ="grande opportunite"
        self.liste_grande_opp = [opportunite(nom,"maison à louer à douala",8000,500,100)]
        self.liste_grande_opp.append(opportunite(nom,"action à logimarcket inc ",8000,500,100))
        self.liste_grande_opp.append(opportunite(nom,"acheter une action dans un champs ",8000,500,100))
        self.liste_grande_opp.append(opportunite(nom,"acheter des biens à la brocante",8000,500,100))
        self.liste_grande_opp.append(opportunite(nom,"acheter une plantation",8000,500,100))
        self.liste_grande_opp.append(opportunite(nom,"acheter une boutique",8000,500,100))
    def activation(self,joueur):
        choice(self.liste_grande_opp).activation(joueur)
    def connection_gui(self,gui):
        for op in self.liste_grande_opp:
            op.connection_iu(gui)


        
