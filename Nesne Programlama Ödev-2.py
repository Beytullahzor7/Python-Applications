import time

class Hayvanlar():

    def __init__(self,tur="Omurgalılar ve Omurgasızlar",Ayak_sayısı="Değişkenlik Gösterir",yasam_alanı="Kara,Hava,Su",Beslenme_sekli="Etçil,Otçul,Hepçil"):

        self.tur=tur
        self.Ayak_Sayısı=Ayak_sayısı
        self.yasam_alanı=yasam_alanı
        self.Beslenme_Sekli=Beslenme_sekli

    def BilgileriGoster(self):

        print("Hayvanların Genel Özellikleri")
        print("Türü:\nAyak_Sayısı:\nYasam_Alanı:\nBeslenme_Sekli:\n")

class Köpekler(Hayvanlar):

    def __init__(self,tur="Memeli",Ayak_sayısı="4",yasam_alanı="Kara",Beslenme_sekli="Etçil",Genel_ozellikler=["Hızlılardır","Ömürleri Kısadır","Fazla Dogum Yaparlar"],cinsleri=["pitbull","dogo","golden"]):

        super().__init__(tur,Ayak_sayısı,yasam_alanı,Beslenme_sekli)
        print("Köpek Classının İnit Fonksiyonu Çagırıldı")
        self.Genel_ozellikleri=Genel_ozellikler
        self.cinsleri=cinsleri

    def BilgileriGoster(self):

        print("Köpeklerin Özellikleri")
        print("Türü:\nAyak_Sayısı:\nYasam_Alanı:\nBeslenme_Sekli\nGenel_ozellikleri:\nCinsi:\n")

class Kuslar(Hayvanlar):

    def __init__(self):