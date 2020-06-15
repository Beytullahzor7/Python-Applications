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
    pass

yönetici=Yönetici("Ahmet",3000,"IT")

yönetici.departman_değiştir("İnsan Kaynakları")

yönetici.zam_yap(400)


yönetici.bilgilerigöster()
