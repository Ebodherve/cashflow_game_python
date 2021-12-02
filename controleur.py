#!/usr/bin/python
# -*- coding: UTF-8 -*-

import partie


class controleur(object):
    def __init__(self):
        #instanciation  d'une partie  
        self.partie = partie(controleur = self)
        
        self._controle = None

		
if __name__ == "__main__":
    from vue.carte.iu_MAINWINDOWS import igu_espacejeu
    from PyQt5 import QtCore, QtGui, QtWidgets
    import sys
    from model.pion import pion
    from model.de import de
    from model.espace import espace
    from model.player import player
    from model.interfaces.i_info_joueur import i_info_joueur
    from vue.carte.iu_login import igu_login    
    from vue.carte.iu_pageaccueil import igu_pageaccueil
    
    
    joueur1 = player()
    pion1 = pion()
    de1 = de(pion = pion1,joueur =joueur1)
    
    pion1.connection_de(de1)
    
    int_info = i_info_joueur(info_joueur=joueur1.info_joueur)
    #joueur1.connection_interface_infojoueur(int_info)
    #int_info.connection_interface(joueur1.info_joueur)
        
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = igu_espacejeu(MainWindow)

    #page d'enregistrement
    framelogin = QtWidgets.QFrame()
    page_enregistre =  igu_login(framelogin)
    
    #page d'accueil
    frameaccueil = QtWidgets.QFrame()
    page_accueil =  igu_pageaccueil(frameaccueil)
    
    ui.joueur = joueur1
    
    #ui.connection_joueur(joueur1)#lambda : joueur.lancer()
    #interface_carte_indice=ui.cle_carte(),
    espace1 = espace(pion=pion1,interface_carte_indice=ui.cle_carte(),iu = ui.liste_interfaces(),iu_ig=ui)
    #################
    #espace1.connection_des_inteface_de_cartes({"bebe":ui.gui_bebe,"cheque":ui.gui_poursuite,"opportunite":ui.gui_liste_opportunite})
    #espace1.active_carte(joueur=joueur1,numero_pion=[1,2])
    joueur1.connection_iu_infojoueur(ui)
    joueur1.connection_iu(ui)
    de1.connection_iu(ui)
    
    page_accueil.connection_continuer(lambda:page_accueil.affiche_autre_page(page_enregistre))
    page_enregistre.connection_continuer(lambda:page_enregistre.affiche_autre_page(ui))
    pion1.connection_iu(ui)
    page_accueil.affiche()
    #ui.affiche_jeu()
    
    sys.exit(app.exec_())
