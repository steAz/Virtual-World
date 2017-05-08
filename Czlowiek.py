import random
from Zwierze import Zwierze
from Organizm import Organizm

class Czlowiek(Zwierze):
    kierunek = Organizm.Kierunek

    def __init__(self, x, y, sila, inicjatywa, znaczek):
        self.x = x;
        self.y = y
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._znak = znaczek
        self._wiek = 1
        self.ustawCzySzybkAntylopyON(False)
        self.ustawCzyMoznaWlSpecjUm(True)
        self.ustawIloscTurOdSpecjUm(0)
        self._czyRozmnazac = False


    def idz(self, swiat, kierunek, dx, dy):
        procent = random.randint(0, 100)

        self.kierunek = kierunek

        if kierunek == Organizm.Kierunek.UP:
            dy = -1

            if self.podajCzySzybkoscAntylopyON():
                dy = -2

                if self.podajIloscTurOdSpecjUm() >= 3:
                    if procent < 50: dy = -1
                    else: dy = -2

        if kierunek == Organizm.Kierunek.DOWN:
            dy = 1

            if self.podajCzySzybkoscAntylopyON():
                dy = 2

                if self.podajIloscTurOdSpecjUm() >= 3:
                    if procent < 50: dy = 1
                    else: dy = 2

        if kierunek == Organizm.Kierunek.RIGHT:
            dx = 1

            if self.podajCzySzybkoscAntylopyON():
                dx = 2

                if self.podajIloscTurOdSpecjUm() >= 3:
                    if procent < 50: dx = 1
                    else: dx = 2

        if kierunek == Organizm.Kierunek.LEFT:
            dx = -1

            if self.podajCzySzybkoscAntylopyON():
                dx = -2

                if self.podajIloscTurOdSpecjUm() >= 3:
                    if procent < 50: dx = -1
                    else: dx = -2
        
        if(self.czySciana(swiat, self.x + dx, self.y + dy) == False):
            self._poprzednieX = self.x
            self._poprzednieY = self.y

            self._czyRozmnazac = False
            self.x += dx
            self.y += dy

    
    def akcja(self, swiat, kierunek):
        self.idz(swiat, kierunek, 0, 0)
        


