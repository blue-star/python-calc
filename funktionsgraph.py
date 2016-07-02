# -*- coding: cp1252 -*-
# Datei:    funktionsgraph.py
# Version:  1.8
# Datum:    01.12.2015, 31.01.2016, 05.02.2016, 27.02.2016
# Autor:    Ovidiu Tatar

from Tkinter import *

class Funktionsgraph(Canvas):
    def __init__(self, wertetabelle, parent):
        Canvas.__init__(self, parent)

        self.wertetabelle = wertetabelle
        self.wertetabelle.anmelden(self)
        
        self.bind("<MouseWheel>", self.zoom)
        self.bind("<Button-1>", self.focus)
        
        self.aktualisieren()

    def close(self):
        self.destroy()
        self.wertetabelle.abmelden(self)

    def focus(self, event = None):
        self.focus_set()

    def zoom(self, event = None):
        if event.delta < 0:
            if self.schrittweite < abs(min(self.wertetabelle.holeAnfang(), min(self.wertetabelle.holeFunktionswerte())) * 2):
                self.schrittweite *= 2.0
                self.anfang *= 2.0
        else:
            if self.schrittweite > 0.02:
                self.schrittweite /= 2.0
                self.anfang /= 2.0
        self.zeichnen()

    def aktualisieren(self):
        self.anfang = min(self.wertetabelle.holeAnfang(), min(self.wertetabelle.holeFunktionswerte()))
        self.schrittweite = abs(self.anfang) / 2
        
        self.zeichnen()

    def zeichnen(self):
        self.delete("all")
        w = int(self["width"])
        h = int(self["height"])

        self.create_line(0, h / 2, w, h / 2, fill = "black", width = 1)
        self.create_line(w / 2, 0, w / 2, h, fill = "black", width = 1)

        for i in range (0, 5):
            n = self.anfang + self.schrittweite * i
            if round(n, 3) != 0.0:
                self.create_line(w / 6 * (i + 1), h / 2 - 2, w / 6 * (i + 1), h / 2 + 3, fill = "black", width = 1)
                self.create_text(w / 6 * (i + 1), h / 2 + 10, text = round(n, 2))
                self.create_line(w / 2 - 2, h / 6 * (i + 1), w / 2 + 3, h / 6 * (i + 1), fill = "black", width = 1)
                self.create_text(w / 2 - 16, h / 6 * (i + 1), text = round(-n, 2))

        koords = []
        for koord in self.wertetabelle.holeKoordinaten():
            koords.append(w / 2 + koord[0] * w / 6.0 / self.schrittweite)
            koords.append(h / 2 + -koord[1] * h / 6.0 / self.schrittweite)
        
        self.create_line(*koords, fill = "red", width = 1)
