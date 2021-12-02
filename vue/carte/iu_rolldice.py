from PyQt5 import QtCore

try:
    from model_cartes.m_rolldice import Ui_Frame
except ModuleNotFoundError:
    from vue.carte.model_cartes.m_rolldice import Ui_Frame
    

class igu_rolldice(Ui_Frame):
    def __init__(self,frame,lancer = None,payer = None,empreinter = None,dashboard = None):
        self.frame_princale = frame
        Ui_Frame.setupUi(self,self.frame_princale)
        self.connection_lancer(lancer)
        self.connection_payer(payer)
        self.connection_emprunter(empreinter)
        self.connection_dashboard(dashboard)
        self.positionne([960,240])
    
    def affiche(self):
    #affichage de l'interface de lancer
        self.frame_princale.show()
        try:
            self.dashboard.hide()
        except AttributeError:
            print("affichage du dashboard ")

    def disparait(self):
    #disparition de l'interface de lancer
        self.frame_princale.hide()

    def connection_lancer(self,lancer = None):
    #connection du lancer à l'interface de lancer
        if lancer !=None: 
            self.pushButton_rolldice.clicked.connect(lancer)
        else:
            self.pushButton_rolldice.clicked.connect(lambda : print("lancer du de "))

    def connection_emprunter(self,emprunter = None):
    #connection du lancer à l'interface d'empreint 
        if emprunter != None:
            self.pushButton_emprunter_rolldice.clicked.connect(emprunter)
        else:
            self.pushButton_emprunter_rolldice.clicked.connect(lambda : print("emprunt"))
    
    def connection_payer(self,payer):
    # connection du lancer à l'interface paiement
    # lorsqu'il veux payer ses dettes
        if payer != None:
            self.pushButton_payer_rolldice.clicked.connect(payer)
        else:
            self.pushButton_payer_rolldice.clicked.connect(lambda : print("payer"))

    def connection_dashboard(self,dashboard = None):
    #connection du lancer au dashbord pour qu'il puisse les 
        if dashboard != None:
            self.dashboard = dashboard
    
    def positionne(self,position):
        #positionnement du lancer à une position bien precise
        self.frame_princale.move(position[0],position[1])

if __name__ == "__main__":
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    espace = igu_rolldice(MainWindow)
    espace.affiche()
    sys.exit(app.exec_())
    


