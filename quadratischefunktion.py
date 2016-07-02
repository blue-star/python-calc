# -*- coding: cp1252 -*-
# Datei:    quadratischefunktion.py
# Version:  1.0
# Datum:    29.11.2015
# Autor:    Ovidiu Tatar

from abstraktefunktion import AbstrakteFunktion

class QuadratischeFunktion(AbstrakteFunktion):
    def __init__(self):
        AbstrakteFunktion.__init__(self)

    def holeY(self, x):
        return self.faktor * (x - self.xVerschiebung) ** 2 + self.yVerschiebung
