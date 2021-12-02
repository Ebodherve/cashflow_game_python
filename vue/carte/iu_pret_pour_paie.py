try:
    from model_cartes.m_pret_pour_paie import Ui_Frame 
    from iu_carte import igu_carte
except:
    from vue.carte.model_cartes.m_pret_pour_paie import Ui_Frame
    from vue.carte.iu_carte import igu_carte


class igu_pret_pour_paie(Ui_Frame,igu_carte):
    #-----------class de pret pour payer apres une opportunite-----------
    # emprunt : fonction d'emprunt 
    # passer : fonction de passage pour ne preter
    def __init__(self,frame,emprunt = None,passer = None,lancer = None):
        #self.frame_principale = frame
        igu_carte.__init__(self,frame = frame,lancer=lancer)
        Ui_Frame.setupUi(self,self.frame_principale)
        self.connection_emprunt(emprunt)
        self.connection_lancer(passer)
        #disparition
        self.disparait()
        
    def connection_passage(self,passer = None):
        #connection à la fonction de passage
        if passer != None:
            self.pushButton_passer_emprunt.clicked.connect(passer)
        else:
            self.pushButton_passer_emprunt.clicked.connect(lambda : print("passage"))

    def connection_emprunt(self,emprunt = None):
        #connection à la fonction d'emprunt
        if emprunt != None:
            self.pushButton_emprunt_pour_achat.clicked.connect(emprunt)
        else:
            self.pushButton_emprunt_pour_achat.clicked.connect(lambda : print("emprunt"))
    
    def disparait(self):
        # redefinition de la methode de disparition
        #return super().disparait()
        self.frame_principale.hide()
    
    def affiche(self):
        #redefinition de methode d'affichage
        #return super().affiche()
        self.frame_principale.show()
