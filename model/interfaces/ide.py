try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type

from model.de import de

class ide(interface_type):
    def __init__(self,de = None):
        interface_type.__init__(self,de)
        self.connection_interface(de)
    
    def face(self):
        #methode de retour d'une des faces du de 
        return self.de.retourner_resultat()


