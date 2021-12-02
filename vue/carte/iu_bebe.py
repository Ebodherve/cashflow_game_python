try:
    from model_cartes.m_bebe import Ui_Frame
    from iu_carte import igu_carte
except ModuleNotFoundError:
    from vue.carte.model_cartes.m_bebe import Ui_Frame
    from vue.carte.iu_carte import igu_carte

from PyQt5 import QtCore, QtGui, QtWidgets
    
class igu_bebe(Ui_Frame,igu_carte):
    def __init__(self,frame,dashboard = None,lancer = None):
        #self.boucle = True
        igu_carte.__init__(self,frame,dashboard=dashboard,lancer= lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        #self.joindre()
        self.pushButton_ok_bebe.clicked.connect(lambda : self.passer())
        self.disparait()
        #self.se_positionner()
        
    def averti_bebe(self):
        self.affiche()
        
    def pas_de_bebe(self):
        self.label_bebe.setText("VOUS N'AURREZ PAS DE BEBE")
        self.averti_bebe()


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    bebe1 = igu_bebe(Frame)
    bebe1.averti_bebe()
    sys.exit(app.exec_())



