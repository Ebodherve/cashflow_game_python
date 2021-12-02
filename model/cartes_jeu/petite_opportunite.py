#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    from cartes_jeu.opportunite import ig_opportunite as opportunite
except:
    from model.cartes_jeu.opportunite import ig_opportunite as opportunite

from random import choice

class petite_opportunite:
    def __init__(self):
        nom ="petite opportunite"
        self.liste_petite_opp = [opportunite(nom,"acheter des biens à la brocante",8000,500,100)]
        self.liste_petite_opp.append(opportunite(nom,"Historic Trading Range: $10 - 30",8000,500,100))
        self.liste_petite_opp.append(opportunite(nom,"acheter une pharmatie",8000,500,100))
        self.liste_petite_opp.append(opportunite(nom,"investir dans une brocante",8000,500,100))
        self.liste_petite_opp.append(opportunite(nom,"Historic Trading Range: $10 - 30",8000,500,100))
    def activation(self,joueur):
        choice(self.liste_petite_opp).activation(joueur)
    def connection_gui(self,gui):
        for op in self.liste_petite_opp:
            op.connection_iu(gui)
        
        
        