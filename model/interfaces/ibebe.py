try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type

class ibebe(interface_type):
    def __init__(self,bebe = None):
        interface_type.__init__(self,bebe)
        self.connection_interface(objet_prive=bebe)

