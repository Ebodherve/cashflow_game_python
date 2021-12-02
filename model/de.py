#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import player
#import pion


from random import choice

class de(object):
    def __init__(self,joueur = None,pion = None,iu = None) :
        self.liste_face = [1,2,3,4,5,6]
        self.face = 1
        self.pion = pion
        
        self.connection_joueur(joueur)
        self.connection_iu(iu)
        
    def connection_iu(self,iu):
        if iu !=None:
            self.iu = iu
        else:
            self.iu = iude()
        self.iu.de = self
    def afficher_resultat(self):
        pass
    def lancer(self):
        self.face = choice(self.liste_face)
        #self.iu.lancer()
        return self.face
    def retourner_resultat(self):
        return self.face
    def active_pion(self,joueur = None,resultat = None):
        if resultat == None:
            self.pion.deplace(joueur = joueur,nbr = self.lancer())
        else:
            self.pion.deplace(joueur,resultat)
    def connection_joueur(self,joueur):
        #connection d'un de à un espace
        if joueur != None:
            self.joueur = joueur
            self.joueur.de = self

class iude:
    def __init__(self) :
        self.de = None
    def lancer(self,text = "resultat du lancé : "):
        if self.de == None:
            print("de absent")
        else:
            print(text+str(self.de.retourner_resultat()))
        
            

if __name__ == "__main__":
    from pion import pion
    from player import player
    from espace import espace


