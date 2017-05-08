from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Panel import Panel

class Plansza(QWidget):
    def __init__(self, rodzic, szerokoscRamki, wysokoscRamki, rozmiarPlanszy):
        QWidget.__init__(self, rodzic)

        self.rozmiarPanelu=(wysokoscRamki/rozmiarPlanszy)
        #self.resize(self.rozmiarPanelu, self.rozmiarPanelu)
        self.rozmiarPlanszy = rozmiarPlanszy

        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(self.backgroundRole(), Qt.darkGreen)
        self.setPalette(paleta)

        self.setLayout(QGridLayout())
        self.tabPaneli = []

        x = 0
        for x in range(rozmiarPlanszy):
            self.tabPaneli.append([])
            y = 0
            for y in range(rozmiarPlanszy):
                self.tabPaneli[x].append(Panel(self, x, y))
                self.tabPaneli[x][y].setGeometry(self.rozmiarPanelu * x, self.rozmiarPanelu * y, self.rozmiarPanelu - 2, self.rozmiarPanelu - 2)


    def ustawPoleTekstowe(self, rodzic, x, y, znak):
        self.tabPaneli[x][y].setText(znak)

        if znak == "Wilk": pixmap = QPixmap('wilk.jpg')
        if znak == "Czlowiek": pixmap = QPixmap('stark.png')
        if znak == "Lis": pixmap = QPixmap('lis.jpg')
        if znak == "Antylopa": pixmap = QPixmap('antylopa.jpg')
        if znak == "Owca": pixmap = QPixmap('owca.jpg')
        if znak == "Zolw": pixmap = QPixmap('zolw.png')
        if znak == "Trawa": pixmap = QPixmap('trawa.jpg')
        if znak == "Mlecz": pixmap = QPixmap('mlecz.jpg')
        if znak == "Guarana": pixmap = QPixmap('guarana.jpg')
        if znak == "WilczeJagody": pixmap = QPixmap('wilczejagody.jpg')

        self.tabPaneli[x][y].setPixmap(pixmap)


    def wyczyscPlansze(self, rodzic):
        for x in range(self.rozmiarPlanszy):
            for y in range(self.rozmiarPlanszy):
                self.tabPaneli[x][y].wyczyscPole(self)



