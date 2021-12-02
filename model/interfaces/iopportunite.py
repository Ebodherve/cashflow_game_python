try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type

class iopportunite(interface_type):
    def __init__(self,opportunite = None):
        interface_type.__init__(self,opportunite)
        self.connection_interface(opportunite)
    def donnees_opportunite(self):
        return {"nom":self.objet_prive.nom,"description":self.objet_prive.description,
                "cashflow":self.objet_prive.cashflow,"prix":self.objet_prive.prix,"prix_marche":self.objet_prive.prix_marche}

