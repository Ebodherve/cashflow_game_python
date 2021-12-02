#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import espace
#import player

from abc import ABC

class carte(ABC):
    def __init__(self,nom = None,position = None,description = None):
        self.nom = nom
        self.position = position
        self.description = description
    def connection_interface(self,iu = None):
        #methode de connection à un interface
        self.iu = iu
        
        
