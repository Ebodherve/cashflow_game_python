#!/usr/bin/python
#from banque import banque
#from de import de
# -*- coding: UTF-8 -*-

try:
    from info_joueur import info_joueur
    from banque import banque
except:
    from model.info_joueur import info_joueur
    from model.banque import banque

from os import system


#import controleur
#import carte

class player(object):
    """cette classe permet de creer les joueurs de la partie"""
    def __init__(self,iu = None,banque = None,partie = None):
        #reconnaissance de la partie par le joueur 
        self.partie = partie
        #nom du joueur    
        self.name = ""
        # variable de sortie de la rate-race
        self.sortie_rate_race = False
        # variable de contenant le nombre fois que l'effet charite sera active
        self.charite = 0
        #banque 
        self.banque = banque
        #le de du joueur
        self.de = None
        #les differents infos du joueur
        self.info_joueur = info_joueur(nom = self.name)
        #class de contole
        self._controle = None
        self.lancer = lambda : self.lancer_un_de()
        #connection à un interface
        self.connection_iu(iu = iu)

    def connection_iu(self,iu = None):
        #interface du joueur
        if iu != None:
            self.iu = iu
        else:
            self.iu = iuplayer()
        self.iu.palyer = self
    def choisir_son_reve(self):
        pass
    
    def rembourser(self):
        pass
    
    def lancer_un_de(self):
        #actualisation des informations du joueur 
        self.info_joueur.actualisation()
        #interface du lancé du dé
        self.iu.lance_ment_du_de()
        #le joueur passe le méssage au dé d'activer le pion
        self.de.active_pion(self)
        #system("clear")


    def lancer_deux_de(self):
        #actualisation des informations du joueur 
        self.info_joueur.actualisation()
        #lancement de deux dés
        self.iu.lance_deux_de()
        resultat = self.de.lancer()+self.de.lancer()
        #le joueur passe un message au dé d'activer le pion
        self.de.active_pion(self,resultat)
        #ce lancement de deux se fait uniquement sous l'éffet de la charité 
        if self.charite > 0:
            self.charite -= 1
        else:
            self.lancer = lambda : self.lancer_un_de()        
        system("clear")

        
    def lancer_trois_de(self):
        #actualisation des informations du joueur 
        self.info_joueur.actualisation()
        choix = self.iu.propose_nbr_lancer()
        if choix == "1":
            self.de.active_pion(self)
        elif choix=="2":
            resultat = self.de.lancer()+self.de.lancer()
            #le joueur passe un message au dé d'activer le pion
            self.de.active_pion(self,resultat)
        else:
            resultat = self.de.lancer()+self.de.lancer()+self.de.lancer()
            #le joueur passe un message au dé d'activer le pion 
            self.de.active_pion(self,resultat)
        #system("clear")

        
    def acheter(self,opport_invest):
        #acheter une opportunitée
        opport_invest.se_vendre(self)
    
    def empreinter(self,cash = 0,dette = []):
        #empreint d'un joueur
        choix = self.iu.propose_empreint()
        if choix== "oui":
            self.info_joueur.ajout_cash(cash)
            self.info_joueur.augmentation_dette(somme = cash,interet=self.banque.taux_interet)
    
    def somme_pret_pour_paie(self,cash):
        #calcule de la somme necessaire pour la paie de ce cash
        #ce nombre est une multiple de 1000
        return banque.somme_pour_preter(self,somme = cash,cash = self.info_joueur.cash)
        #cash est la somme à preter
        #et self.info_joueur.cash est le cash du joueur

    
    def vendre(self,investissement,prix):
        #methode utilisée en cas de faillite 
        self.iu.propose_vente(investissement,prix)
        self.info_joueur.reduire_les_investissements([investissement])
        self.info_joueur.ajout_cash(prix)

    def payer_dette(self):
        pass

    def payer_dette_faillite(self):
        self.info_joueur.diminution_dette_zero()
    
    def peut_payer_dettes(self):
        # methode permettant de savoir si le joueur 
        # peut payer la dette la plus ancienne        
        return self.info_joueur.cash >= self.info_joueur.dettes[0][0]
    def connection_iu_infojoueur(self,iu = None):
        try:
            self.info_joueur.connection_iu(iu)
        except:
            pass
    def connection_interface_infojoueur(self,interface = None):
        interface.connection_interface(self.info_joueur)
        

#interface du joueur
class iuplayer:
    def __init__(self,player = None):
        self.palyer = player
    def demande_choix_achat(self):
        pass
    def propose_empreint(self) :
        return "oui"
    def lance_ment_du_de(self):
        input("lancer le dé : ")
    def lance_deux_de(self):
        input("Lancer de deux dé : ")
    def lance_trois_de(self):
        input("lancement de trois de : ")
    def propose_nbr_lancer(self):
        return input("lancer 1-2 ou 3 dés : ")
    def propose_vente(self,inv,prix):
        #focntion de vente dont le prix est propose 
        input(inv["vente"].format(prix))
        



if __name__=="__main__":
    from pion import pion
    from de import de
    from espace import espace,rate_race,fast_track
    from banque import banque
    
    j1 = player(banque = banque())
    esp = fast_track()
    p1 = pion(espace=esp)
    de1 = de(j1,p1)
    
    while True :
        j1.lancer()

