#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from rendu2.controleur.model.cartes_jeu.investissement import investissement
#from carte import carte
try:
    from cartes_jeu.carte import carte
except ModuleNotFoundError:
    from model.cartes_jeu.carte import carte

class cheque_de_paie(carte):
    def __init__(self,iu = None,partie = None):
        if iu == None:
            self.iu = iu_cheque_de_paie(self)
        else:
            self.iu = iu
        #La carte cheque de paie doit connetre la partie qui se joue
        self.partie = partie
    
    def en_faillite(self,joueur):
        #teste si le joueur est faillite
        return joueur.info_joueur.cheque_de_paie<0
    
    def a_des_dettes(self,joueur):
        return len(joueur.info_joueur.dettes) > 0
    
    def action_faillite(self,joueur):
        #methode permettant d'implémenter la faillite
        self.iu.faillite_joueur()
        while self.en_faillite(joueur) and len(joueur.info_joueur.investissement)>0 and self.a_des_dettes(joueur):
            #Tanque le joueur est en faillite, a toujours des investissement à vendre et des dettes à payer
            #Il doit les vendre et payer ses dettes
            if joueur.peut_payer_dettes():
                #paie de la premiere dette
                joueur.payer_dette_faillite()
            else:
                investissement = joueur.info_joueur.investissement[0]
                #vente du premier investissement
                joueur.vendre(investissement,investissement["cout sur le marché "]/2)
        if self.en_faillite(joueur):
            #à la sortie de la boucle si il est toujours en fallite il est éliminé
            self.elimination_joueur(joueur)
    
    def propose_son_cheque(self, joueur):
        #teste de situation de faillite
        if not self.en_faillite(joueur):
            #le joueur peut faire un choix entre recevoir son cheque de paie ou non
            choix = self.iu.demande_cheque_de_paie()
            if choix == "oui":
                #augmentation du cash du joueur
                joueur.info_joueur.ajout_cash(joueur.info_joueur.cheque_de_paie)
                #paie des accomptes sur les dettes 
                joueur.info_joueur.paie_des_dettes()
        else:
            self.action_faillite(joueur)
    
    def elimination_joueur(self,joueur):
        #cette methode permet d'eliminer un joueur lorsqu'il est en faillite totale
        pass
    
    def activation(self,joueur):
        self.propose_son_cheque(joueur)

class ig_cheque_de_paie(cheque_de_paie):
    def __init__(self,iu = None,partie = None):
        cheque_de_paie.__init__(self,iu = iu,partie = partie)
    def action_faillite(self,joueur):
        #methode permettant d'implémenter la faillite
        self.ui.passer()
        #self.iu.faillite_joueur()
    def propose_son_cheque(self, joueur):
        #teste de situation de faillite
        if not self.en_faillite(joueur):
            #le joueur peut faire un choix entre recevoir son cheque de paie ou non
            self.iu.demande_cheque_de_paie(paie = lambda:self.paie(joueur))
            #augmentation du cash du joueur
            #paie des accomptes sur les dettes 
        else:
            self.action_faillite(joueur)
    def paie(self,joueur):
        joueur.info_joueur.ajout_cash(joueur.info_joueur.cheque_de_paie)
        joueur.info_joueur.paie_des_dettes()
        self.iu.passer()

class iu_ig_cheque_de_paie:
    def __init__(self):
        pass
    def demande_cheque_de_paie(self,paie):
        pass
    

class iu_cheque_de_paie():
    def __init__(self,cheque_de_paie = None):
        self.cheque_de_paie = cheque_de_paie
    def demande_cheque_de_paie(self, text="voulez vous recevoir votre cheque de paie ?"):
        if input("n pour non"+text) == 'n':
            return ""
        else:
            return "oui"
    def faillite_joueur(self):
        print("Vous etes en faillite : ")
        
if __name__ =="__main__":
	from test_player import player
	j1=player()
	cp=cheque_de_paie()
	cp.propose_son_cheque(j1)

