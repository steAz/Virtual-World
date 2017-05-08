

class Organizm:
    
    def __init__(self):
        self._sila = 0
        self._wiek = 0
        self._znak = "Organizm"
        self._inicjatywa = 0
        self._numerOrganizmu = 0
        self.x  = 0
        self.y = 0
        self._poprzednieX = 0
        self._poprzednieY = 0
        self._czyRozmnazac = False
        self._iloscTurOdSpecjUm = 0
        self._szybkoscAntylopyON = True
        self._czyMoznaWlSpecjUm = True

    

    class Kierunek:
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3
        LOSOWY = 4


    def czySciana(self, swiat, x, y):
        if (x < 0 or x > swiat.podajSzerokosc() - 1): return True

        if (y < 0 or y > swiat.podajWysokosc() - 1): return True

        return False


    def akcja(self, swiat, kierunek):
        return


    def kolizja(self, swiat, czyRozmnazac):
        return


    def ustawNumerOrganizmu(self, nrOrganizmu):
        self._numerOrganizmu = nrOrganizmu


    def podajNumerOrganizmu(self):
        return self._numerOrganizmu


    def ustawWiek(self, wiek):
        self._wiek = wiek

    
    def podajZnak(self):
        return self._znak


    def zwiekszSile(self, sila):
        self._sila += sila


    def podajWiek(self):
        return self._wiek


    def usunOrganizm(self, organizm):
        organizm = None


    def dodajWiek(self):
        self._wiek += 1


    def podajInicjatywe(self):
        return self._inicjatywa


    def ustawIloscTurOdSpecjUm(self, iloscTurOdSpecjUm):
        self._iloscTurOdSpecjUm = iloscTurOdSpecjUm


    def podajCzyMoznaWlSpecjUm(self):
        return self._czyMoznaWlSpecjUm


    def dodajIloscTurOdSpecjUm(self):
        self._iloscTurOdSpecjUm += 1


    def podajIloscTurOdSpecjUm(self):
        return self._iloscTurOdSpecjUm


    
    def ustawCzySzybkAntylopyON(self, szybkoscAntylopyON):
        self._szybkoscAntylopyON = szybkoscAntylopyON


    def ustawCzyMoznaWlSpecjUm(self, czyMoznaWlSpecjUm):
        self._czyMoznaWlSpecjUm = czyMoznaWlSpecjUm


    def podajCzySzybkoscAntylopyON(self):
        return self._szybkoscAntylopyON


    def ustawInicjatywe(self, inicjatywa):
        self._inicjatywa = inicjatywa

   
    def ustawSile(self, sila):
        self._sila = sila


    def podajSile(self):
        return self._sila


    def podajWiek(self):
        return self._wiek


    def podajCzyMoznaRozmnazac(self):
        return self._czyRozmnazac
