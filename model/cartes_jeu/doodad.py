#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from carte import carte
try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    from model.cartes_jeu.carte import carte

from random import choice

class doodad(carte):
    
    def __init__(self,nom = "doodad",description = "",position = 0,somme = 45,iu = None):
        carte.__init__(self,nom,position,description)
        self.somme = somme
        if iu == None:
            self.iu = iu_doodat(self)
        else:
            self.iu = iu
            iu.doodad = self
    
    def diminution_cash(self,joueur):
        #diminution du cash du joueur apres un evene ment inattendu 
        joueur.info_joueur.diminution_cash(self.somme)
    
    def a_asse_de_cash(self,joueur):
        #teste si le joueur a assez de cash pour l'évenement
        return joueur.info_joueur.cash >= self.somme
    
    def affecte_finance(self,joueur):
        #methode activer apres atterissage du pion
        self.iu.evenement()
        if self.a_asse_de_cash(joueur):        
            self.diminution_cash(joueur)
        else:
            pret = joueur.somme_pret_pour_paie(self.somme)
            if self.iu.propose_de_faire_un_pret(pret):
                joueur.empreinter(pret)

    def activation(self,joueur):
        self.affecte_finance(joueur)
        


class liste_doodad:
    def __init__(self):
        self.liste_doodad = [
                        ig_doodad(description="allez chez le dentiste vous as couter :",somme = 400),
                        ig_doodad(description="aider votre frère dans la maladie va vous couter :",somme = 250),
                        ig_doodad(description="un voyage pour douala vous à couter :",somme = 300)]
    def activation(self,joueur):
        #choix hasardueux d'une carte doodad
        choice(self.liste_doodad).activation(joueur)
    def connection_interface(self,iu):
        for ele in self.liste_doodad:
            ele.connection_interface(iu)

class ig_doodad(doodad):
    def __init__(self,nom = "doodad",description = "",position = 0,somme = 45,iu = None):
        doodad.__init__(self,nom = nom,description = description,position = position,somme = somme,iu = iu)
    def affecte_finance(self,joueur):
        #methode activer apres atterissage du pion
        self.iu.evenement(action = lambda : self.action_doodad(joueur),somme = self.somme,description=self.description)
    def action_doodad(self,joueur):
        if self.a_asse_de_cash(joueur):
            self.diminution_cash(joueur)
            self.iu.passer()
        else:
            pret = joueur.somme_pret_pour_paie(self.somme)
            self.iu.propose_de_faire_un_pret(somme = pret,action = lambda : self.empeint(joueur,pret))
    def empeint(self,joueur,somme):
        joueur.empreinter(somme)
        self.iu.passer()
        

class iu_doodat:
    def __init__(self,doodad = None):        
        self.doodad = doodad
        
    def evenement(self,description,prix,evenement = None):
        #arrivé d'un evenement inattendu
        print("carte : ",self.doodad.nom)
        input(self.doodad.description + str(self.doodad.somme))
    def propose_de_faire_un_pret(self,somme = 0):
        #dans le joueur le joueur n'a pas assez de cash
        choix = input("faire un pret de {} à la banque - (n pour 'non')".format(somme))
        return choix != "n"
    

if __name__=="__main__":
    from test_player import player
    j1 = player()
    liste_d = liste_doodad()
    liste_d.activation(j1)
    do = doodad(description="allez chez le dentiste vous as couter")
    do.activation(j1)
