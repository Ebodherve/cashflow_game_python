try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type



class ibanque(interface_type):
    def __init__(self,banque = None):
        interface_type.__init__(self,banque)
        self.connection_interface(banque)

