# -*- coding: cp1252 -*-
# Datei:    functions_gui.py
# Version:  1.3
# Datum:    01.12.2015, 31.01.2016, 05.02.2016, 24.02.2016, 25.02.2016
# Autor:    Lucas Voelz

from abstraktefunktion import AbstrakteFunktion
from cosinusfunktion import CosinusFunktion
from exponentialfunktion import ExponentialFunktion
from linearefunktion import LineareFunktion
from quadratischefunktion import QuadratischeFunktion
from sinusfunktion import SinusFunktion
from zufallsfunktion import ZufallsFunktion
from wertetabelle import Wertetabelle
from tabellenanzeige import TabellenAnzeige
from funktionsgraph import Funktionsgraph
from Tkinter import *
import tkMessageBox
import winsound
import math
import wave
import struct

class Functions_GUI(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry("700x350")
        self.resizable(0,0)
        
        self.title("Functions")

        self.eingabe = Frame(self, relief = SUNKEN, borderwidth = 2)
        self.eingabe.pack(side = BOTTOM, fill = BOTH, expand = 1, padx = 5)

        self.wertetabelle = Wertetabelle(LineareFunktion(), -100, 100, 1)

        self.tabelle = TabellenAnzeige(self.wertetabelle, self)
        self.tabelle.pack(side = LEFT, padx = 5)

        self.graph = Funktionsgraph(self.wertetabelle, self)
        self.graph.pack(side = RIGHT, padx = 5)

        vcmd = (self.register(self.pruefen_Zahl), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.la_anfang = Label(self.eingabe, text = "Intervalsbeginn:")
        self.la_anfang.grid(row = 0, column = 0, sticky = W)
        self.anfang = Entry(self.eingabe, width = 8, validate = "key", vcmd = vcmd)
        self.anfang.insert(0,"-100")
        self.anfang.grid(row = 0, column = 1, sticky = E, padx = 5, pady = 5)

        self.la_ende = Label(self.eingabe, text = "Intervalsende:")
        self.la_ende.grid(row = 1, column = 0, sticky = W)
        self.ende = Entry(self.eingabe, width = 8, validate = "key", vcmd = vcmd)
        self.ende.insert(0,"100")
        self.ende.grid(row = 1, column = 1, sticky = E, padx = 5, pady = 5)
        
        self.la_schrittweite = Label(self.eingabe, text = "Schrittweite:")
        self.la_schrittweite.grid(row = 0, column = 2, sticky = W)
        self.schrittweite = Entry(self.eingabe, width = 8, validate = "key", vcmd = vcmd)
        self.schrittweite.insert(0,"1")
        self.schrittweite.grid(row = 0, column = 3, sticky = E, padx = 5, pady = 5)

        self.la_faktor = Label(self.eingabe, text = "Faktor:")
        self.la_faktor.grid(row = 1, column = 2, sticky = W)
        self.faktor = Entry(self.eingabe, width = 8, validate = "key", vcmd = vcmd)
        self.faktor.insert(0,"1")
        self.faktor.grid(row = 1, column = 3, sticky = E, padx = 5, pady = 5)

        self.la_xVerschiebung = Label(self.eingabe, text = "Verschiebung (x-Achse):")
        self.la_xVerschiebung.grid(row = 0, column = 4, sticky = W)
        self.xVerschiebung = Entry(self.eingabe, width = 8, validate = "key", vcmd = vcmd)
        self.xVerschiebung.insert(0,"0")
        self.xVerschiebung.grid(row = 0, column = 5, sticky = E, padx = 5, pady = 5)

        self.la_yVerschiebung = Label(self.eingabe, text = "Verschiebung (y-Achse):")
        self.la_yVerschiebung.grid(row = 1, column = 4, sticky = W)
        self.yVerschiebung = Entry(self.eingabe, width = 8, validate = "key", vcmd = vcmd)
        self.yVerschiebung.insert(0,"0")
        self.yVerschiebung.grid(row = 1, column = 5, sticky = E, padx = 5, pady = 5)
        
        arten = ["linear", "quadratisch", "sinus", "cosinus", "exponential", "zufall", "frei"]
        self.la_art = Label(self.eingabe, text = "Funktionsart:")
        self.la_art.grid(row = 0, column = 6, sticky = W)
        self.art = StringVar()
        self.art.set(arten[0])
        self.op_art = apply(OptionMenu, (self.eingabe, self.art) + tuple(arten))
        self.op_art.grid(row = 0, column = 7, sticky = E, padx = 5, pady = 5)

        self.bu_uebernehmen = Button(self.eingabe, text = "anhören", command = self.anhoeren)
        self.bu_uebernehmen.grid(row = 1, column = 6, sticky = E, padx = 5, pady = 5)

        self.bu_uebernehmen = Button(self.eingabe, text = "übernehmen", command = self.uebernehmen)
        self.bu_uebernehmen.grid(row = 1, column = 7, sticky = E, padx = 5, pady = 5)

        self.funktion = Entry(self.eingabe, width = 8)
        self.funktion.grid(row = 0, column = 8)

    def pruefen_Zahl(self, d, i, P, s, S, v, V, W):
        try:
            P = float(P)
            return True
        except:
            return False

    def uebernehmen(self):
        self.wertetabelle.setzeAnfang(float(self.anfang.get()))
        self.wertetabelle.setzeEnde(float(self.ende.get()))
        if float(self.schrittweite.get()) <= 0:
            tkMessageBox.showwarning("Falsche Eingabe", "Die Schrittweite kann nicht kleiner oder gleich 0 sein!")
            return
        self.wertetabelle.setzeSchrittweite(float(self.schrittweite.get()))
        if self.art.get() == "linear":
            funktion = LineareFunktion()
        elif self.art.get() == "quadratisch":
            funktion = QuadratischeFunktion()
        elif self.art.get() == "sinus":
            funktion = SinusFunktion()
        elif self.art.get() == "cosinus":
            funktion = CosinusFunktion()
        elif self.art.get() == "exponential":
            funktion = ExponentialFunktion()
        elif self.art.get() == "zufall":
            funktion = ZufallsFunktion()
        elif self.art.get() == "frei":
            funktionen = FreieFunktion()
        else:
            funktion = LineareFunktion()
        funktion.setzeFaktor(float(self.faktor.get()))
        funktion.setzeXVerschiebung(float(self.xVerschiebung.get()))
        funktion.setzeYVerschiebung(float(self.yVerschiebung.get()))
        self.wertetabelle.setzeFunktion(funktion)

    def synthComplex(self, freq=[440],coef=[1], datasize=10000, fname="test.wav"):
        frate = 44100.00  
        amp=8000.0 
        sine_list=[]
        for x in range(datasize):
            samp = 0
            for k in range(len(freq)):
                samp = samp + coef[k] * math.sin(2*math.pi*freq[k]*(x/frate))
            sine_list.append(samp)
        wav_file=wave.open(fname,"w")
        nchannels = 1
        sampwidth = 2
        framerate = int(frate)
        nframes=datasize
        comptype= "NONE"
        compname= "not compressed"
        wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
        for s in sine_list:
            wav_file.writeframes(struct.pack('h', int(s*amp/2)))
        wav_file.close()

    def anhoeren(self):
        f = wave.open("function.wav", "w")
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(1000)
        f.setnframes(10000)
        f.setcomptype("NONE","not compressed")
        try:
            for y in self.wertetabelle.holeFunktionswerte():
                f.writeframes(struct.pack('h', int(y)))
        except:
            f.close()
        f.close()
        f = wave.open("function_sin.wav", "w")
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(1000)
        f.setnframes(10000)
        f.setcomptype("NONE","not compressed")
        try:
            for koord in self.wertetabelle.holeKoordinaten():
                f.writeframes(struct.pack('h', int(koord[1] * math.sin(koord[0]))))
        except:
            f.close()
        f.close()
        
        winsound.PlaySound("function.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

if __name__ == '__main__':
    dasFenster = Functions_GUI()

    mainloop()
