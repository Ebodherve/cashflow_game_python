#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from carte import carte
try:
    from cartes_jeu.carte import carte
except:
    from model.cartes_jeu.carte import carte


class charite(carte):
    def __init__(self,iu =None ):
        carte.__init__(self)
        if iu==None:
            self.iu = iu_charite(self)
        else:
            self.iu = iu
            self.iu.charite = self
        
    def effet_charite(self,joueur):
        #reduction de 10%
        joueur.info_joueur.diminution_cash((joueur.info_joueur.cash)*0.1)
        #activation de l'effet charité
        joueur.charite = 3
        #changement de la fonction de lancé pour un lancé à deux dés
        joueur.lancer = lambda : joueur.lancer_deux_de()
        
    def demande_charite(self,joueur):
        #demande de charite
        accepte = self.iu.offre_charite()
        #si le joueur accepte
        if accepte:
            #activation de l'effet de charité
            self.effet_charite(joueur)
    def activation(self,joueur):
        self.demande_charite(joueur)


class iu_charite:
    def __init__(self,charite = None):
        self.charite = charite
    def offre_charite(self):
        print("carte charite : ")
        choix = input("n pour non : Voulez vous faire une offre de charite ? ")
        if choix=="n":
            return False
        else:
            return True


