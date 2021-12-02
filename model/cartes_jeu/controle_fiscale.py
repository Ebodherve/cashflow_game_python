#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from test_carte import carte
#from carte import carte
try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    from model.cartes_jeu.carte import carte

class controle_fiscale(carte):
    def __init__(self, iu = None):
        #gestion de plusieurs interfaces
        if iu == None:
            self.iu = iu_controle_fiscale(self)
        else:
            self.iu = iu
            iu.controle_fiscale = self
    def dimunition_cash(self,joueur):
        #diminution de la moitier du cash du joueur
        joueur.info_joueur.diminution_cash((joueur.info_joueur.cash)/2)
    def fraude_fiscale(self, joueur):
        #interface d'un lancé de dé 
        self.iu.message()
        #fonction activée lors d'un controle fiscale
        self.dimunition_cash(joueur)
    def activation(self,joueur):
        self.fraude_fiscale(joueur)


class iu_controle_fiscale():
    def __init__(self,controle_fiscale = None) :
        self.controle_fiscale = controle_fiscale
    def message(self, texte="il se peut que vous soyez accusé d'evasion fiscale vous allez perdre la moitie de votre cash") :
        input(texte)


class iu_proces():

	def __init__(self) :
		pass
	def message(self, texte="il se peut que vous soyez attaqué en justice vous allez perdre la moitié de votre cash"):
		input(texte)
		
if __name__ == "__main__":
    pass
"""	from test_carte import carte
	from test_info_joueur import info_joueur
	from test_player import player

	cf=controle_fiscale(iu = iu_proces())
	j1=player()
	cf.fraude_fiscale(j1)
"""
