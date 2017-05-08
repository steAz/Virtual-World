import random
from Roslina import Roslina

class Mlecz(Roslina):
    def __init__(self, x, y, sila, inicjatywa, znaczek):
        self.x = x;
        self.y = y
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._znak = znaczek
        self._wiek = 1
        self._czyRozmnazac = False


    def akcja(self, swiat, kierunek):
        for i in range(3):
            procent = random.randint(1, 100)
            prawdopodobienstwo = random.randint(1, 15)

            if procent < prawdopodobienstwo:
                losuj = random.randint(0, 7)

                if losuj == 0:
                    dx = 1
                    dy = 0
                    if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                        swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())

                elif losuj == 1:
                    dx = 1
                    dy = -1

                    if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                        swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())

                elif losuj == 2:
                    dx = 0
                    dy = -1

                    if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                        swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())

                elif losuj == 3:
                    dx = -1
                    dy = -1

                    if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                        swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())

                elif losuj == 4:
                    dx = -1
                    dy = 0

                    if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                        swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())

                elif losuj == 5:
                    dx = -1
                    dy = 1

                    if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                        swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())

                elif losuj == 6:
                    dx = 0
                    dy = 1

                    if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                        swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())

                elif losuj == 7:
                    dx = 1
                    dy = 1

                    if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                        swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())


