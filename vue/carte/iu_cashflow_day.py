##
from PyQt5.QtWidgets import QWidget

try :
    from model_cartes.m_cashflow_day import Ui_Frame
    from iu_carte import igu_carte
except:
    from vue.carte.model_cartes.m_cashflow_day import Ui_Frame
    from vue.carte.iu_carte import igu_carte

    
class igu_cashflow_day(Ui_Frame,igu_carte):
    def __init__(self,frame,valider = None,passer =None,lancer = None):
        self.frame_principale = frame
        igu_carte.__init__(self,self.frame_principale,lancer=lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        self.pushButton_passer_cashflow_day_2.clicked.connect(lambda : self.passer())
            
    


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frame = QtWidgets.QFrame()
    charite1 = igu_cashflow_day(frame)
    charite1.offre_charite()
    sys.exit(app.exec_())

