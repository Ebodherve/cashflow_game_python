from PyQt5 import QtWidgets,QtCore
from time import sleep

try:
    from model_cartes.m_MAINWINDOWS import Ui_MainWindow
    from iu_bebe import igu_bebe
    #from iu_doodad import igu_doodad
    from iu_charite import igu_charite
    from iu_controle_fiscale import igu_contole_fiscale
    from iu_divorce import igu_divorce
    from iu_investissement import igu_investissement
    from iu_marche import igu_marche
    from iu_poursuite import igu_proces
    from iu_reduction_taille import igu_reduction_taille
    from iu_rolldice import igu_rolldice
    from iu_liste_opportunite import igu_l_opportunite
    from iu_opportunite import igu_opportunite
    #from iu_marche import igu_marche
    from iu_paycheck import igu_paycheque
    from iu_doodad import igu_doodad
except ModuleNotFoundError:
    from vue.carte.model_cartes.m_MAINWINDOWS import Ui_MainWindow
    from vue.carte.iu_bebe import igu_bebe
    from vue.carte.iu_charite import igu_charite
    from vue.carte.iu_controle_fiscale import igu_contole_fiscale
    from vue.carte.iu_divorce import igu_divorce
    from vue.carte.iu_investissement import igu_investissement
    from vue.carte.iu_marche import igu_marche
    from vue.carte.iu_poursuite import igu_proces
    from vue.carte.iu_reduction_taille import igu_reduction_taille
    from vue.carte.iu_rolldice import igu_rolldice
    from vue.carte.iu_liste_opportunite import igu_l_opportunite
    from vue.carte.iu_opportunite import igu_opportunite
    #from vue.carte.iu_marche import igu_marche
    from vue.carte.iu_paycheck import igu_paycheque
    from vue.carte.iu_doodad import igu_doodad


class igu_espacejeu(Ui_MainWindow):
    def __init__(self,espaces,joueur=None):
        self.peut_afficher_dash = True
        self.espaces = espaces
        Ui_MainWindow.setupUi(self,self.espaces)
        self.pushButton_dashboard.clicked.connect(lambda : self.modifi_dashboard())
        self.connection_joueur(joueur)
        
        self.init_espace()
        # self.pushButton_quitter.clicked.connect(lambda : self.disparait())

        # interface du lancer du de
        framede = QtWidgets.QFrame(self.centralwidget)
        self.gui_rolldice = igu_rolldice(framede,dashboard=self.dashboard,lancer=lambda : self.lancer_de())
        #self.gui_rolldice.affiche()

        #interface de la carte bebe
        framebebe = QtWidgets.QFrame(self.centralwidget)
        self.gui_bebe = igu_bebe(framebebe,dashboard=self.dashboard,lancer = self.gui_rolldice)
        #self.gui_bebe.affiche()
        
        #-----------gui_cashflow_day------------ 
        
        #interface de carte charite
        framecharite = QtWidgets.QFrame(self.centralwidget)
        self.gui_charite = igu_charite(framecharite,dashboard=self.dashboard,lancer = self.gui_rolldice)
        #self.gui_charite.affiche()
        
        #interface du controle fiscale
        frame_controle_fiscale = QtWidgets.QFrame(self.centralwidget)
        self.gui_controle_fiscale = igu_contole_fiscale(frame_controle_fiscale,dashboard=self.dashboard,lancer = self.gui_rolldice)
        #self.gui_controle_fiscale.affiche()
        
        #interface de divorce
        frame_divorce = QtWidgets.QFrame(self.centralwidget)
        self.gui_divorce = igu_divorce(frame_divorce,dashboard=self.dashboard,lancer = self.gui_rolldice)
        #self.gui_divorce.affiche()
        
        #interface de la carte investissement
        frame_doodad = QtWidgets.QFrame(self.centralwidget)
        self.gui_doodad = igu_doodad(frame_doodad,dashboard=self.dashboard,lancer = self.gui_rolldice)
        #self.gui_doodad.affiche()
        
        #interface de la carte investissement
        frame_investissement = QtWidgets.QFrame(self.centralwidget)
        self.gui_investissement = igu_investissement(frame_investissement,dashboard=self.dashboard,lancer = self.gui_rolldice)
        #self.gui_investissement.affiche()
        
        frame_opportunite = QtWidgets.QFrame(self.centralwidget)
        self.gui_opportunite = igu_opportunite(frame_opportunite,dashborad=self.dashboard,lancer=self.gui_rolldice)
        #self.gui_opportunite.affiche()
        
        # interface de la liste des opportunites
        frame_l_opportunite = QtWidgets.QFrame(self.centralwidget)
        self.gui_liste_opportunite = igu_l_opportunite(frame_l_opportunite,dashboard=self.dashboard,lancer = self.gui_rolldice)
        #self.gui_liste_opportunite.affiche()
        
        # interface du marche
        frame_marche = QtWidgets.QFrame(self.centralwidget)
        self.gui_marche = igu_marche(frame_marche,dashboard = self.dashboard,lancer=self.gui_rolldice)
        #self.gui_marche.affiche()
        
        #interface du cheque de paie
        frame_paycheque = QtWidgets.QFrame(self.centralwidget)
        self.gui_paycheque = igu_paycheque(frame_paycheque,dashboard = self.dashboard,lancer=self.gui_rolldice)
        #self.gui_paycheque.affiche()
        
        #interface de la poursuite
        frame_poursuite = QtWidgets.QFrame(self.centralwidget)
        self.gui_poursuite = igu_proces(frame_poursuite,lancer = self.gui_rolldice,dashboard=self.dashboard)
        #self.gui_poursuite.affiche()
        
        #interface de reduction de taille
        frame_reduction_taille = QtWidgets.QFrame(self.centralwidget)
        self.gui_reduction_taille = igu_reduction_taille(frame_reduction_taille,dashboard = self.dashboard,lancer=self.gui_rolldice)
        #self.gui_reduction_taille.affiche()
    
    def lance_ment_du_de(self):
        pass    
    
    def liste_interfaces(self):
        #proces
        #doodad
        #liste_investissement
        #reve
        return {"bebe":self.gui_bebe,"controle_fiscale":self.gui_controle_fiscale,"divorce":self.gui_divorce,"cheque":self.gui_paycheque, 
                           "charite":self.gui_charite,"opportunite":self.gui_liste_opportunite,
                           "reduction_de_taille":self.gui_reduction_taille,"marche":self.gui_marche,
                           "une_opportunite":self.gui_opportunite,"doodad":self.gui_doodad}
        #return {"bebe":self.gui_bebe,"charite":self.gui_charite,"divorce":self.gui_divorce,"opportunite":self.gui_liste_opportunite}

    def affiche_jeu(self):
        self.espaces.show()
        
    def cle_carte(self):
        liste_cle = []
        for ele in self.rate_race:
            liste_cle.append(ele[4])
        return liste_cle
        #return ["reduction_de_taille","reduction_de_taille","reduction_de_taille","reduction_de_taille","reduction_de_taille","reduction_de_taille","reduction_de_taille","reduction_de_taille","reduction_de_taille","reduction_de_taille","reduction_de_taille","reduction_de_taille"]
        
    def init_espace(self):
        self.rate_race = [[650,570,21,21,"cheque"],[610,560,21,21,"opportunite"],[580,540,21,21,"doodad"],[560,520,21,21,'opportunite'],[540,490,21,21,"bebe"],[530,460,21,21,"opportunite"],[530,420,21,21,"marche"],[540,390,21,21,"opportunite"],[560,360,21,21,"cheque"],[580,340,21,21,"opportunite"],[610,320,21,21,"marche"],[640,310,21,21,"opportunite"],
                          [680,310,21,21,"doodad"],[710,320,21,21,"opportunite"],[740,340,21,21,'bebe'],[770,360,21,21,"opportunite"],[780,390,21,21,"cheque"],[790,420,21,21,"opportunite"],[790,460,21,21,"marche"],[780,490,21,21,"opportunite"],[770,520,21,21,"doodad"],[740,540,21,21,"opportunite"],[710,560,21,21,"reduction_de_taille"],[680,570,21,21,"opportunite"]]
        self.fast_track = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    def modifi_dashboard(self):
        if self.peut_afficher_dash:
            self.affiche_dashboard()
        else:
            self.efface_dashboard()
    
    def deplace_pion(self,position =None):
        if position != None:
            #self.gui_rolldice.affiche()
            self.efface_dashboard()
            self.Pion.move(self.rate_race[position][0],self.rate_race[position][1])
            #sleep(0.8)
        else:
            #self.gui_rolldice.affiche()
            self.efface_dashboard()
            #self.Pion.move(self.rate_race[position][0],self.rate_race[position][1])
            self.Pion.move(self.rate_race[self.pion.numero_position][0],self.rate_race[self.pion.numero_position][1])
            #sleep(0.8)
            #numero_position
            #self.Pion.move(self.rate_race[self.pion.position()][0],self.rate_race[self.pion.position()][1])

    def affiche_dashboard(self):
        self.dashboard.show()
        self.peut_afficher_dash = False
    
    def efface_dashboard(self):
        self.dashboard.hide()
        self.peut_afficher_dash = True
    
    
    def lancer_de(self):
        #lancement du de
        self.efface_dashboard()
        self.gui_rolldice.disparait()
        #autres actions
        self.joueur.lancer()
    #def lancer(self):
    #    self.lancer_de()
        
    def affiche_lancer(self):
        self.gui_rolldice.affiche()
    
    def connection_joueur(self,joueur = None):
        #fonction de lancer de dée
        self.joueur = joueur
    
    def actualisation_info(self):
        #-----------actualisation des informations du joueur--------------
        #extraction des donnees
        donnees = self.info_joueur.interface.donnes_info_joueur()
        #les trois widgets en listes des depenses entrees et responsabilite sont effacés 
        self.listWidget_depenses_2.clear()
        self.listWidget_entrees_2.clear()
        self.listWidget_responsabilites_2.clear()
        self.listWidget_investissements_2.clear()
        #puis elles sont actualisée
        self.actualisation_entre(donnees["investissement"],donnees["salaire"])
        self.actualisation_depenses(donnees["investissement"],donnees["loyer"],donnees["dettes"],donnees["nombre_bebe"])
        self.actualisation_investissement(donnees["investissement"])
        self.actualisation_responsabilite(donnees["investissement"],donnees["loyer"],donnees["dettes"],donnees["nombre_bebe"])
        # actualistaion du cash
        self.actualisation_cash(donnees["cash"])
        # actualisation du totale des depenses
        self.actualisation_depense_t(donnees["total_depenses"])
        # actualisation du total des entrees
        self.actualisation_entree_t(donnees["evolution"])#"total_entre"
        # actualisation du cheque de paie
        self.actualisation_cheque_de_paie(donnees["cheque_de_paie"])
        #actualisation de la barre de progression
        self.actulisation_barre_progression(donnees["evolution"])
        
    def actualisation_entre(self,liste_inv,salaire):
        #ajout du salaire
        self.listWidget_entrees_2.addItem("salaire : {} ".format(salaire))
        #ajout des investissements ayant un cashflow positifs dans la liste des entres
        self.listWidget_entrees_2.addItems([inv["nom"]+"        "+str(int(inv["cashflow"])) for inv in liste_inv if inv["cashflow"]>=0])#investissement
    
    
    def actualisation_depenses(self,liste_inv,loyer,dettes,bebe):
        #-----------actualisation de toutes les depenses-----------
        # ajout du loyer
        self.listWidget_depenses_2.addItem("loyer : "+str(int(loyer)))
        # ajout de la dettes
        self.listWidget_depenses_2.addItem("dettes : "+str(int(self.som_depense_dettes(dettes))))
        #ajout du nombre de bebe
        self.listWidget_depenses_2.addItem("nombre de bebe : "+str(bebe))
        # ajout des investisements ayant un cashflow negatif
        self.listWidget_depenses_2.addItems([inv["nom"]+"        "+str(inv["cashflow"]) for inv in liste_inv if inv["cashflow"]<0])
    
    def actualisation_investissement(self,liste_inv):
        #-----------actualistation de tout les investissements-----------
        self.listWidget_investissements_2.addItems([inv["nom"]+"        "+str(int(inv["cashflow"])) for inv in liste_inv])#investissement
    
    def actualisation_responsabilite(self,liste_inv,loyer,dettes,bebe):
        # ajout des investisements ayant un cashflow negatif
        self.listWidget_responsabilites_2.addItems([inv["nom"]+"        "+str(inv["cashflow"]) for inv in liste_inv if inv["cashflow"]<0])
        #ajout du loyer
        self.listWidget_responsabilites_2.addItem("loyer : "+str(int(loyer)))
        # ajout de la dettes
        self.listWidget_responsabilites_2.addItem("dettes : "+str(int(self.som_depense_dettes(dettes))))    
        #ajout du nombre de bebe
        self.listWidget_responsabilites_2.addItem("nombre de bebe : "+str(bebe))
        
    def affiche(self):
        self.affiche_jeu()

    def som_depense_dettes(self,dettes):
        #calcule de somme des acomptes d'une dette
        som = 0
        for dette in dettes:
            som += dette[1]
        return som
    
    def actualisation_cash(self,cash):
        translation = QtCore.QCoreApplication.translate
        #actualistion du cash avc conservation du style (translation)
        self.label_cash.setText(translation("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">"+ str(int(cash)) +"</span></p><p><br/></p></body></html>"))
    
    def actualisation_depense_t(self,cash):
        #actualisation du totale des depenses
        translation = QtCore.QCoreApplication.translate
        self.label_depenses.setText(translation("MainWindow", "<html><head/><body><p>"+str(int(cash))+"</p></body></html>"))
    
    def actualisation_cheque_de_paie(self,cash):
        #actualisation du totale des depenses
        translation = QtCore.QCoreApplication.translate
        self.label_paycheck.setText(translation("MainWindow", "<html><head/><body><p>"+str(int(cash))+"</p></body></html>"))
        
    def actualisation_entree_t(self,cash):
        #actualisation du totale des entres
        translation = QtCore.QCoreApplication.translate
        self.label_totalentrees.setText(translation("MainWindow", "<html><head/><body><p>"+str(int(cash))+"</p></body></html>"))

    def actulisation_barre_progression(self,proucentage):
        #actualistion de la progess barre
        self.progressBar_2.setProperty("value",proucentage)
                 
    
    def disparait(self):
        #disparition de l'espace
        self.espaces.hide()
    
    
    
if __name__=="__main__":
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    espace = igu_espacejeu(MainWindow)
    espace.affiche_jeu()
    sys.exit(app.exec_())


