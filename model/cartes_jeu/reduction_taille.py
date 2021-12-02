#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from carte import carte
try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    from model.cartes_jeu.carte import carte

class reduction_taille(carte):
    def __init__(self,espace = None,iu = None):
        carte.__init__(self)
        self.espace = espace
        if iu == None:
            self.iu = iu_reduction_taille(self)
        else:
            self.iu = iu
            self.iu.reduction_taille = self 
    def perdre_son_travaille(self,joueur):
        #prevention de la prete d'employ
        self.iu.previent_perte()
        #nombre de fois que la redution prendra effet
        self.espace.reduction_taille = 2
        #activation de l'effet reduction taille sur l'espace
        self.espace.active_carte = lambda joueur,numero_pion : self.espace.effet_reduction_taille(joueur,numero_pion)
        #annulation de l'effet de charite
        joueur.charite = 0
        #changement de la fonction de lancé pour un lancé de un dé
        joueur.lancer = lambda : joueur.lancer_un_de()

    def activation(self,joueur):
        self.perdre_son_travaille(joueur)
        



class iu_reduction_taille:
    def __init__(self,reduction = None):
        self.reduction_taille = reduction
    def previent_perte(self):
        input("reduction de taille, vous allez predre votre employe pour vos deux prochains tours : ")

