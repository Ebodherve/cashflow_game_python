#from model.cartes_jeu.investissement import investissement

try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type

class i_investissement(interface_type):
    def __init__(self,invest = None):
        interface_type.__init__(self)#,investissement()
        self.connection_interface(invest)

    def cout_marcher(self):
        #acces au cout sur le marché
        return self.investissement.cout_marche

    def desription_invest(self):
        #acces à la description de l'investissement
        return self.investissement.description

    def somme_inest(self):
        #acces à la somme de paie 
        return self.investissement.somme
        


