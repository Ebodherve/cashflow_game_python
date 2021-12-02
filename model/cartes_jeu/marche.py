#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from rendu2.controleur.model.de import de
#from carte import carte
from random import choice,randint
#from rendu2.controleur.vue.carte.iu_marche import igu_marche
try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    from model.cartes_jeu.carte import carte



class marche(carte):
    def __init__(self,iu = None):
        #investisseur
        self.investisseur = investisseur(self)
        #attribut permettant le calcul du prix d'un investissement
        self.prix_marche_actuelle = None
        if iu == None:
            self.iu = interface_marche(self)
        else:
            self.iu = iu
 
    def test_investissement(self,joueur):
        #test si le joueur possede l'investissement
        return len(joueur.info_joueur.investissement) > 0
    
    def achat_joueur(self,joueur):
        self.iu.affichage()
        #teste si le joueur detient le à un investissement à vendre
        if self.test_investissement(joueur):
            #si le joueur à un investissement dont le cashflow est négatif 
            if joueur.info_joueur.investissement[0]["cash flow"] < 0:
                #alors on une activation avec priorité sur le premier élément
                self.investisseur.acheter_investissement(joueur,priorite = 0)
            else:
                #si non on active le joueur sans priorité particuliere
                self.investisseur.activation(joueur)
        else:
            self.iu.pas_dinvestissement()
                            
    def prix_marche(self,inv):
        #calcule du prit d'un investissement sur le marché
        self.prix_marche_actuelle =  randint(inv["cout sur le marché "],inv["prix max sur le marché "])
        return self.prix_marche_actuelle
    
    def activation(self,joueur):
        #activation du marche
        self.achat_joueur(joueur)

#classe marche pour l'interface graphique
class ig_marche(marche):
    def __init__(self,iu = None,investisseur = None):
        marche.__init__(self,iu)
        self.connection_investisseur(investisseur)
    def achat_joueur(self,joueur):
        #teste si le joueur detient le à un investissement à vendre
        if self.test_investissement(joueur):
            #si le joueur à un investissement dont le cashflow est négatif 
            if joueur.info_joueur.investissement[0]["cashflow"] < 0:
                #alors on une activation avec priorité sur le premier élément
                self.investisseur.acheter_investissement(joueur,priorite = 0)
            else:
                #si non on active le joueur sans priorité particuliere
                self.investisseur.activation(joueur)
        else:
            self.iu.pas_dinvestissement()
    def connection_investisseur(self,investisseur = None):
        if investisseur!=None:
            self.investisseur = investisseur
        else:
            self.investisseur = ig_investisseur(self)
        self.investisseur.connection_iu(self.iu)
        


class investisseur(object):
    def __init__(self,marche = None):
        self.marche = marche
        self.investissement = None
        #investissement choisi
        self.choix_achat = None
        #prix sur le marche de l'investissement choisit
        self.prix_dachat = 0
    def connection_iu(self,iu = None):
        if iu != None:
            self.iu = iu
        else:
            self.iu = interface_investisseur(self)        
    
    def achete_au_joueur(self,joueur):
        #achat d'investissement à un joueur
        joueur.info_joueur.reduire_les_investissements([self.choix_achat])
        #puis augmentation de cash
        joueur.info_joueur.ajout_cash(self.prix_dachat)
        #passer le tour
        self.iu.passer()
    
    def acheter_investissement(self,joueur,priorite = None):
        #test de contenance d'un investissement chez le joueur
        if priorite== None:
            #choix d'un investissement
            self.choix_achat = choice(joueur.info_joueur.investissement)
            #renseignement du prix sur le marché
            self.prix_dachat = self.marche.prix_marche(self.choix_achat)
            #affichage du choix de l'investisseur
            choix = self.iu.propose()
            if choix == "vente":
                self.achete_au_joueur(joueur)
        else :
            #choix d'un investissement
            self.choix_achat = joueur.info_joueur.investissement[priorite]
            #l'achat se fait au prix max sur le marché
            self.prix_dachat = self.choix_achat["prix max sur le marché "]
            #affichage du choix de l'investisseur
            choix = self.iu.propose()
            if choix == "vente":
                self.achete_au_joueur(joueur)
            #message affiché lorsque celui ci n'a pas l'invetissement requi
    def activation(self,joueur):
        self.acheter_investissement(joueur)


class ig_investisseur(investisseur):
    def __init__(self,marche = None):
        investisseur.__init__(self)
        self.connection_marche(marche)
    def connection_marche(self,marche):
        if marche == None:
            self.marche = ig_marche(investisseur = self)
        else :
            self.marche = marche
    def acheter_investissement(self,joueur,priorite = None):
        #test de contenance d'un investissement chez le joueur
        if priorite== None:
            #choix d'un investissement
            self.choix_achat = choice(joueur.info_joueur.investissement)
            #renseignement du prix sur le marché
            self.prix_dachat = self.marche.prix_marche(self.choix_achat)
            #affichage du choix de l'investisseur
        else :
            #choix d'un investissement
            self.choix_achat = joueur.info_joueur.investissement[priorite]
            #l'achat se fait au prix max sur le marché
            self.prix_dachat = self.choix_achat["prix max sur le marché "]
            #affichage du choix de l'investisseur
        self.iu.propose(lambda : self.achete_au_joueur(joueur),[self.choix_achat,self.prix_dachat])
        #message affiché lorsque celui ci n'a pas l'invetissement requit
        

class interface_marche(object):
    def __init__(self,marche = None) :
        self.marche = marche
    def affichage(self,vente):
        print("carte maché")
    def pas_dinvestissement(self):
        input("Vous n'avez rien à vendre : ")

class interface_marche_ig(object):
    def __init__(self,marche = None) :
        self.marche = marche
    def affichage(self,vente = None):
        print("carte maché")
    def pas_dinvestissement(self):
        input("Vous n'avez rien à vendre : ")

class interface_investisseur(object):
    def __init__(self,investisseur):
        self.investisseur = investisseur
    def propose(self,text = "voulez vous vendre votre investissement ?"):
        print(text)
        print(self.investisseur.choix_achat)
        choix = input("n-pour 'non' :")
        if choix == 'n':
            return ""
        return "vente"

if __name__ == "__main__":
    from test_player import player
    j1 = player()
    inv1 = investisseur()
    inv1.acheter_investissement(j1)


