# -*- coding: cp1252 -*-
# Datei:    tabellenanzeige.py
# Version:  1.6
# Datum:    30.11.2015, 24.02.2016
# Autor:    Ovidiu Tatar

from Tkinter import *

class TabellenAnzeige(Frame):
    def __init__(self, wertetabelle, parent):
        Frame.__init__(self, parent)

        self.wertetabelle = wertetabelle
        self.wertetabelle.anmelden(self)

        self.scrollbar = Scrollbar(self, orient = VERTICAL, command = self.scroll)
        self.xBox = Listbox(self, selectbackground = "gray", yscrollcommand = self.yBoxScroll, width = 15, selectmode=SINGLE)
        self.yBox = Listbox(self, selectbackground = "gray", yscrollcommand = self.xBoxScroll, width = 15, selectmode=SINGLE)

        Label(self, text = "x").grid(column = 0, row = 0)
        Label(self, text = "y").grid(column = 1, row = 0)
        self.xBox.grid(column = 0, row = 1)
        self.yBox.grid(column = 1, row = 1)
        self.scrollbar.grid(column = 2, row = 1, sticky = W + N + S)

        self.aktualisieren()

    def close(self):
        self.destroy()
        self.wertetabelle.abmelden(self)

    def xBoxScroll(self, *args):
        self.xBox.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yBoxScroll(self, *args):
        self.yBox.yview_moveto(args[0])
        self.scrollbar.set(*args)
    
    def scroll(self, *args):
        self.xBox.yview(*args)
        self.yBox.yview(*args)

    def aktualisieren(self):
        self.xBox.delete(0, END)
        self.yBox.delete(0, END)
        
        index = 0
        for koord in self.wertetabelle.holeKoordinaten():
            self.xBox.insert(index, koord[0])
            self.yBox.insert(index, koord[1])

            index += 1
