import random
from Organizm import Organizm

WIELKOSC_PLANSZY = 2022

class Roslina(Organizm):

    kierunek = Organizm.Kierunek

    def czyZnalezionyOrgOtychWspol(self, swiat, sprawdzanyOrganizm, dx, dy):
        for i in range(WIELKOSC_PLANSZY + 1):
            if (swiat.organizmy[i].podajWiek() >= 1) and (sprawdzanyOrganizm is not swiat.organizmy[i]):
                if (sprawdzanyOrganizm.x + dx == swiat.organizmy[i].x) and (sprawdzanyOrganizm.y + dy == swiat.organizmy[i].y):
                    return True

        return False


    def kolizja(self, swiat, czyRozmnazac):
        i = 1

    def akcja(self, swiat, kierunek):
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




