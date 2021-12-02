try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type


class igrandes_opportunite(interface_type):
    def __init__(self,grande_opportunite = None):
        interface_type.__init__(self,grande_opportunite)
        self.connection_interface(objet_prive = grande_opportunite)


