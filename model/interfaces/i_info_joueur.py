try:
    from model.interfaces.interface_type import interface_type
except:
    from interfaces.interface_type import interface_type


class i_info_joueur:
    def __init__(self,info_joueur = None):
        self.connection_interface(info_joueur)
        #self.connection_interface(info_joueur)
        #self.connection_inteface(info_joueur)
    def connection_interface(self,info_joueur):
        self.info_joueur = info_joueur
        self.info_joueur.interface = self
    def donnes_info_joueur(self):
        #differentes informations sur le profil du joueur
        evolution =( 100*int((self.info_joueur.revenu_passif)/(self.info_joueur.total_depenses)))%99
        return {"nom":self.info_joueur.nom,
                "salaire":self.info_joueur.salaire,
                "cash":self.info_joueur.cash,
                "economies":self.info_joueur.economies,
                "loyer":self.info_joueur.loyer,
                "depense":self.info_joueur.liste_depense,
                "cheque_de_paie":self.info_joueur.cheque_de_paie,
                "dettes":self.info_joueur.dettes,
                "investissement":self.info_joueur.investissement,
                "total_entre":self.info_joueur.total_entrees,
                "nombre_bebe":self.info_joueur.nb_bebe,
                "total_depenses":self.info_joueur.total_depenses,
                "revenu_passif":self.info_joueur.revenu_passif,
                "evolution":evolution}
                #{100*int((self.info_joueur.revenu_passif)//(self.info_joueur.total_depenses))}

#100*int(int(self.info_joueur.revenu_passif)//int(self.info_joueur.total_depenses))

