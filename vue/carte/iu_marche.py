
try:
    from model_cartes.m_marche import Ui_Frame
    from iu_carte import igu_carte
except ModuleNotFoundError:
    from vue.carte.model_cartes.m_marche import Ui_Frame
    from vue.carte.iu_carte import igu_carte

from PyQt5 import QtCore, QtGui, QtWidgets
    
class igu_marche(Ui_Frame,igu_carte):
    def __init__(self,frame,dashboard = None,lancer = None):
        #self.boucle = True
        igu_carte.__init__(self,frame,dashboard = dashboard,lancer = lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        #self.joindre()
        self.pushButton_passer_marche.clicked.connect(lambda : self.passer())
        self.disparait()
        
    def propose(self,achat_joueur,investissement):
        #modificaton du libelé des investissements
        self.affiche_investissement(investissement)  
        #affichage de la carte
        self.affiche()
        #affichage du button de vente car il etre en etat no affiche
        self.pushButton_vendre_marche.clicked.connect(achat_joueur)
        
    def affiche_investissement(self,investissement = "VENDRE CETTE INVESTISSEMENT !"):
        self.label_marche.setText(investissement)
                
    def pas_dinvestissement(self):
        self.affiche()
        #disparition du bouton de vente
        self.pushButton_vendre_marche.hide()
        self.label_marche.setText("VOUS N'AVEZ PAS D'INVESTISSEMENT")
        
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    bebe1 = igu_marche(Frame)
    bebe1.propose(lambda:print(12),"bonjour")
    sys.exit(app.exec_())

