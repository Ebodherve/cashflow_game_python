try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type


class imarche(interface_type):
    def __init__(self,marche = None):
        interface_type.__init__(self,marche)
        self.connection_interface(marche)


