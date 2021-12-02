#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import de
#import espace


class pion(object):
    def __init__(self,espace = None,de = None,iu = None):
        #initialisation des attributs
        self.position = None
        self.taille_espace = 0
        self.couleur = None
        self.connection_de(de)
        self.numero_position = 0
        self.ancienne_pos = self.numero_position
        self.connnection_espace(espace)
        
    def connection_de(self,de = None):
        if de != None:
            self.de = de
            self.de.pion = self
        else:
            pass
    def connection_iu(self,iu):
        if iu != None:
            self.iu = iu
        else:
            self.iu = iupion()
        self.iu.pion = self
    def deplace(self,joueur = None,nbr = 0):
        #conservation de la position actuelle
        self.ancienne_pos = self.numero_position
        #calcule du nouveau numero de position
        if nbr + self.numero_position > self.taille_espace:
            self.numero_position = nbr + self.numero_position - self.taille_espace
        else:
            self.numero_position += nbr
        #deplacement du pion en interface
        # self.iu.deplace_pion()
        # l'espace doit se charger de déplacer le pion
        #deplacement sur espace
        if joueur != None:
            self.tombe_carte(joueur)

    def tombe_carte(self,joueur = None):
        # activation d'une carte sur l'espace avec le couple 
        # des deux positions anciennes et nouvelles du joueur
        if joueur != None:
            self.espace.active_carte(joueur,(self.ancienne_pos,self.numero_position))
        # de cette facon la partie peut etre au courant, sur
        # l'intervalle de déplacement du pion et peut gerer 
        # le cas ou le pion passe sur la carte cheque de paie
    
    def retourne_position(self):
        self.deplace()
        return self.numero_position
    
    def connnection_espace(self,espace = None):
        if espace != None:
            self.espace = espace
            self.espace.pion = self
            self.taille_espace = self.espace.taille()-1
            #interface par défaut ou celui passé en parametre
    def position(self):
        return self.numero_position


#interface du pion
class iupion:
    def __init__(self):
        self.pion = None
    def deplace_pion(self,position = None):
        if position == None:
            print("pion en position : "+str(self.pion.numero_position))
        else:
            print("pion en position : ",str(position))

if __name__ == "__main__":
    from player import player
    from espace import espace
    j1 = player()
    esp = espace()
    p1 = pion(espace=esp)
    p1.deplace(j1,2)
    
    
