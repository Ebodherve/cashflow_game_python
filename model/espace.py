#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import partie
#from model.cartes_jeu.bebe import bebe

try:
    from cartes_jeu.bebe import bebe
    from cartes_jeu.reve import reve
    from cartes_jeu.controle_fiscale import controle_fiscale,iu_proces
    from cartes_jeu.divorce import divorce
    from cartes_jeu.doodad import liste_doodad
    from cartes_jeu.cheque_de_paie import cheque_de_paie,ig_cheque_de_paie
    from cartes_jeu.investissement import liste_investissement,investissement_ft 
    from cartes_jeu.charite import charite 
    from cartes_jeu.liste_opportunite import liste_opportunite,ig_liste_opportunite
    #from cartes_jeu.liste_opportunite import liste_opportunite
    from cartes_jeu.reduction_taille import reduction_taille
    from cartes_jeu.marche import marche,ig_marche
except :
    from model.cartes_jeu.bebe import bebe
    from model.cartes_jeu.reve import reve
    from model.cartes_jeu.controle_fiscale import controle_fiscale,iu_proces
    from model.cartes_jeu.divorce import divorce
    from model.cartes_jeu.doodad import liste_doodad
    from model.cartes_jeu.cheque_de_paie import cheque_de_paie,ig_cheque_de_paie
    from model.cartes_jeu.investissement import liste_investissement,investissement_ft 
    from model.cartes_jeu.charite import charite 
    from model.cartes_jeu.liste_opportunite import liste_opportunite,ig_liste_opportunite
    from model.cartes_jeu.reduction_taille import reduction_taille
    from model.cartes_jeu.marche import marche,ig_marche


try :
    from interfaces.iliste_interfaces_carte import liste_interfaces_cartes
except:
    from model.interfaces.iliste_interfaces_carte import liste_interfaces_cartes

#import pion

#classe de l'espace de jeu

class espace(object):
    def __init__(self,partie = None,pion = None,interface_carte_indice = None,iu = None,iu_ig = None):
        self.partie_ = partie
        
        if interface_carte_indice != None:
            self.interface_carte_indice = interface_carte_indice
        else:
            #carte qui sont communes à la rate-race et à la fast-track
            self.interface_carte_indice = ["cheque","bebe","opportunite","reduction_de_taille","cheque","cheque","bebe","opportunite","reduction_de_taille","cheque"]
        self.deplace = None
        self.connection_pion(pion)
        self.reduction_taille = 0

        #self.liste_carte = {"bebe":bebe(),"reve":reve(),"controle_fiscale":controle_fiscale(),"proces":controle_fiscale(iu = iu_proces()),"divorce":divorce(),"doodad":liste_doodad(),"cheque":cheque_de_paie(), 
        #                    "investissement":liste_investissement(),"charite":charite(),"opportunite":liste_opportunite(),"reduction_de_taille":reduction_taille(self),"marche":marche()}
        self.liste_carte = {"bebe":bebe(),"reve":reve(),"controle_fiscale":controle_fiscale(),"proces":controle_fiscale(iu = iu_proces()),"divorce":divorce(),"doodad":liste_doodad(),"cheque":ig_cheque_de_paie(), 
                            "investissement":liste_investissement(),"charite":charite(),"opportunite":ig_liste_opportunite(),"reduction_de_taille":reduction_taille(self),"marche":ig_marche()}
        
        self.nb_carte = self.taille()
        self.active_carte = lambda joueur,numero_pion : self.activation_normale_carte(joueur,numero_pion)
        
        self.connection_des_inteface_de_communication(liste_interfaces_cartes.liste_int_cartes())
        self.connection_des_inteface_de_cartes(iu)
        self.connection_des_inteface_ig(iu_ig)        
    
    #connection à l'interface utilisateur
    def connection_des_inteface_ig(self,iu = None):
        if iu != None:
            self.iu = iu
        
    #la reduction de taille est activer par le carte reduction de taille
    def effet_reduction_taille(self,joueur,numero_pion):
        self.pion.iu.deplace_pion()
        self.iu.affiche_lancer()
        #print("reduction taille")
        if self.reduction_taille > 1:
            self.reduction_taille -= 1
        else:
            #desactivation de l'effet
            self.active_carte = lambda joueur,numero_pion : self.activation_normale_carte(joueur,numero_pion)
        
    def taille(self):
        return len(self.interface_carte_indice)

    def activation_normale_carte(self,joueur,couple_numero_pion):
        cheque_de_paie = self.test_cheque_de_paie(couple_numero_pion)
        if cheque_de_paie == None:
            self.pion.iu.deplace_pion()
            #activation de la carte correspondante à la nouvelle position du pion
            self.liste_carte[self.interface_carte_indice[couple_numero_pion[1]]].activation(joueur)
        else:
            #activation du pion avec la liste des cheques de paie
            for indice in cheque_de_paie:
                self.pion.iu.deplace_pion(indice)
                #activation de la carte correspondante à la nouvelle position du pion
                self.liste_carte[self.interface_carte_indice[indice]].activation(joueur)
        #numero_pion
        
    def connection_pion(self,pion= None):
        #connection de l'espace à un pion
        if pion != None:
            self.pion = pion
            self.pion.connnection_espace(self)
    def test_cheque_de_paie(self,couple_position):
        #teste si le cheque de paie ne sera depasse
        ancienne_position = couple_position[0]
        nouvelle_position = couple_position[1]
        liste_cheque_paie = []
        #si ancienne position inferieure à nouvelle position
        if ancienne_position>nouvelle_position:
            #dans ce teste on cherche dans deux liste si il y a cheque de paie            
            #recherche du cheque de paie entre la derniere position du pion et la fin de liste des cartes
            for ele in self.interface_carte_indice[ancienne_position+1:]:
                ancienne_position+=1
                if ele == "cheque" :
                    liste_cheque_paie.append(ancienne_position)
            #recherche du cheque de paie entre la position 0 et la nouvelle position du pion
            ancienne_position = 0
            for ele in self.interface_carte_indice[:nouvelle_position]:
                if ele == "cheque":
                    liste_cheque_paie.append(ancienne_position)
                ancienne_position+=1
        else:
            # dans ce cas l'ancienne position est inferieur à la nouvelle
            posi_cheque = ancienne_position+1
            for ele in self.interface_carte_indice[ancienne_position+1:nouvelle_position]:
                if ele == "cheque":
                    liste_cheque_paie.append(posi_cheque)
                posi_cheque += 1
             
        if len(liste_cheque_paie)>0:
            return liste_cheque_paie
        else:
            return None
    def connection_des_inteface_de_cartes(self,dict_interfaces = None):
        for cle in dict_interfaces.keys():    
            if "une_opportunite" != cle:
                self.liste_carte[cle].connection_interface(dict_interfaces[cle])        
        self.liste_carte["opportunite"].connection_gui(dict_interfaces["une_opportunite"])
            
    def connection_des_inteface_de_communication(self,dict_interfaces = None):
        try :
            for cle in dict_interfaces.keys():
                dict_interfaces[cle].connection_interface(self.liste_carte[cle])
        except:
            pass
        
        
#definitions des differents espaces 

# l'interface de suivante est celle qu'il faudrait 
# utiliser:  self.liste_carte = {"bebe":bebe(),"reve":reve(),"controle_fiscale":controle_fiscale(),"proces":controle_fiscale(iu = iu_proces()),"divorce":divorce(),"doodad":liste_doodad(),"cheque":cheque_de_paie(), 
# "investissement":liste_investissement(),"charite":charite(),"oppotunite":liste_opportunite(),"reduction":reduction_taille(self),"marche":marche()}


#rate-race
class rate_race(espace):
    def __init__(self,partie = None,pion = None):
        #remplissage des cartes de l'espace
        self.interface_carte_indice = ["bebe","opportunite","cheque","doodad","reduction_taille","marche","cheque","opportunite","bebe","cheque","doodad","reduction_taille","marche","cheque"]
        # initialisation de la classe parente
        espace.__init__(self,partie=partie,pion = pion,interface_carte_indice = self.interface_carte_indice)
        #interface des cartes 
        #self.liste_carte = {"bebe":bebe(),"doodad":liste_doodad(),"cheque":cheque_de_paie(partie = self.partie),"cheque":charite(),"opportunite":liste_opportunite(),"reduction_taille":reduction_taille(self),"marche" : marche()}
    
    def sortie_rate_race(self,joueur,fast_track):
        #sortie de la rate-race :
        # multiplication  du cash du joueur par 100 :
        joueur.info_joueur.multiplication_cash(100)
        fast_track.entrer_fast_track(joueur.de.pion)
        
    
#rate-race
class fast_track(espace):
    def __init__(self,partie = None,pion = None):
        #remplissage des cartes de l'espace
        self.interface_carte_indice = ["bebe","cheque","investissement","divorce","investissement",'charite',"controle_fiscale","bebe","cheque","investissement",'charite',"divorce","cheque","investissement","controle_fiscale","charite"]
        
        espace.__init__(self,partie=partie,pion = pion,interface_carte_indice = self.interface_carte_indice)
        #interface des cartes 
        #self.liste_carte = {"bebe":bebe(),"doodad":liste_doodad(),"cheque":cheque_de_paie(partie = self.partie),"cheque":charite(),"opportunite":liste_opportunite(),"reduction_taille":reduction_taille(self),"marche" : marche()}
    
    def entree_fast_track(self,pion):
        #entree du joueur dans la fast-track    
        self.connection_pion(pion)



