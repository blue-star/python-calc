# -*- coding: cp1252 -*-
# Datei:    freiefunktion.py
# Version:  1.0
# Datum:    02.07.2016
# Autor:    Lucas Voelz

import math
from abstraktefunktion import AbstrakteFunktion

##class FreieFunktion(AbstrakteFunktion):
##    def __init__(self):
##        AbstrakteFunktion.__init__(self)
##
##        slow = ['+', '-']
##        medium = ['*','/']
##        fast = ['sin', 'cos', 'ln', 'log']
##        veryfast = ['^', 'wurzel']
##        
##
##    def splitFunction(self, function):
##        for i in range (len(self.function.split(slow[0]))):
##            
##        self.function.split(slow[1])

class Funktionen():
    def __init__(self):
        kette = [1,2,3,4,5,6]
##        alle operatoren sind falsch, spaetere abfrage welcher richtig ist um
##        dann mit einer in range schleife zu gucken welcher true ist und den ausfuehren
        plus = False
        minus = False
        mal = False,
        geteilt = False
        
##        self.operatoren = ['+', plus, '-', minus, '*', mal, '/', geteilt]
##        self.operatorenAufuehren = [self.summeStart,
##                                    self.differenzStart,
##                                    self.produktStart,
##                                    self.divisionStart]
##        for i in range(len(self.operatoren)):
##            if die Stelle im String == self.operatoren[2i]:
##                self.operatoren[2i+1] = True
##                self.operatorenAufuehren[i]
        
    def summeStart(self,kette):
        return self.summiere(0,kette)
        
    def summiere(self,zwischensumme,kette):
        if kette == None:
            return 0
        return summiere(zwischensumme+kette.pop(0), kette)

    def differenzStart(self, kette):
        return self.differenziere(0, kette)

    def differienziere(self, zwischensumme, kette):
        if kette == None:
            return 0
        return differenziere(zwischensumme-kette.pop(0), kette)

    def produktStart(self, kette):
        return self.produkt(0, kette)

    def produkt(self,zwischensumme, kette):
        if kette == None:
            return 0
        return produkt(zwischensumme*kette.pop(0), kette)

    def divisionStart(self, kette):
        return self.dividiere(0, kette)

    def dividiere(self, zwischensumme, kette):
        if kette == None:
            return 0
        return dividiere(zwischensumme/kette.pop(0), kette)
