try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type
    

class icheque_de_paie(interface_type):
    def __init__(self,chp = None):
        interface_type.__init__(self)
        self.connection_interface(chp)


