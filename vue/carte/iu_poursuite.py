try:
    from model_cartes.m_poursuite import Ui_Frame
    from iu_carte import igu_carte
except ModuleNotFoundError:
    from vue.carte.model_cartes.m_poursuite import Ui_Frame
    from vue.carte.iu_carte import igu_carte

from PyQt5 import QtCore, QtGui, QtWidgets
    
class igu_proces(Ui_Frame,igu_carte):
    def __init__(self,frame,lancer = None,dashboard = None):
        #self.boucle = True
        igu_carte.__init__(self,frame,lancer = lancer,dashboard= dashboard )
        Ui_Frame.setupUi(self,self.frame_principale)
        #self.joindre()
        self.pushButton_ok_poursuite.clicked.connect(lambda : self.disparait())
        self.disparait()
        
    def message(self):
        self.affiche()
        

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    pours = igu_proces(Frame)
    pours.message()
    sys.exit(app.exec_())



