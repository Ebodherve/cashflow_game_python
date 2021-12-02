try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type


class ireve(interface_type):
    def __init__(self,reve = None):
        interface_type.__init__(self,reve)
        self.connection_interface(reve)

