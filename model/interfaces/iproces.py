try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type


class iproces(interface_type):
    def __init__(self,proces = None):
        interface_type.__init__(self,proces)
        self.connection_interface(proces)


