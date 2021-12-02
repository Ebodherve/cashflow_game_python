
from PyQt5 import QtWidgets, QtCore

try:
    from model_cartes.m_opportunite2 import Ui_Frame 
    from iu_carte import igu_carte
    from iu_pret_pour_paie import igu_pret_pour_paie
except:
    from vue.carte.model_cartes.m_opportunite2 import Ui_Frame
    from vue.carte.iu_carte import igu_carte
    from vue.carte.iu_pret_pour_paie import igu_pret_pour_paie


class igu_opportunite(Ui_Frame,igu_carte):
    def __init__(self,frame,dashborad = None,lancer = None):
        #self.frame_principale = frame
        igu_carte.__init__(self,frame = frame,dashboard = dashborad,lancer = lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        #interface de pret pour la paie d'un 
        frame_paie = QtWidgets.QFrame(self.frame_principale)
        self.pret = igu_pret_pour_paie(frame = frame_paie,passer=lambda : self.passer())
        self.pushButton_passer_opp.clicked.connect(lambda : self.passer())
        
    def demande_dachat(self,achat = None):
        self.actualisation_info()
        self.affiche()
        if achat != None:
            self.pushButton_payer_opp.clicked.connect(achat)
        else:
            self.pushButton_payer_opp.clicked.connect(lambda : print("achat de l'opportunite"))
    
    def propose_pret_somme(self,empreint = None):
        #---------------proposition de pret-------------
        self.disparait()
        self.pret.connection_emprunt(emprunt=empreint)
        self.pret.affiche()
        
    def passer_pret(self):
        self.pret.disparait()
        self.affiche()
    
    def actualisation_info(self):
        donnees = self.opportunite.donnees_opportunite()
        
        self.actualisation_cout(donnees["prix"])
        self.actualisation_opportunite2(donnees["description"])
        self.actualisation_prixmarche(donnees["prix_marche"])
        self.actualisation_cashflow(donnees["cashflow"])
        
    def actualisation_opportunite2(self,text):
        translation = QtCore.QCoreApplication.translate
        self.label_opportunite2.setText(translation("Frame", text))
        
    def actualisation_prixmarche(self,text):
        translation = QtCore.QCoreApplication.translate
        self.label_prixmarche_opp2.setText(translation("Frame", "<html><head/><body><p><span style=\" font-weight:600;\">0 -"+ str(text) +"</span></p></body></html>"))
    
    def actualisation_cashflow(self,text):
        translation = QtCore.QCoreApplication.translate
        self.label_cashflow.setText(translation("Frame", "<html><head/><body><p><span style=\" font-weight:600;\">"+ str(text) +"</span></p></body></html>"))
    
    def actualisation_cout(self,text):
        translation = QtCore.QCoreApplication.translate
        self.label_cout_opp2.setText(translation("Frame", "<html><head/><body><p><span style=\" font-weight:600;\">"+ str(text) +"</span></p></body></html>"))
    
    def affiche(self):
        self.frame_principale.show()   

