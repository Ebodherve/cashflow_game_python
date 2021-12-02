try:
    from model_cartes.m_opportunite1 import Ui_Frame
    from iu_carte import igu_carte
except ModuleNotFoundError:
    from vue.carte.model_cartes.m_opportunite1 import Ui_Frame
    from vue.carte.iu_carte import igu_carte

from PyQt5 import QtCore, QtGui, QtWidgets
    
class igu_l_opportunite(Ui_Frame,igu_carte):
    def __init__(self,frame,dashboard = None,lancer = None):
        #self.boucle = True
        igu_carte.__init__(self,frame,dashboard = dashboard,lancer = lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        #self.joindre()
        self.disparait()
        
    def propose_type_opportunite(self,petite,grande):
        self.pushButton_petites_opp.clicked.connect(petite)
        self.pushButton_grandes_opp.clicked.connect(grande)
        self.affiche()
        
    def passer(self):
        self.disparait()
        self.lancer.disparait()

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    opp1 = igu_l_opportunite(Frame)
    opp1.propose_type_opportunite(lambda:print("petite"),lambda : print("grande"))
    sys.exit(app.exec_())





