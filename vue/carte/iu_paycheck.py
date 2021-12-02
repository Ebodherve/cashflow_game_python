######
from PyQt5.QtWidgets import QWidget

try :
    from model_cartes.m_paycheck import Ui_Frame
    from iu_carte import igu_carte
except:
    from vue.carte.model_cartes.m_paycheck import Ui_Frame
    from vue.carte.iu_carte import igu_carte

    
class igu_paycheque(Ui_Frame,igu_carte):
    def __init__(self,frame,valider = None,dashboard = None,passer =None,lancer = None):
        self.frame_principale = frame
        igu_carte.__init__(self,self.frame_principale,lancer=lancer,dashboard= dashboard)
        Ui_Frame.setupUi(self,self.frame_principale)
        self.pushButton_passer_paycheck.clicked.connect(lambda : self.disparait())
    def demande_cheque_de_paie(self,paie):
        self.pushButton_valider_paycheck.clicked.connect(paie)
        self.affiche()
        
        
if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frame = QtWidgets.QFrame()
    paie = igu_paycheque(frame)
    paie.affiche()
    sys.exit(app.exec_())

