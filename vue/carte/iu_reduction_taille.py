try:
    from model_cartes.m_reduction_de_taille import Ui_Frame
    from iu_carte import igu_carte
except ModuleNotFoundError:
    from vue.carte.model_cartes.m_reduction_de_taille import Ui_Frame
    from vue.carte.iu_carte import igu_carte

from PyQt5 import QtCore, QtGui, QtWidgets
    
class igu_reduction_taille(Ui_Frame,igu_carte):
    def __init__(self,frame,dashboard = None,lancer = None):
        #self.boucle = True
        igu_carte.__init__(self,frame,dashboard = dashboard,lancer=lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        #self.joindre()
        self.pushButton_reduction_taille.clicked.connect(lambda : self.disparait())
        self.disparait()
        
    def previent_perte(self):
        self.affiche()
        

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    pours = igu_reduction_taille(Frame)
    pours.previent_perte()
    sys.exit(app.exec_())



