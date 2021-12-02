######
try:
    from model_cartes.m_doodad import Ui_Frame 
    from iu_carte import igu_carte
except:
    from vue.carte.model_cartes.m_doodad import Ui_Frame
    from vue.carte.iu_carte import igu_carte
    


class igu_doodad(Ui_Frame,igu_carte):
    def __init__(self,frame,dashboard=None,lancer = None):
        igu_carte.__init__(self,frame,dashboard= dashboard,lancer= lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        self.disparait()
        self.pushButton_payer_doodad.clicked.connect(self.disparait)
        
    def evenement(self,action = None,somme =0,description = None):
        self.label_doodad.setText(description+str(somme))
        self.pushButton_payer_doodad.clicked.connect(action)
        self.affiche()
    
    def propose_de_faire_un_pret(self,somme = 0,action = None):
        self.label_doodad.setText("vous n'avez pas assez de cash faites un pret de :"+str(somme))
        self.pushButton_payer_doodad.clicked.connect(action)
        


