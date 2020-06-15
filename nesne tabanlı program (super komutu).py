class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalısan sınıfının init fonksiyonu")

        self.isim=isim
        self.maaş=maaş
        self.departman=departman

    def bilgilerigöster(self):
        print("Çalışan sınıfının bilgileri....")

        print("İsim: {} \nMaaş : {} \nDepartman : {} \n".format(self.isim,self.maaş,self.departman))

    def departman_değiştir(self,yeni_departman):
        self.departman= yeni_departman

    def zam_yap(self,zam):
        print("Zam Yapılıyor...")
        self.maaş+=zam

class Yönetici(Çalışan):

    def __init__(self,isim,maaş,departman,kişi_sayısı):
        super().__init__(isim,maaş,departman)
        print("Yönetici Sınıfının İnit Fonksiyonu")
        self.kişi_sayısı= kişi_sayısı

    def bilgilerigöster(self):
        print("Yönetici Sınıfının Bilgileri....")

        print("isim: {}\nMaaş: {}\nDepartman: {}\nKişi sayısı: {}\n".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))

    def zam_yap(self,zam):
        print("Zam Yapılıyor...")
        self.maaş+=zam

yönetici=Yönetici("mehmet",5000,"Bilişim",5)
yönetici.bilgilerigöster()

