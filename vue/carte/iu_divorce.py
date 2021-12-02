try:
    from model_cartes.m_divorce import Ui_Frame 
    from iu_carte import igu_carte
except:
    from vue.carte.model_cartes.m_divorce import Ui_Frame
    from vue.carte.iu_carte import igu_carte
    
    
class igu_divorce(Ui_Frame,igu_carte):
    def __init__(self,frame,dashboard = None,lancer = None):
        #self.frame_principale = frame
        igu_carte.__init__(self,frame,dashboard = dashboard,lancer = lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        self.pushButton_ok_divorce.clicked.connect(lambda : self.continuer())
        
        #self.disparait()
    
    def continuer(self):
        #methode permettant de continuer
        self.disparait()
    
    def message(self):
        #message affiché lors d'un divorce
        self.affiche()


