try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type
    

class icontrole_fiscale(interface_type):
    def __init__(self,controle = None):
        interface_type.__init__(self,controle)#,controle_fiscale()
        self.connection_interface(controle)

