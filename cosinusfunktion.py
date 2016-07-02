# -*- coding: cp1252 -*-
# Datei:    cosinusfunktion.py
# Version:  1.0
# Datum:    29.11.2015
# Autor:    Ovidiu Tatar

import math
from abstraktefunktion import AbstrakteFunktion

class CosinusFunktion(AbstrakteFunktion):
    def __init__(self):
        AbstrakteFunktion.__init__(self)

    def holeY(self, x):
        return self.faktor * math.cos((x - self.xVerschiebung)) + self.yVerschiebung
