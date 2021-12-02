#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from carte import carte
#from test_carte import carte
try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    from model.cartes_jeu.carte import carte

#prototype non finie
class reve(carte):
    def __init__(self,nom = None,prix =None,iu = None):
        self.nom = nom
        self.prix = prix
        if iu == None:
            self.iu = iureve(self)
        else:
            self.iu = iu(self)
    def test_cash_necessaire(self,joueur):
        #test du cash necessaire sur le joueur
        return True
    def achat_reve(self,joueur):
        #achat du reve
        pass
    def evaluation_joueur(self,joueur):
        #evaluation du joueur
        if self.test_cash_necessaire(joueur):
            self.achat_reve(joueur)
            self.iu.achat_reve()
    def activation(self,joueur):
        #self activation du reve lorsque le de se pose dessus
        self.evaluation_joueur(joueur)

class iureve:
    def __init__(self,reve = None):
        self.reve = reve
    def achat_reve(self,text = "reve acheter"):
        input(text)

if __name__ == "__main__":
    from test_player import player
    j1 = player()
    reve1 = reve()
    reve1.activation(j1)
    