##
from PyQt5.QtWidgets import QWidget

try :
    from model_cartes.m_charite import Ui_Frame
    from iu_carte import igu_carte
except:
    from vue.carte.model_cartes.m_charite import Ui_Frame
    from vue.carte.iu_carte import igu_carte

    
class igu_charite(Ui_Frame,igu_carte):
    def __init__(self,frame,lancer = None,dashboard = None):
        igu_carte.__init__(self,frame,lancer= lancer,dashboard=dashboard)
        Ui_Frame.setupUi(self,self.frame_principale)
        self.pushButton_donner_charite.clicked.connect(self.donner)
        self.pushButton_passer_charite.clicked.connect(self.passer)
        self.disparait()
    
    def donner(self):
        #methode qui s'exécute lorsque le choix est de donner  
        self.choix = True
        self.boucle = False
        self.disparait()
    
    def passer(self):
        #methode qui s'execute lorsque le choix est de ne pas donner(passer) 
        self.choix = False
        self.boucle = False
        self.disparait()
    
    
    def offre_charite(self):
        self.affiche()
        #while self.boucle:
        #    pass
        #return self.choix


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frame = QtWidgets.QFrame()
    charite1 = igu_charite(frame)
    charite1.offre_charite()
    sys.exit(app.exec_())

