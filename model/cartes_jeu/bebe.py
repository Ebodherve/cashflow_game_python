#!/usr/bin/python
# -*- coding: UTF-8 -*-

#from carte import carte
try:
    from cartes_jeu.carte import carte
except:
    from model.cartes_jeu.carte import carte


#from test_carte import carte

class bebe(carte):
    def __init__(self):
        carte.__init__(self)
        self.nbre_max_de_bebe = 5
        self.iu = iubebe(self)
        self.depense = 10
    def peut_avoir_bebe(self,joueur):
        #cacul du nombre de bebe
        return joueur.info_joueur.nb_bebe < self.nbre_max_de_bebe
    def ajout_bebe(self,joueur):
        #ajout d'un bebe
        joueur.info_joueur.nb_bebe += 1
        #augmentation des depenses
        joueur.info_joueur.augmentation_cash_depense(self.depense)
    def avoir_nouveau_bebe(self,joueur):        
        #methode permettant de faire avoir un nouveau bebe
        if self.peut_avoir_bebe(joueur):
            self.iu.averti_bebe()
            self.ajout_bebe(joueur)
        else:
            self.iu.pas_de_bebe()
    def activation(self,joueur):
        #activation de la carte bebe
        self.avoir_nouveau_bebe(joueur)
        
class iubebe:
    def __init__(self,bebe):
        self.bebe = bebe
    def averti_bebe(self,text = "nouveau bébé : "):
        input(text)
    def pas_de_bebe(self,text = "vous n'aurez pas de bebe :"):
        self.averti_bebe(text = text)
        

if __name__=="__main__":
    from test_player import player
    j1 = player()
    be = bebe()
    be.avoir_nouveau_bebe(j1)
            



