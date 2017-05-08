from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Panel(QLabel):
    def __init__(self, rodzic, x, y):
        QLabel.__init__(self, rodzic)
        self.x = x
        self.y = y
        self.setStyleSheet("background-color: darkGray")


    def wyczyscPole(self, rodzic):
        self.setText("")
        self.setPixmap(QPixmap(None))


    def contextMenuEvent(self, pole):
        self.__menu = QMenu(self)
        opcje=["Wilk", "Antylopa", "Lis", "Owca", "Mlecz", "Trawa", "Guarana", "WilczeJagody", "Zolw"]
        wybor = []
        for i in range (0,9):
            wybor.append(QAction(opcje[i],self))
            self.__menu.addAction(wybor[i])
        wybor[0].triggered.connect(lambda: self.parent().parent().swiat.dodajOrganizm(self.x, self.y, "Wilk"))
        wybor[1].triggered.connect(lambda: self.parent().parent().swiat.dodajOrganizm(self.x, self.y, "Antylopa"))
        wybor[2].triggered.connect(lambda: self.parent().parent().swiat.dodajOrganizm(self.x, self.y, "Lis"))
        wybor[3].triggered.connect(lambda: self.parent().parent().swiat.dodajOrganizm(self.x, self.y, "Owca"))
        wybor[4].triggered.connect(lambda: self.parent().parent().swiat.dodajOrganizm(self.x, self.y, "Mlecz"))
        wybor[5].triggered.connect(lambda: self.parent().parent().swiat.dodajOrganizm(self.x, self.y, "Trawa"))
        wybor[6].triggered.connect(lambda: self.parent().parent().swiat.dodajOrganizm(self.x, self.y, "Guarana"))
        wybor[7].triggered.connect(lambda: self.parent().parent().swiat.dodajOrganizm(self.x, self.y, "WilczeJagody"))
        wybor[8].triggered.connect(lambda: self.parent().parent().swiat.dodajOrganizm(self.x, self.y, "Zolw"))
        self.parent().parent().swiat.rysujOrganizmy()
        self.__menu.popup(QCursor.pos())
        


