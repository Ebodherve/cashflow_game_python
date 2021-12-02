try:
    from model_cartes.m_controle_fiscale import Ui_Frame 
    from iu_carte import igu_carte
except:
    from vue.carte.model_cartes.m_controle_fiscale import Ui_Frame
    from vue.carte.iu_carte import igu_carte
    


class igu_contole_fiscale(Ui_Frame,igu_carte):
    def __init__(self,frame,dashboard = None,lancer = None):
        igu_carte.__init__(self,frame,dashboard=dashboard,lancer=lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        self.pushButton_ok_fiscalite.clicked.connect(self.passer)
    
    def continuer(self):
        #methode permettant de continuer
        self.disparait()
    
    def message(self):
        #message affiché lors d'un divorce
        self.affiche()
        







