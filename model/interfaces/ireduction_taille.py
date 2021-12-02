try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type
 

class ireduction_taille(interface_type):
    def __init__(self,rtaille = None):
        interface_type(self)
        self.connection_interface(rtaille)
