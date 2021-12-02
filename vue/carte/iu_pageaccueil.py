try:
    from model_cartes.m_pageaccueil import Ui_Frame
except:
    from vue.carte.model_cartes.m_pageaccueil import Ui_Frame


class igu_pageaccueil(Ui_Frame):
    def __init__(self,frame):
        self.frame_principale = frame
        Ui_Frame.setupUi(self,self.frame_principale)
        #self.connection_quitter(lambda : self.frame_principale.close())
        self.disparait()
    
    def affiche(self):
        self.frame_principale.show()
    
    def connection_quitter(self,quitter):
        self.pushButton_quitter.cliked.connect(quitter)
    
    def disparait(self):
        self.frame_principale.hide()
    
    def connection_continuer(self,continuer):
        self.pushButton_quitter.clicked.connect(continuer)
    
    def affiche_autre_page(self,affiche):
        affiche.affiche()
        self.disparait()




