try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type


class ipion(interface_type):
    def __init__(self,pion):
        interface_type.__init__(self,pion)
        self.connection_interface(pion)


