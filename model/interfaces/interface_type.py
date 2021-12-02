from abc import ABC

class interface_type(ABC):
    def __init__(self,objet_prive_defaut = None):
        # objet privé à interfacer par défaut lorsque 
        # l'objet de connection par défaut est None 
        #self.objet_prive = objet_prive_defaut
        self.connection_interface(objet_prive_defaut)
    def connection_interface(self,objet_prive = None):
        if objet_prive != None:
            try :
                del self.objet_prive
            except AttributeError:
                pass
            self.objet_prive = objet_prive
            self.objet_prive.interface = self
        else:
            pass
