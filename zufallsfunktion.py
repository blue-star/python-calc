# -*- coding: cp1252 -*-
# Datei:    zufallsfunktion.py
# Version:  1.0
# Datum:    06.02.2016
# Autor:    Ovidiu Tatar

import random
from linearefunktion import LineareFunktion

class ZufallsFunktion(LineareFunktion):
    def __init__(self):
        LineareFunktion.__init__(self)

    def holeY(self, x):
        return self.faktor * random.random() + self.yVerschiebung
