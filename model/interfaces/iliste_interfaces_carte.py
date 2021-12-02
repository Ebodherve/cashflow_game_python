try:
    from interfaces.i_investissement import i_investissement
    from interfaces.icharite import icharite
    from interfaces.icheque_de_paie import  icheque_de_paie
    from interfaces.icontrole_fiscale import icontrole_fiscale
    from interfaces.idivorce import idivorce
    from interfaces.idoodad import idoodad
    from interfaces.iespace import iespace
    from interfaces.imarche import imarche
    from interfaces.iopportunite import iopportunite
    from interfaces.iproces import iproces
    from interfaces.ireduction_taille import ireduction_taille
    from interfaces.ireve import ireve
except:
    from model.interfaces.i_investissement import i_investissement
    from model.interfaces.icharite import icharite
    from model.interfaces.icheque_de_paie import  icheque_de_paie
    from model.interfaces.icontrole_fiscale import icontrole_fiscale
    from model.interfaces.idivorce import idivorce
    from model.interfaces.idoodad import idoodad
    from model.interfaces.iespace import iespace
    from model.interfaces.imarche import imarche
    from model.interfaces.iopportunite import iopportunite
    from model.interfaces.iproces import iproces
    from model.interfaces.ireduction_taille import ireduction_taille
    from model.interfaces.ireve import ireve

class liste_interfaces_cartes:
    def __init__(self):
        pass
    def liste_int_cartes():
        int_investissement = i_investissement()
        int_icharite = icharite()
        int_icheque_de_paie = icheque_de_paie()
        int_icontrole_fiscale = icontrole_fiscale()
        int_idivorce = idivorce()
        int_idoodad = idoodad()
        int_iespace = iespace()
        int_imarche = imarche()
        int_iopportunite = iopportunite()
        int_iproces = iproces
        int_ireduction_taille = ireduction_taille()
        int_ireve = ireve()
        return {"reve":int_ireve,"controle_fiscale":int_icontrole_fiscale,"proces":int_iproces,"divorce":int_idivorce,"doodad":int_idoodad,"cheque":int_icheque_de_paie,"investissement":int_investissement,"charite":int_icharite,"opportunite":int_iopportunite,"reduction_taille":int_ireduction_taille,"marche":int_imarche}



