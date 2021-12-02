try:
    from cartes_jeu.grande_opportunite import grande_opportunite
    from cartes_jeu.petite_opportunite import petite_opportunite
except :
    from model.cartes_jeu.grande_opportunite import grande_opportunite
    from model.cartes_jeu.petite_opportunite import petite_opportunite


"""from cartes_jeu.grande_opportunite import grande_opportunite
from cartes_jeu.petite_opportunite import petite_opportunite
"""

class liste_opportunite:
    def __init__(self,iu = None):
        if iu == None:
            self.iu = iu_listeopportunite(self)
        else :
            self.iu = iu
            self.iu.liste_opportunite = self 
        self.grande_op = grande_opportunite()
        self.petite_op = petite_opportunite()
        
    def propose_type_opportunite(self,joueur):
        #interface de proposition d'un investissement 
        choix = self.iu.propose_type_opportunite()
        #chois d'un objet en fonction du choix de l'utilisateur
        if choix == "petite":
            self.petite_op.activation(joueur)
        else:
            self.grande_op.activation(joueur)
    def activation(self,joueur):
        self.propose_type_opportunite(joueur)
    def connection_interface(self,iu = None):
        if iu != None:
            self.iu = iu
            self.lopportunite = self
    def connection_gui(self,gui):
        self.petite_op.connection_gui(gui)
        self.grande_op.connection_gui(gui)
    
        

class ig_liste_opportunite(liste_opportunite):
    def __init__(self,iu = None):
        liste_opportunite.__init__(self)
        self.connection_interface(iu)
    def propose_type_opportunite(self,joueur):
        
        petite = lambda : self.petite_opp_(joueur)
        grande = lambda : self.grande_opp_(joueur)
        self.iu.propose_type_opportunite(petite,grande)
    def petite_opp_(self,joueur):
        self.iu.passer()
        self.petite_op.activation(joueur)
    def grande_opp_(self,joueur):
        self.iu.passer()
        self.grande_op.activation(joueur)

class iu_listeopportunite:
    def __init__(self,liste_opportunite = None):
        self.liste_oppotunite = liste_opportunite
    
    def propose_type_opportunite(self):
        print("carte - opportunite : ")
        choix = input("Faire un choix entre petite opportunite et grande (p pour petite) :")
        if choix == "p":return "petite"
        else :  return "grande" 
        
        
    
    
        


