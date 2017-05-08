import sys
import types
import pickle
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ZlyRozmiarPlanszy import ZlyRozmiarPlanszy
from Interfejs import Okno
from ZlyZnak import ZlyZnak
from Wilk import Wilk
from Czlowiek import Czlowiek
from Organizm import Organizm
from Lis import Lis
from Antylopa import Antylopa
from Owca import Owca
from Zolw import Zolw
from Trawa import Trawa
from Guarana import Guarana
from Mlecz import Mlecz
from WilczeJagody import WilczeJagody

WIELKOSC_PLANSZY = 2022

class Swiat:
    def __init__(self):
        self.czyCzlowiekZywy = True
        self.__tura = 0
        self.__zapamietanaTura = 0
        self.__szerokosc = 0
        self.__wysokosc = 0
        self.organizmy = {}  #Mozna tez tak : self.organizmy = []

        for i in range(WIELKOSC_PLANSZY + 1):    
            self.organizmy[i] = Organizm()   #Wtedy trzeba dodawac do listy na koniec appendem()
            self.organizmy[i].ustawWiek(0)

        self.dodajOrganizm(3, 8, "Wilk")
        self.dodajOrganizm(3, 6, "Lis")
        self.dodajOrganizm(3, 7, "Czlowiek")
        self.dodajOrganizm(2, 15, "Antylopa")
        self.dodajOrganizm(2, 18, "Owca")
        self.dodajOrganizm(15, 10, "Zolw")
        self.dodajOrganizm(0, 0, "Trawa")
        self.dodajOrganizm(13, 13, "Mlecz")
        self.dodajOrganizm(5, 5, "Guarana")
        self.dodajOrganizm(7, 15, "WilczeJagody")

    def weryfikacja(self, x, y):
        if x < 9 or y < 9:
            return False
        else:
            return True

    def zapiszDoPliku(self):
        plik = open("zapisany.txt", "wb")
        plik2 = open("zapisanySwiat.txt", "wb")
        pickle.dump(self.organizmy, plik)
        self.__zapamietanaTura = self.podajTure()
        

    def wczytajZpliku(self):
        plik = open("zapisany.txt", "rb")
        plik2 = open("zapisanySwiat.txt", "rb")
        self.organizmy = pickle.load(plik)
        self.__tura = self.__zapamietanaTura
        self.okno.wywolajCzyszczeniePlanszy()
        self.rysujOrganizmy()
        
        print("Aktualna tura: ", self.podajTure())

        if self.organizmy[WIELKOSC_PLANSZY].podajWiek() >= 1:
            print("Sila Czlowieka: ", self.organizmy[WIELKOSC_PLANSZY].podajSile())
        



    def ustawWymiarySwiata(self, szerokosc, wysokosc):
        self.__szerokosc = szerokosc
        self.__wysokosc = wysokosc


    def podajWysokosc(self):
        return self.__wysokosc

    
    def podajSzerokosc(self):
        return self.__szerokosc


    def menu(self, x, y):
        try:
            if self.weryfikacja(x, y) == False: raise ZlyRozmiarPlanszy('Plansza ma zly rozmiar')

            app = QApplication(sys.argv)
            okno = Okno(self, x, y)
            self.okno = okno;
            self.rysujOrganizmy()
            sys.exit(app.exec_())

        except ZlyRozmiarPlanszy:
            print("Wyjatek zlapany")


    def dodajOrganizm(self, x, y, znak):
        nrOrganizmu = (x * 100) + y

        try:
            if znak == "Wilk":
                organizm = Wilk(x, y, 9, 5, "Wilk")

            elif znak == "Czlowiek":
                organizm = Czlowiek(x, y, 5, 4, "Czlowiek")

            elif znak == "Lis":
                organizm = Lis(x, y, 3, 7, "Lis")

            elif znak == "Antylopa":
                organizm = Antylopa(x, y, 4, 4, "Antylopa")

            elif znak == "Owca":
                organizm = Owca(x, y, 4, 4, "Owca")

            elif znak == "Zolw":
                organizm = Zolw(x, y, 2, 1, "Zolw")

            elif znak == "Trawa":
                organizm = Trawa(x, y, 0, 0, "Trawa")

            elif znak == "Mlecz":
                organizm = Mlecz(x, y, 0, 0, "Mlecz")

            elif znak == "Guarana":
                organizm = Guarana(x, y, 0, 0, "Guarana")

            elif znak == "WilczeJagody":
                organizm = WilczeJagody(x, y, 99, 0, "WilczeJagody")

            else:
                raise ZlyZnak("Probujesz dodac organizm o nieprawidlowym znaku")
        except ZlyZnak:
            print("Wyjatek zlapany")
            return None

        if znak == "Czlowiek": organizm.ustawNumerOrganizmu(WIELKOSC_PLANSZY)
        else: organizm.ustawNumerOrganizmu(nrOrganizmu)

        organizm.ustawWiek(1)

        self.organizmy[organizm.podajNumerOrganizmu()] = organizm

        return organizm


    def rysujOrganizmy(self):
        for i in range(WIELKOSC_PLANSZY + 1):
            if self.organizmy[i].podajWiek() >= 1:
               self.okno.ustawPoleKratki(self.organizmy[i].x, self.organizmy[i].y, self.organizmy[i].podajZnak())

    
    def podajNajwiekszaInicjatywe(self):
        najwiekszaInicjatywa = 1
        czyPierwszaZnalezionaInicjatywa = True

        for i in range(WIELKOSC_PLANSZY + 1):
            if self.organizmy[i].podajWiek() >= 1:
                if czyPierwszaZnalezionaInicjatywa == True:
                    najwiekszaInicjatywa = self.organizmy[i].podajInicjatywe()
                    czyPierwszaZnalezionaInicjatywa = False

                if self.organizmy[i].podajInicjatywe() > najwiekszaInicjatywa:
                    najwiekszaInicjatywa = self.organizmy[i].podajInicjatywe()

        return najwiekszaInicjatywa


    def dodajWiek(self):
        for i in range(WIELKOSC_PLANSZY + 1):
            if self.organizmy[i].podajWiek() >= 1:
                self.organizmy[i].dodajWiek()

    
    def podajOrgOtejSamejInicjatywie(self, sprawdzanyOrganizm):
        for i in range(WIELKOSC_PLANSZY + 1):
            if self.organizmy[i].podajWiek() >= 1:
                if self.organizmy[i].podajZnak() != sprawdzanyOrganizm.podajZnak() and self.organizmy[i].podajZnak() != "Czlowiek":
                    if (self.organizmy[i].podajInicjatywe() == sprawdzanyOrganizm.podajInicjatywe()):
                        return self.organizmy[i]

        return None
              

    def podajTure(self):
        return self.__tura


    def dodajTure(self):
        self.__tura += 1


    def wykonajKolizje(self):
        for i in range(WIELKOSC_PLANSZY + 1):
            if self.organizmy[i].podajWiek() >= 1:
                if self.organizmy[i].podajCzyMoznaRozmnazac() == True:
                    self.organizmy[i].kolizja(self, True)
                else:
                    self.organizmy[i].kolizja(self, False)


    def wykonajTure(self, przycisk):
        if przycisk.key() == Qt.Key_Up: kierunekCzlowieka = Organizm.Kierunek.UP
        if przycisk.key() == Qt.Key_Down: kierunekCzlowieka = Organizm.Kierunek.DOWN
        if przycisk.key() == Qt.Key_Right: kierunekCzlowieka = Organizm.Kierunek.RIGHT
        if przycisk.key() == Qt.Key_Left: kierunekCzlowieka = Organizm.Kierunek.LEFT

        najwiekszaInicjatywa = self.podajNajwiekszaInicjatywe()

        i = 0
        while i < WIELKOSC_PLANSZY + 1:
            organizm = None
            
            if self.organizmy[i].podajWiek() >= 1:
                if najwiekszaInicjatywa == self.organizmy[i].podajInicjatywe():
                    if self.podajOrgOtejSamejInicjatywie(self.organizmy[i]) != None:
                        organizm = self.podajOrgOtejSamejInicjatywie(self.organizmy[i])

                        if organizm.podajWiek() > self.organizmy[i].podajWiek():
                            if isinstance(organizm, Czlowiek) == True:
                                if self.czyCzlowiekZywy == True:
                                    organizm.akcja(self, kierunekCzlowieka)
                                    self.organizmy[i].akcja(self, Organizm.Kierunek.LOSOWY)
                            else:
                                organizm.akcja(self, Organizm.Kierunek.LOSOWY)
                                self.organizmy[i].akcja(self, Organizm.Kierunek.LOSOWY)
                        else:
                            if isinstance(self.organizmy[i], Czlowiek) == True:
                                if self.czyCzlowiekZywy == True:
                                    self.organizmy[WIELKOSC_PLANSZY].akcja(self, kierunekCzlowieka)
                            else:
                                self.organizmy[i].akcja(self, Organizm.Kierunek.LOSOWY)

                    elif self.podajOrgOtejSamejInicjatywie(self.organizmy[i]) == None:
                            if isinstance(self.organizmy[i], Czlowiek) == True:
                                if self.czyCzlowiekZywy == True:
                                    self.organizmy[WIELKOSC_PLANSZY].akcja(self, kierunekCzlowieka)
                            else:
                                self.organizmy[i].akcja(self, Organizm.Kierunek.LOSOWY)

            czyPrzedluzyc = True
            if i == WIELKOSC_PLANSZY:
                najwiekszaInicjatywa -= 1

                if najwiekszaInicjatywa != -1:
                    i = 0
                    czyPrzedluzyc = False

            if czyPrzedluzyc == True:
                i += 1


        self.wykonajKolizje()
        self.dodajWiek()

        #SPECJALNA UMIEJETNOSC CZLOWIEK
        if self.organizmy[WIELKOSC_PLANSZY].podajWiek() >= 0:
            if self.organizmy[WIELKOSC_PLANSZY].podajCzySzybkoscAntylopyON() == True:
                self.organizmy[WIELKOSC_PLANSZY].dodajIloscTurOdSpecjUm()

                if self.organizmy[WIELKOSC_PLANSZY].podajIloscTurOdSpecjUm() >= 5:
                    self.organizmy[WIELKOSC_PLANSZY].ustawCzyMoznaWlSpecjUm(False)
                    self.organizmy[WIELKOSC_PLANSZY].ustawCzySzybkAntylopyON(False)
                    self.organizmy[WIELKOSC_PLANSZY].ustawIloscTurOdSpecjUm(0)

            elif (self.organizmy[WIELKOSC_PLANSZY].podajCzySzybkoscAntylopyON() == False) and (self.organizmy[WIELKOSC_PLANSZY].podajCzyMoznaWlSpecjUm() == False):
                self.organizmy[WIELKOSC_PLANSZY].dodajIloscTurOdSpecjUm()

                if self.organizmy[WIELKOSC_PLANSZY].podajIloscTurOdSpecjUm() >= 5:
                    self.organizmy[WIELKOSC_PLANSZY].ustawCzyMoznaWlSpecjUm(True)
                    self.organizmy[WIELKOSC_PLANSZY].ustawIloscTurOdSpecjUm(0)
        ##################################################
        
        self.okno.wywolajCzyszczeniePlanszy()
        self.dodajTure()

        print("Aktualna tura: ", self.podajTure())

        if self.organizmy[WIELKOSC_PLANSZY].podajWiek() >= 1:
            print("Sila Czlowieka: ", self.organizmy[WIELKOSC_PLANSZY].podajSile())


        self.rysujOrganizmy()
        