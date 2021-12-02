
try:
    from model_cartes.m_investissement import Ui_Frame
    from iu_carte import igu_carte
except ModuleNotFoundError:
    from vue.carte.model_cartes.m_investissement import Ui_Frame
    from vue.carte.iu_carte import igu_carte

from PyQt5 import QtCore, QtGui, QtWidgets
    
class igu_investissement(Ui_Frame,igu_carte):
    def __init__(self,frame,lancer = None,dashboard = None):
        #self.boucle = True
        igu_carte.__init__(self,frame,lancer = lancer,dashboard= dashboard)
        Ui_Frame.setupUi(self,self.frame_principale)
        #self.joindre()
        self.pushButton_passer_investissement.clicked.connect(lambda : self.disparait())
        self.disparait()
        
    def demande_dachat(self,achat):
        self.affiche()
        self.pushButton_achetez_investissement.show()
        #connection du joueur à sa fonction d'achat
        self.pushButton_achetez_investissement.clicked.connect(achat)
        
    def pas_de_cash(self):
        self.label_investissement.setText("VOUS N'AVEZ PAS ASSER DE CASH POUR ACHETER CETTE INVESTISSEMENT")
        self.pushButton_achetez_investissement.hide()
    
    def passer(self):
        self.disparait()

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    bebe1 = igu_investissement(Frame)
    bebe1.demande_dachat(lambda:print(12))
    sys.exit(app.exec_())

