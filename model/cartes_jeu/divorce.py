#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from carte import carte
try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    from model.cartes_jeu.carte import carte


#carte de la fast-track correspondant au divorce 
class divorce(carte):
    def __init__(self, iu = None):
        self.iu= iu_divorce() 
    
    def dimunition_cash(self,joueur):
        #perte total de l'argent du joueur
        joueur.info_joueur.diminution_cash((joueur.info_joueur.cash))

    def demande_divorce(self, joueur):
        #methode utiliser pour le divorce
        self.iu.message()
        self.dimunition_cash(joueur)
    
    def activation(self,joueur):
        #methode d'activation
        self.demande_divorce(joueur)

#interface du divorce
class iu_divorce():

	def __init__(self) :
		pass

	def message(self, texte="il se peut que vous soyez en situation de divorce par conséquent vous allez perdre tous votre cash"):
		input(texte)


if __name__ == "__main__":
    pass

"""	from test_info_joueur import info_joueur
	from test_player import player

	cf=divorce()
	j1=player()
	cf.demande_divorce(j1)
"""
