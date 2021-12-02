#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import player

class banque(object):
    def __init__(self):
        self.nom = None
        self.liste_inscrit = [self]
        self.taux_interet = 0.1
    
    def somme_pour_preter(self,somme = 0,cash = 0):
        #somme à payer
        #cash du joueur
        somme_potentielle = somme - cash 
        if somme_potentielle <= 0:
            return 0
        elif somme_potentielle <=10:
            return (int(somme_potentielle)) * 1000
        elif somme_potentielle <= 100:
            return (int(somme_potentielle)//10)*1000
        else :
            return (int(somme_potentielle)//100)*1000
        
    def rembourser(self):
        pass
    
    def payer(self):
        pass
    
    def inscription_joueur(self,joueur):
        if len(self.liste_inscrit) < 3:
            self.liste_inscrit.append(joueur(banque = self))

