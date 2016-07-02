# -*- coding: cp1252 -*-
# Datei:    abstraktefunktion.py
# Version:  1.1
# Datum:    29.11.2015, 05.02.2016
# Autor:    Ovidiu Tatar

class AbstrakteFunktion():
    def __init__(self):
        self.xVerschiebung = 0
        self.yVerschiebung = 0
        self.faktor = 1
        self.function = 0

    def setzeXVerschiebung(self, verschiebung):
        self.xVerschiebung = verschiebung

    def holeXVerschiebung(self):
        return self.xVerschiebung

    def setzeYVerschiebung(self, verschiebung):
        self.yVerschiebung = verschiebung

    def holeYVerschiebung(self):
        return self.yVerschiebung

    def setzeFaktor(self, faktor):
        self.faktor = faktor

    def holeFaktor(self):
        return self.faktor

    def holeY(self, x):
        pass

    def getFunction(self, function):
        return self.function
