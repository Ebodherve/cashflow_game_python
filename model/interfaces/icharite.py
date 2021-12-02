
try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type
    

class icharite(interface_type):
    def __init__(self,charite = None):
        interface_type.__init__(self,charite)
        self.connection_interface(charite)
    


