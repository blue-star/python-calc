# -*- coding: cp1252 -*-
# Datei:    wertetabelle.py
# Version:  1.2
# Datum:    01.12.2015
# Autor:    Ovidiu Tatar

from liniarefunktion import LiniareFunktion

class Wertetabelle():
    def __init__(self, funktion = LiniareFunktion(), anfang = -5, ende = 5, schrittweite = 1):
        self.schrittweite = schrittweite
        self.anfang = min(anfang, ende)
        self.ende = max(anfang, ende)
        self.funktion = funktion
        self.beobachter = []

    def setzeSchrittweite(self, schrittweite):
        if self.schrittweite != schrittweite:
            self.schrittweite = schrittweite
            self.benachrichtigen()

    def holeSchrittweite(self):
        return self.schrittweite
    
    def setzeAnfang(self, anfang):
        if self.anfang != anfang:
            self.anfang = anfang
            self.benachrichtigen()

    def holeAnfang(self):
        return self.anfang

    def setzeEnde(self, ende):
        if self.ende != ende:
            self.ende = ende
            self.benachrichtigen()

    def holeEnde(self):
        return self.ende

    def setzeFunktion(self, funktion):
        self.funktion = funktion
        self.benachrichtigen()

    def anmelden(self, beobachter):
        if not beobachter in self.beobachter:
            self.beobachter.append(beobachter)

    def abmelden(self, beobachter):
        if beobachter in self.beobachter:
            self.beobachter.remove(beobachter)
    
    def holeFunktionswerte(self):
        werte = []
        x = self.anfang
        while x <= self.ende:
            werte.append(self.funktion.holeY(x))
            x += self.schrittweite
        return werte
    
    def holeKoordinaten(self):
        koordinaten = []
        x = self.anfang
        while x <= self.ende:
            koordinaten.append((x, self.funktion.holeY(x)))
            x += self.schrittweite
        return koordinaten

    def benachrichtigen(self):
        for beobachter in self.beobachter:
            try:
                beobachter.aktualisieren()
            except:
                self.abmelden(beobachter)
                print beobachter, "konnte nicht aktualisiert werden und wurde aus der Beobachterliste entfernt!"
            
