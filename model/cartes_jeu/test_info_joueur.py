#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import player
#
#nom                                : nom du joueur
#sal (salaire)                      : salaire du joueur
#cash                               : cash du joueur 
#econo (economies)                  : economies du joueur
#loyer                              : loyer
#t_dp (depenses)                    : somme correspondante à la valeur total des depenses t_dp = somme de toute les depenses
#t_ent (total_entrees)              : somme correspondante à la valeur total des entreés t_ent
#dt (dette)                         : liste contenant de dictionnaires d'éléments contenants la somme totale du pret et le taux d'interet ainsi que l'acompte
#(r_pas)revenu_passif               : revenu passif
#
#
#
#
#
#



class info_joueur(object):
    def __init__(self,nom = "",sal = 50,cash = 1000,econo = 50,loyer = 10,ent = 0,chp = 50,dt = [],invest = [],bb = 0,t_dp = 10,liste_depense = [],r_pas = 0,iu = None):
        self.connection_iu(iu)
        t_ent = sal #le totale des entres est le salaire à l'initialisation du jeu
        t_dp = loyer # calule des depenses au debut du jeu
        self.actualisation_profil(nom,sal,cash,econo,loyer,ent,chp,dt,invest,t_ent,bb,t_dp,liste_depense,r_pas)
        
    def connection_iu(self,iu = None):
        if iu == None:
            self.iu = iu_info_joueur(self)
        else:
            self.iu = iu
        
    def ajout_investissement(self,inv):
        #ajout de l'investissement  
        self.investissement.append(inv.sajouter_au_investissement())
        #augmentation du cheque de paie par le cashflow 
        self.cheque_de_paie += inv.cashflow 
        #actualisation des infos du joueur
        self.actualisation()
    
    def ajout_opportunite(self,opport):
        #ajout de l'opportunite aux investissements 
        self.investissement.append(opport.sajouter_au_opportunite())
        #actualisation des infos du joueur
        self.actualisation()

    def reduire_les_investissements(self,liste_invest):
        #reduction des investissements
        for inv in liste_invest:
            self.investissement.remove(inv)
        #actualisation des infos du joueur
        self.actualisation()
    
    def augmenter_les_entrees(self,cash):
        #augmeentation des revenu passif
        self.revenu_passif += cash
        #calcule à nouveau du total des entreés 
        self.calule_du_total_des_entres()
        #calcule à nouveau du cheque de paie
        self.calule_cheque_de_paie()
        #actualisation des infos du joueur
        self.actualisation()
    
    def calule_cheque_de_paie(self):
        #calule du cheque de paie
        self.cheque_de_paie = self.salaire + self.revenu_passif - self.total_depenses
        return self.cheque_de_paie
    
    def calule_du_total_des_entres(self):
        #calcule du total des entreés
        self.total_entrees = self.salaire + self.revenu_passif
        return self.total_entrees
    
    def augmentation_dette(self,somme = 0,interet = 0.1):
        #un pret s'effectu à la banque
        #puis la dette est conservée dans les infos du joueur
        #somme : somme preteé
        #interet : pourcentage d'interet
        somme += somme*interet
        #accompte : somme a payer pour chaque payday dans le compte du pret
        accompte = somme*0.1
        self.dettes.append([somme,accompte])
        #diminution du cheque de paie pour pouvoir payer la dette
        self.cheque_de_paie -= accompte 
        
    def diminution_dette_zero(self):
        self.diminution_cash(self.dettes[0][0])
        self.dettes.remove(self.dettes[0])

    def paie_des_dettes(self):
        #indice de position
        ind = 0
        #diminution des différentes dettes
        for dette in self.dettes:
            if dette[0]>0:
                #la dette est diminuer si elle n'est pas encore completement payée
                self.dettes[ind][0] -= self.dettes[ind][1]
                ind += 1
            else:
                #lorsque la dette a été payée son accompte s'arrete  
                self.cheque_de_paie += dette[1]
                #et elle est retirée des dettes
                self.dettes.remove(dette)
                    
    def ajout_cash(self,cash):
        #augementation du cash 
        self.cash += cash
    
    def multiplication_cash(self,nbr):
        #multiplication du cash du joueur par nbr
        self.cash *= nbr
        
    def augmentation_cash_depense(self,dp):
        #calcule des nouvelles depenses
        self.total_depenses += dp
        #calcule du nouveau cheque de paie
        self.cheque_de_paie -= dp
    
    def augmentation_depense(self,dp):
        #calcule des nouvelles depenses
        #self.depenses += dp
        #calcule du nouveau cheque de paie
        #self.cheque_de_paie -= dp
        pass
        
        
    def diminution_cash(self,cash):
        #diminution du cash d'une somme passé en parametre
        self.cash -= cash
        
        
    def actualisation(self):
        #actualisation d'une fenetre graphique par ses propres attributs (apres sa modification)
        self.actualisation_profil(self.nom,self.salaire,self.cash,self.economies,self.loyer,self.liste_entre,self.cheque_de_paie,
                                  self.dettes,self.investissement,self.total_entrees,self.nb_bebe,self.total_depenses,self.liste_depense,self.revenu_passif)
        self.iu.actualisation_info()
        
    
    def actualisation_profil(self,nom,sal,cash,econo,loyer,l_ent,chp,dt,invest,t_ent,bb,t_dp,l_dp,r_pas):
        self.nom = nom
        self.salaire = sal
        self.cash = cash
        self.economies = econo
        self.loyer = loyer
        self.liste_entre = l_ent
        self.cheque_de_paie = chp
        self.dettes = dt
        self.investissement = invest
        self.total_entrees = t_ent
        self.nb_bebe = bb
        self.total_depenses = t_dp
        self.liste_depense = l_dp
        self.revenu_passif = r_pas
        #le total des entrés doit etre calculé à chaque actualisation y compris le démarrrage 
        self.calule_du_total_des_entres()

class iu_info_joueur:
    def __init__(self,inf_j = None):
        if inf_j==None:
            self.info_joueur = info_joueur()
        else:
            self.info_joueur = inf_j
                    
    def actualisation_info(self):
        print("nom                  : ",self.info_joueur.nom)
        print("salaire              : ",self.info_joueur.salaire)
        print("cash                 : ",self.info_joueur.cash)
        print("economies            : ",self.info_joueur.economies)
        print("loyer                : ",self.info_joueur.loyer)
        print("depenses             : ",self.info_joueur.liste_depense)
        print("cheque de paie       : ",self.info_joueur.cheque_de_paie)
        print("dettes               : ",self.info_joueur.dettes)
        print("investissement       : ",self.info_joueur.investissement)
        print("total entrees        : ",self.info_joueur.total_entrees)
        print("nombre de bebe       : ",self.info_joueur.nb_bebe)
        print("total de depenses    : ",self.info_joueur.total_depenses)
        print("revenu passif        : ",self.info_joueur.revenu_passif)
        

if __name__=="__main__":
    inf = info_joueur()        
    inf.actualisation()

                
        

