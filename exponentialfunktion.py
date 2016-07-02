# -*- coding: cp1252 -*-
# Datei:    exponentialfunktion.py
# Version:  1.0
# Datum:    24.02.2015
# Autor:    Ovidiu Tatar

from abstraktefunktion import AbstrakteFunktion

class ExponentialFunktion(AbstrakteFunktion):
    def __init__(self):
        AbstrakteFunktion.__init__(self)

    def holeY(self, x):
        return self.faktor ** (x - self.xVerschiebung) + self.yVerschiebung
