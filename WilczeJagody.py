from Roslina import Roslina
from Organizm import Organizm

WIELKOSC_PLANSZY = 2022

class WilczeJagody(Roslina):
    def __init__(self, x, y, sila, inicjatywa, znaczek):
        self.x = x;
        self.y = y
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._znak = znaczek
        self._wiek = 1
        self._czyRozmnazac = False




