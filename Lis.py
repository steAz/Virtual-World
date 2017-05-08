import random
from Zwierze import Zwierze
from Organizm import Organizm

WIELKOSC_PLANSZY = 2022

class Lis(Zwierze):
    def __init__(self, x, y, sila, inicjatywa, znaczek):
        self.x = x;
        self.y = y
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._znak = znaczek
        self._wiek = 1
        self._czyRozmnazac = False


    def czyObokSilniejszyPrzeciwnik(self, swiat, kierunek, dx, dy):
        for i in range(WIELKOSC_PLANSZY + 1):
            if swiat.organizmy[i].podajWiek() >= 1:
                if self.podajSile() < swiat.organizmy[i].podajSile():
                    if (self.x + dx == swiat.organizmy[i].x) and (self.y + dy == swiat.organizmy[i].y):
                        return True

        return False


    def idz(self, swiat, kierunek, dx, dy):
        self.kierunek = kierunek

        if self.czyMozeIsc(swiat, dx, dy) == True:
            if(self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                self._poprzednieX = self.x
                self._poprzednieY = self.y

                self._czyRozmnazac = False
                self.x += dx
                self.y += dy

        elif self.czyMozeIsc(swiat, dx, dy) == False:
            self._czyRozmnazac = True


    def akcja(self, swiat, kierunek):
        losuj = random.randint(0, 3)

        if losuj == 0:
            if self.czyObokSilniejszyPrzeciwnik(swiat, kierunek, 0, -1) == False:
                self.idz(swiat, Organizm.Kierunek.UP, 0, -1)

        if losuj == 1:
            if self.czyObokSilniejszyPrzeciwnik(swiat, kierunek, 0, 1) == False:
                self.idz(swiat, Organizm.Kierunek.UP, 0, 1)

        if losuj == 2:
            if self.czyObokSilniejszyPrzeciwnik(swiat, kierunek, 1, 0) == False:
                self.idz(swiat, Organizm.Kierunek.UP, 1, 0)

        if losuj == 3:
            if self.czyObokSilniejszyPrzeciwnik(swiat, kierunek, -1, 0) == False:
                self.idz(swiat, Organizm.Kierunek.UP, -1, 0)


