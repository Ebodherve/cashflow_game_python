#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from banque import banque
#from de import de
#from info_joueur import info_joueur
from test_info_joueur import info_joueur
#import controleur
#import carte

class player(object):
    """cette classe permet de creer les joueurs de la partie"""
    def __init__(self):
        #interface du joueur
        self.iu = iuplayer(self)
        #nom du joueur    
        self.name = None
        ##
        self._appartient = None
        #banque 
        self.banque = None
        #liste des dé du joueur
        self.liste_de = []
        #les differents infos du
        self.info_joueur = info_joueur()
        #class de contole
        self._controle = None
    def choisir_son_reve(self):
        pass
    def rembourser(self):
        pass
    def lancer(self):
        if len(self.liste_de)==1:
        #lorsque le joueur n'a qu'un seul de à lancer
            self.liste_de[0].active_pion()
        elif len(self.liste_de)>1:
        # lorsqu'il a plusieur de à lancer un seul 
        # des de active le pion avec le resultat de tout les dés
            resultat_lance = 0
            for resultat in [de.retourner_resultat() for de in self.liste]:
                resultat_lance += resultat
            self.liste_de[0].active_pion(resultat_lance)
    def acheter(self,opport_invest):
        pass
    
    def empreinter(self,cash = 0,dette = []):
        choix = self.iu.propose_empreint()
        if choix== "oui":
            self.info_joueur.ajout_cash(cash)
            self.info_joueur.augmentation_dette(dette = [])

    def tirer(self):
        pass
    
    def possede_investissement(self,investisseur):
        pass
    
    def vendre(self,investisseur):
        pass
    def payer_dettes(self):
        pass

class iuplayer:
    def __init__(self,player):
        self.palyer = player
    def demande_choix_achat(self):
        pass
    def propose_empreint(self) :
        return "oui"

