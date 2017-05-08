import random
from Zwierze import Zwierze
from Organizm import Organizm

WIELKOSC_PLANSZY = 2022

class Zolw(Zwierze):
    def __init__(self, x, y, sila, inicjatywa, znaczek):
        self.x = x;
        self.y = y
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._znak = znaczek
        self._wiek = 1
        self._czyRozmnazac = False

    def akcja(self, swiat, kierunek):
        losuj = random.randint(0, 3)
        procent = random.randint(1, 100)

        if procent < 25:
            if losuj == 0:
                self.idz(swiat, Organizm.Kierunek.UP, 0, 0)

            if losuj == 1:
                self.idz(swiat, Organizm.Kierunek.DOWN, 0, 0)

            if losuj == 2:
                self.idz(swiat, Organizm.Kierunek.RIGHT, 0, 0)

            if losuj == 3:
                self.idz(swiat, Organizm.Kierunek.LEFT, 0, 0)


    def kolizja(self, swiat, czyRozmnazac):
        if self.podajCzyMoznaRozmnazac() == True:
            losuj = 0

            if losuj == 0:
                dx = 1
                dy = 0
                if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                    swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())
                else:
                    losuj += 1

            if losuj == 1:
                dx = 1
                dy = -1

                if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                    swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())
                else:
                    losuj += 1

            if losuj == 2:
                dx = 0
                dy = -1

                if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                    swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())
                else:
                    losuj += 1

            if losuj == 3:
                dx = -1
                dy = -1

                if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                    swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())
                else:
                    losuj += 1

            if losuj == 4:
                dx = -1
                dy = 0

                if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                    swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())
                else:
                    losuj += 1

            if losuj == 5:
                dx = -1
                dy = 1

                if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                    swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())
                else:
                    losuj += 1

            if losuj == 6:
                dx = 0
                dy = 1

                if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                    swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())
                else:
                    losuj += 1

            if losuj == 7:
                dx = 1
                dy = 1

                if (self.czyZnalezionyOrgOtychWspol(swiat, self, dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy) == False):
                    swiat.dodajOrganizm(self.x + dx, self.y + dy, self.podajZnak())

        elif self.podajCzyMoznaRozmnazac() == False:
            for i in range(WIELKOSC_PLANSZY + 1):
                if swiat.organizmy[i].podajWiek() >= 1:
                    if self.podajZnak() != swiat.organizmy[i].podajZnak():
                        if self.x == swiat.organizmy[i].x and self.y == swiat.organizmy[i].y:
                            if swiat.organizmy[i].podajZnak() == "Guarana" or swiat.organizmy[i].podajZnak() == "Trawa" or swiat.organizmy[i].podajZnak() == "Mlecz" or swiat.organizmy[i].podajZnak() == "WilczeJagody":
                                if swiat.organizmy[i].podajZnak() == "Guarana":
                                    print(self.podajZnak(), "zjadl ", swiat.organizmy[i].podajZnak())
                                    self.zwiekszSile(1)
                                    swiat.organizmy[i].ustawWiek(0)
                                elif swiat.organizmy[i].podajZnak() == "WilczeJagody": 
                                    print(self.podajZnak(), "zjadl ", swiat.organizmy[i].podajZnak())
                                    swiat.organizmy[i].ustawWiek(0)
                                    self.ustawWiek(0)
                                else:
                                    print(self.podajZnak(), "zjadl ", swiat.organizmy[i].podajZnak())
                                    swiat.organizmy[i].ustawWiek(0)

                            elif swiat.organizmy[i].podajZnak() == "Antylopa":
                                procent = random.randint(1, 100)

                                if procent < 50:
                                    if self.podajSile() >= swiat.organizmy[i].podajSile():
                                        print(self.podajZnak(), "zabil ", swiat.organizmy[i].podajZnak())
                                        swiat.organizmy[i].ustawWiek(0)
                                    elif self.podajSile() < swiat.organizmy[i].podajSile():
                                        if self.podajZnak() == "Czlowiek":
                                            swiat.czyCzlowiekZywy = False
                                            print(swiat.organizmy[i].podajZnak(), "zabil ", self.podajZnak())
                                            self.ustawWiek(0)
                                        else:
                                            print(swiat.organizmy[i].podajZnak(), "zabil ", self.podajZnak())
                                            self.ustawWiek(0)
                                else:
                                    losuj = 0

                                    if losuj == 0:
                                        dx = 1
                                        dy = 0

                                        if (self.czyZnalezionyOrgOtychWspol(swiat, swiat.organizmy[i], dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy)):
                                            swiat.organizmy[i].x = swiat.organizmy[i].x + dx
                                            swiat.organizmy[i].y = swiat.organizmy[i].y + dy
                                        else:
                                            losuj += 1

                                    if losuj == 1:
                                        dx = 1
                                        dy = -1

                                        if (self.czyZnalezionyOrgOtychWspol(swiat, swiat.organizmy[i], dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy)):
                                            swiat.organizmy[i].x = swiat.organizmy[i].x + dx
                                            swiat.organizmy[i].y = swiat.organizmy[i].y + dy
                                        else:
                                            losuj += 1

                                    if losuj == 2:
                                        dx = 0
                                        dy = -1

                                        if (self.czyZnalezionyOrgOtychWspol(swiat, swiat.organizmy[i], dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy)):
                                            swiat.organizmy[i].x = swiat.organizmy[i].x + dx
                                            swiat.organizmy[i].y = swiat.organizmy[i].y + dy
                                        else:
                                            losuj += 1

                                    if losuj == 3:
                                        dx = -1
                                        dy = -1

                                        if (self.czyZnalezionyOrgOtychWspol(swiat, swiat.organizmy[i], dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy)):
                                            swiat.organizmy[i].x = swiat.organizmy[i].x + dx
                                            swiat.organizmy[i].y = swiat.organizmy[i].y + dy
                                        else:
                                            losuj += 1

                                    if losuj == 4:
                                        dx = -1
                                        dy = 0

                                        if (self.czyZnalezionyOrgOtychWspol(swiat, swiat.organizmy[i], dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy)):
                                            swiat.organizmy[i].x = swiat.organizmy[i].x + dx
                                            swiat.organizmy[i].y = swiat.organizmy[i].y + dy
                                        else:
                                            losuj += 1

                                    if losuj == 5:
                                        dx = -1
                                        dy = 1

                                        if (self.czyZnalezionyOrgOtychWspol(swiat, swiat.organizmy[i], dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy)):
                                            swiat.organizmy[i].x = swiat.organizmy[i].x + dx
                                            swiat.organizmy[i].y = swiat.organizmy[i].y + dy
                                        else:
                                            losuj += 1

                                    if losuj == 6:
                                        dx = 0
                                        dy = 1

                                        if (self.czyZnalezionyOrgOtychWspol(swiat, swiat.organizmy[i], dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy)):
                                            swiat.organizmy[i].x = swiat.organizmy[i].x + dx
                                            swiat.organizmy[i].y = swiat.organizmy[i].y + dy
                                        else:
                                            losuj += 1

                                    if losuj == 7:
                                        dx = 1
                                        dy = 1

                                        if (self.czyZnalezionyOrgOtychWspol(swiat, swiat.organizmy[i], dx, dy) == False) and (self.czySciana(swiat, self.x + dx, self.y + dy)):
                                            swiat.organizmy[i].x = swiat.organizmy[i].x + dx
                                            swiat.organizmy[i].y = swiat.organizmy[i].y + dy

                            elif self.podajSile() >= swiat.organizmy[i].podajSile():
                                if swiat.organizmy[i].podajZnak() == "Czlowiek":
                                    print(self.podajZnak(), "zabil ", swiat.organizmy[i].podajZnak())
                                    swiat.organizmy[i].ustawWiek(0)
                                    swiat.czyCzlowiekZywy = False
                                else:
                                    print(self.podajZnak(), "zabil ", swiat.organizmy[i].podajZnak())
                                    swiat.organizmy[i].ustawWiek(0)

                            elif self.podajSile() < swiat.organizmy[i].podajSile():
                                    print(swiat.organizmy[i].podajZnak(), "zabil ", self.podajZnak())
                                    self.ustawWiek(0) # jak organizm ma wiek 0, to nie zyje - do chodzenia po glownych petlach i omijania pustych elementow



