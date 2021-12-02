#!/usr/bin/python
# -*- coding: UTF-8 -*-
# exo4
#from carte import carte
try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    from model.cartes_jeu.carte import carte

#prix : prix maximum sur l'opportunité
#cashflow : cashflow de l'opportunité
#prix_marcher : prix auquel le joueur peut acheter sur le marché
# 


class opportunite(carte):
    def __init__(self,nom = None,description = None, prix = 100,cashflow = None,prix_marcher = None,iu = None):
        carte.__init__(self,nom = nom,description =description)
        self.prix = prix
        self.cashflow = cashflow
        self.prix_marcher = prix_marcher
        self.connection_iu(iu)
    def connection_iu(self,iu):
        if iu == None:
            self.iu = iuopportunitee(self)
        else:
            self.iu = iu
            self.iu.opportunite = self 
    def test_cash(self,joueur):
        #test si le cash du joueur est suffisant
        return joueur.info_joueur.cash >= self.prix_marcher
    def propose_opportunite(self,joueur = None):
        validation = False
        #propsition du choix d'achat
        choix = self.iu.demande_dachat()
        if choix == "acheter":
            validation = self.test_cash(joueur)
        #boucle contraignant le joueur faire un pret s'il n'a pas le cash nécessaire pour faire l'achat
        while not validation and choix == "acheter":
            choix = self.iu.demande_de_pret()
            if choix == "pret":
                joueur_valide_pret = self.iu.propose_pret_somme()
                if joueur_valide_pret:
                    joueur.empreinter(self.prix_marcher)
            choix = self.iu.demande_dachat()
            if choix== "acheter":
                validation = self.test_cash(joueur)
        if choix=="acheter":
            joueur.acheter(self)
    def activation(self,joueur):
        self.propose_opportunite(joueur)
    def retourne_prix(self):
        return self.prix
    
    def sajouter_au_opportunite(self):
        return {"nom":self.nom,"cout sur le marché ": self.prix_marcher,"prix max sur le marché ":self.prix,"cashflow":self.cashflow,"vente":"vendre cette"+ str(self.nom)+" à {} "}
    
    def se_vendre(self,joueur):
        #paiement du joueur à la bnque
        joueur.info_joueur.diminution_cash(self.prix_marcher)
        #modifications des infos du joueur pour l'insertion de l'oppotunité
        joueur.info_joueur.ajout_opportunite(self)
        #augmentation des entrees
        joueur.info_joueur.augmenter_les_entrees(self.cashflow)
        
    def donnees_opportunite(self):
        return {"nom":self.nom,"description":self.description,
                "cashflow":self.cashflow,"prix":self.prix,"prix_marche":self.prix_marcher}


class ig_opportunite(opportunite):
    def __init__(self,nom = None,description = None, prix = 100,cashflow = None,prix_marcher = None,iu = None):
        opportunite.__init__(self,nom = nom,description = description, prix = prix,cashflow = cashflow,prix_marcher = prix_marcher,iu = iu)
    def propose_opportunite(self,joueur = None):
        #proposition de l'opportunite
        self.iu.demande_dachat(achat = lambda : self.achat(joueur))
        
    def achat(self,joueur):
        if self.test_cash(joueur):
            # achat de lopportunite
            joueur.acheter(self)
            # passage à l'étape suivante
            self.iu.passer()
        else:
            self.iu.propose_pret_somme(lambda : joueur.empreinte(self.prix_marcher))
        
        
class iu_ig_opportunite:
    def __init__(self,opportunite = None):
        self.opportunite = opportunite
    def demande_dachat(self,achat = None):
        #achat : fonction d'achat
        pass
    def propose_pret_somme(self,empreint = None):
        #empreint : fonction d'empreint
        pass
    def passer(self):
        #passage
        pass
            


class iuopportunitee:
    def __init__(self,opporunitee):
        self.opportunite = opporunitee
    def demande_dachat(self,text="voulez vous Acheter cet action ? "):
        choix = input("n-pour 'non' : "+str(text))
        if choix== "n":
            return ""
        return "acheter"

    def demande_de_pret(self,text="voulez vous un faire un pret ?"):
        choix = input("n-pour 'non' : "+text)
        if choix== "n":
            return ""
        return "pret"

    def propose_pret_somme(self,text="faire un pret de : "):
        choix = input("n-pour non : "+text+str(self.opportunite.retourne_prix()))
        if choix== "n":
            return False
        return True


if __name__ == "__main__":
    from player import player
    j1 =player()
    opport1 = opportunite()
    opport1.propose_opporntunite(j1)

