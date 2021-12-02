#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from random import choice
#from carte import carte

# dans sa premiere version 
# -----------------------ce jeu ne tiendra pas compte de la liste des investissements et ne proposera qu'un seul----------------------- 
# ceci doit etre pris en compte apres
#---------------------------------------------------------------------------------------------------------------------------------------

try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    #from carte import carte
    from model.cartes_jeu.carte import carte
    


class investissement(carte):
    def __init__(self, nom = "investissement",description = None, position = None, prix_max = 4000, cashflow = None, cout_marche = None, iu = None):
        carte.__init__(self,nom = nom, position = position, description = description)
        self.prix_max = prix_max
        self.cashflow = cashflow
        self.cout_marche = cout_marche
        self.iu = uiinvestissement(self)
        
    def sajouter_au_investissement(self):
        #ajout dans les investissements
        #retour des informations de l'investissement dans le profil du joueur
        return {"nom":self.nom,"cout sur le marché ": self.cout_marche,"prix max sur le marché ":self.prix_max,"cash flow":self.cashflow,"vente":"vendre cette"+ str(self.nom)+" à {} "}

    def se_vendre(self,joueur):
        #paie du joueur
        joueur.info_joueur.diminution_cash(self.cout_marche)
        #service de l'ajout de l'investissement 
        joueur.info_joueur.ajout_investissement(self)
        #augmentation des entrees 
        joueur.info_joueur.augmenter_les_entrees(self.cashflow)

    def test_cash(self,joueur):
        #teste si le joueur a assez de cash pour pouvoir acheter l'investissement    
        return self.cout_marche <= joueur.info_joueur.cash

    def propose_investissement(self,joueur = None):
        #proposition de vente d'un investissement
        validation = False
        choix = self.iu.demande_dachat()
        if choix == "acheter":
            validation = self.test_cash(joueur)
        #boucle permettant de tester si le veut acheter et si il possede le cash requit
        while not validation and choix == "acheter":
            #proposition du choix de pret à la banque
            choix = self.iu.demande_de_pret()
            if choix == "pret":
                joueur_valide_pret = self.iu.propose_pret_somme()
                #si le joueur choisi de faire un 
                if joueur_valide_pret:
                    #alors il empreinte
                    joueur.empreinter(self.cout_marche)
            choix = self.iu.demande_dachat()
            if choix== "acheter":
                validation = self.test_cash(joueur)
        # à la sortie de la boucle si il veut acheter il a focément assez de cash pour le faire  
        if choix=="acheter":
            joueur.acheter(self)
    def activation(self, joueur):
        #activation d'un investissement
        self.propose_investissement(joueur)

class investissement_ft(investissement):
    def __init__(self,nom = "investissement",description = None, position = None, prix_max = 4000, cashflow = None, cout_marche = None, iu = None):
        investissement.__init__(self,nom,description, position, prix_max, cashflow, cout_marche, iu)
        
    def propose_investissement(self, joueur):
        self.iu.demande_dachat(lambda : self.acheter(joueur))
            
    def acheter(self,joueur):
        if self.test_cash(joueur):
            #lorsque le joueur a assez de cash il achete
            self.se_vendre(joueur)
            self.iu.passer()
        else:
            # lorsqu'il n'a pas assez de cash il passe son tour 
            # et avec l'affichage du nouveau message
            self.iu.pas_de_cash()
            
        
class iu_investissement_ft():
    def __init__(self):
        pass
    def demande_dachat(self,achat):
        pass
    def passer(self):
        pass
    def pas_de_cash(self):
        pass        

class liste_investissement:
    def __init__(self,iu = None):
        self.iu = iu_liste_investissement(self)
        self.liste_investissement = [investissement(nom = None, description="achetez une villa au prix de 2000dollards qui vous rameneras 10000 dollards",position = None, prix_max = 600, cashflow = 100, cout_marche = 50, iu = None),
                       investissement(nom = None, description="achetez une action chez visart studio au prix de 2000 dollards qui vous rameneras 50000 dollards",position = None, prix_max = 500, cashflow = 75, cout_marche = 40, iu = None),
                       investissement(nom = None, description="achetez une action chez investor inc au prix de 200 dollards qui vous rameneras 6000 dollards",position = None, prix_max = 300, cashflow = 78, cout_marche = 20, iu = None)]

class ig_liste_investissement:
    def __init__(self,iu = None):
        self.iu = iu_liste_investissement(self)
        self.liste_investissement = [investissement(nom = None, description="achetez une villa au prix de 2000dollards qui vous rameneras 10000 dollards",position = None, prix_max = 600, cashflow = 100, cout_marche = 50, iu = None),
                       investissement(nom = None, description="achetez une action chez visart studio au prix de 2000 dollards qui vous rameneras 50000 dollards",position = None, prix_max = 500, cashflow = 75, cout_marche = 40, iu = None),
                       investissement(nom = None, description="achetez une action chez investor inc au prix de 200 dollards qui vous rameneras 6000 dollards",position = None, prix_max = 300, cashflow = 78, cout_marche = 20, iu = None)]
    def connection_interface(self,iu_inv):
        for inv in self.liste_investissement:
            inv.connection_interface(iu=iu_inv)

def activation(self,joueur):
        #choix hasardueux d'une carte investissement
        self.liste_investissement[self.iu.propose__liste_investissement()].activation(joueur)


#interface d'un objet investissement 
class uiinvestissement:
    def __init__(self,investissement):
        self.investissement = investissement

    def demande_dachat(self,text="voulez acheter un invetissement ? "):
        choix = input("n-pour 'non' : "+text)
        if choix== "n":
            return ""
        return "acheter"

    def demande_de_pret(self,text="voulez vous un faire un pret ?"):
        choix = input("n-pour 'non' : "+text)
        if choix== "n":
            return ""
        return "pret"

    def propose_pret_somme(self,text="faire un pret de : "):
        choix = input("n-pour non : "+text+str(self.investissement.cout_marche))
        if choix== "n":
            return False
        return True

    def evenement(self):
        #arrivé d'un investissement probable 
        print("carte : ",self.investissement.nom)
        input(self.investissement.description + str(self.investissement.somme))  

class iu_liste_investissement(object):
    def __init__(self,liste_investissement = None):
        self.liste_investissement = liste_investissement

    def propose__liste_investissement(self):
        print("faire le choix d'un investissement :")
        i=0
        for invest in self.liste_investissement.liste_investissement :
            print(str(i) +"-"+ invest.description)
            i+=1
        try :
            return int(input("choix d'un investissement par son numero : "))
        except:
            return 0
        



if __name__ == "__main__":
    from test_player import player

    j1 = player()
    inv1 = investissement()
    inv1.propose_investissement(j1)

