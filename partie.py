#!/usr/bin/python
# -*- coding: UTF-8 -*-
from model import *
from vue import *
from time import time


class partie(object):
    def __init__(self,duree = 3600,controle = None):
        self.debut = None
        self.duree = duree
        self.fin = None
        self._appartient = []
        self._unnamed_espace_ = None
        self._unnamed_Class_ = None
        self.connection_controle(controle=controle)

    def demarrage(self):
        #demarrage de la partie (instanciation des autres objets du jeu)
        pass

    def quitter_save(self):
        pass

    def initialisation(self):
        pass

    def quitter(self):
        pass

    def continuer(self):
        pass

    def calcule_fin(self):
        return self.duree + self.debut

    def calcule_debut(self):
        return time()

    def connection_controle(self,controle = None):
        self.controle = controle




