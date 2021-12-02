#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from carte import carte
try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    from model.cartes_jeu.carte import carte


class proces(carte):
	def __init__(self):
		self.iu = iu_proces()

	def perte_du_cash(cash):
		pass

	def plainte(self):
		choix = self.iu.message()
		#info_joueur.perte_du_cash(cash)




class iu_proces():

	def __init__(self) -> None:
		pass

	def message(self, texte="il se peut que vous soyez attaqué en justice vous allez perdre la moitié de votre cash"):
		choix=input("valider sur ok ")
		if choix == "ok":
			return "choix valide"
