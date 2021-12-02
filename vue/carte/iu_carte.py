
from PyQt5 import QtCore


class igu_carte:
    def __init__(self,frame = None,lancer = None,dashboard = None):
        self.frame_principale = frame
        self.connection_dashboard(dashboard)
        self.connection_lancer(lancer)
        self.se_positionner([960,240])
        self.disparait()

    def suite(self,ijoueur = None):
        if ijoueur != None:
            ijoueur.lance()
    
    def disparait(self):
        #disparition de la carte (affichage du lancé)
        self.frame_principale.hide()
        try:
            self.lancer.affiche()
        except AttributeError:
            print("lancer")
    
    def affiche(self):
        self.frame_principale.show()
        try:
            self.dashboard.show()
        except AttributeError:
            print("affichage du dashboard : ")
        
    def connection_lancer(self,lancer = None):
        if lancer != None:
            self.lancer = lancer
    def connection_dashboard(self,dashboard = None):
        if dashboard != None:
            self.dashboard = dashboard
    def affiche_dashboard(self):
        try :
            self.dashboard.show()
        except AttributeError:
            pass
    def affiche_lancer(self):
        try:
            self.lancer.affiche()
        except AttributeError:
            pass
    def se_positionner(self,position):
        #positionnement d'une carte à des coordonnées bien precises
        self.frame_principale.move(position[0],position[1])  
    def se_redimensionner(self,haut,larg):
        #redimensionnement de la carte
        self.frame_principale.rezise(haut,larg)
    def connection_affiche_dash(self,affiche_dash = None):
        if affiche_dash != None:
            self.affiche_dash = affiche_dash
    
    def passer(self):
        # disparition de la carte
        self.disparait()
        # affichage du lancé
        self.affiche_lancer()
        




