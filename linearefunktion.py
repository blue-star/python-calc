# -*- coding: cp1252 -*-
# Datei:    linearefunktion.py
# Version:  1.0
# Datum:    29.11.2015
# Autor:    Ovidiu Tatar

from abstraktefunktion import AbstrakteFunktion

class LineareFunktion(AbstrakteFunktion):
    def __init__(self):
        AbstrakteFunktion.__init__(self)

    def setzeXVerschiebung(self, verschiebung):
        pass

    def holeXVerschiebung(self):
        return 0

    def holeY(self, x):
        return self.faktor * x + self.yVerschiebung
