try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type


class idoodad(interface_type):
    def __init__(self,doodad = None):
        interface_type.__init__(self,doodad)
        #self.connection_interface(doodad)
    
    def somme_doodad(self):
        #acces à la valeur de la somme d'une carte doodad 
        return self.doodad.somme    


