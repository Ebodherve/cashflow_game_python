try:
    from model_cartes.m_login import Ui_Frame
except:
    from vue.carte.model_cartes.m_login import Ui_Frame


class igu_login(Ui_Frame):
    def __init__(self,frame):
        self.frame_principale = frame
        Ui_Frame.setupUi(self,self.frame_principale)
        #self.connection_quitter(lambda : self.frame_principale.close())
        self.disparait()
    
    def affiche(self):
        self.frame_principale.show()
        
    def connection_continuer(self,continuer):
        self.pushButton_commencer_login.clicked.connect(continuer)
    
    def disparait(self):
        self.frame_principale.hide()
        
    def affiche_autre_page(self,affichage):
        affichage.affiche()
        self.disparait() 









