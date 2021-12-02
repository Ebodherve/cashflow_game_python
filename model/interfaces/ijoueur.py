try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type

    

class ijoueur(interface_type):
    def __init__(self,joueur = None):
        interface_type.__init__(self,joueur)
        self.connecte_interface(joueur)
    
    def connection_iu_joueur(self,iu = None):
        self.joueur.connection_iu(iu)
    def connection_iu_info(self,iu = None):
        self.joueur.connection_iu(iu) 
        


