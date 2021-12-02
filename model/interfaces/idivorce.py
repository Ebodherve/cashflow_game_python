try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type



class idivorce(interface_type):
    def __init__(self,divorce = None):
        interface_type.__init__(self,divorce)
        self.connection_interface(divorce)


