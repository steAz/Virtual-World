from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Plansza import Plansza
from Organizm import Organizm

WIELKOSC_PLANSZY = 2022

class Okno(QMainWindow):
    def __init__(self, swiat, szerokoscPlanszy, wysokoscPlanszy):
        szerokoscRamki = 900
        wysokoscRamki = 600
        self.swiat = swiat
        self.swiat.ustawWymiarySwiata(szerokoscPlanszy, wysokoscPlanszy)
        self.swiat.wysokosc = wysokoscPlanszy

        super(Okno, self).__init__() 

        self.setGeometry(50, 50, szerokoscRamki, wysokoscRamki)
        self.setWindowTitle("Michal Kazanowski 160512")
        self.setWindowIcon(QIcon('ziemia.gif'))
        self.plansza = Plansza(self, szerokoscRamki, wysokoscRamki, szerokoscPlanszy)
        self.setCentralWidget(self.plansza)
        self.show()


    def ustawPoleKratki(self, x, y, znak):
        self.plansza.ustawPoleTekstowe(self, x, y, znak)


    def wywolajCzyszczeniePlanszy(self):
        self.plansza.wyczyscPlansze(self)

    
    def keyPressEvent(self, przycisk):
        if przycisk.key() == Qt.Key_Up: self.swiat.wykonajTure(przycisk)
        if przycisk.key() == Qt.Key_Down: self.swiat.wykonajTure(przycisk)
        if przycisk.key() == Qt.Key_Right: self.swiat.wykonajTure(przycisk)
        if przycisk.key() == Qt.Key_Left: self.swiat.wykonajTure(przycisk)
        if przycisk.key() == Qt.Key_Escape: self.close()
        if przycisk.key() == Qt.Key_S: self.swiat.zapiszDoPliku()
        if przycisk.key() == Qt.Key_L: self.swiat.wczytajZpliku()
        if przycisk.key() == Qt.Key_X: 
            if self.swiat.organizmy[WIELKOSC_PLANSZY].podajWiek() >= 1:
                if self.swiat.organizmy[WIELKOSC_PLANSZY].podajCzyMoznaWlSpecjUm():
                    self.swiat.organizmy[WIELKOSC_PLANSZY].ustawCzySzybkAntylopyON(True)



