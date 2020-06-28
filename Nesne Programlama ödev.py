import time

class Bilgisayar():

    def __init__(self,calısan_uygulama="PYTHON",tur="Masaüstü",marka="Monster",hafıza="1 TB",ekran_kartı="GTX1050",uygulama_list=["Microsoft Office","Oyunlar","Web"]):

        self.calısan_uygulama=calısan_uygulama
        self.tur=tur
        self.marka=marka
        self.hafıza=hafıza
        self.ekran_kartı=ekran_kartı
        self.uygulama_list=uygulama_list

    def uygulama_acma(self):

        print("Mevcut Uygulamalar",self.uygulama_list)

        Acılmak_istenen_uygulama=input("Lütfen açmak istediginiz uygulamayı giriniz:")

        if (Acılmak_istenen_uygulama == "Microsoft Office"):

            print("""
            ***********
            1. Microsoft Word
            2. Powerpoint Sunu
            3. Excel
            4. Microsoft Outlook
            ***********
            """)

            while True:
                işlem=input("Yapmak istediginiz işlemi seçiniz:")

                if (işlem=="1"):
                    print("Uygulama Üzerine Çift Tıklayınız")
                    time.sleep(2)
                    print("Microsoft Word Açılıyor...")
                elif (işlem=="2"):
                    print("Uygulama Üzerine Çift Tıklayınız")
                    time.sleep(2)
                    print("Powerpoint Sunu Açılıyor...")
                elif (işlem=="3"):
                    print("Uygulama Üzerine Çift Tıklayınız")
                    time.sleep(2)
                    print("Excel Açılıyor...")
                elif(işlem=="4"):
                    print("Uygulama Üzerine Çift Tıklayınız")
                    time.sleep(2)
                    print("Microsoft Outlook Açılıyor...")
                return

        if(Acılmak_istenen_uygulama == "Oyunlar"):

            print("""
            ************
            1. CS-GO
            2. PES-2020
            3. PUBG
            ************
            """)
            while True:

                işlem = input("Yapmak istediginiz işlemi seçiniz:")

                if (işlem=="1"):
                    print("Oyun açılıyor...")
                    time.sleep(2)
                    print("CS-GO Açıldı!")
                    return
                elif (işlem =="2"):
                    print("Oyun Açılıyor...")
                    time.sleep(2)
                    print("PES-2020 Açıldı!")
                    return
                elif (işlem =="3"):
                    print("Oyun Açılıyor...")
                    time.sleep(2)
                    print("PUBG Açıldı!")
                    return
        if(Acılmak_istenen_uygulama == "Web"):

            print(""""
            *********
            1. Google Chrome
            2. Opera
            *********
            """)
            while True:

                işlem = input("Yapmak istediginiz işlemi seçiniz:")

                if (işlem== "1"):
                    print("Google Chrome Açıldı!")

                elif (işlem== "2"):

                    print("Opera Açıldı!")
                return


    def uygulama_indirme(self):

        İndirilecek_Uygulama=input("İndirmek İstediginiz Uygulamayı Giriniz:")
        print("Uygulama İndiriliyor Lütfen Bekleyiniz....")
        self.uygulama_list.append(İndirilecek_Uygulama)
        time.sleep(2)
        print("{} indirildi".format(İndirilecek_Uygulama))
        return

    def Uygulama_Kapatma(self):

        print("Uygulamayı Kapatmak İçin 'X' e basınız")
        self.calısan_uygulama="Uygulama Kapatılıyor"
        time.sleep(2)
        print("Uygulama Kapatıldı")
        return


bilgisayar1=Bilgisayar()

print("Bilgisayara Hoşgeldiniz!")

print("""
*********
İŞLEMLER

1. UYGULAMA AÇMA

2. UYGULAMA İNDİRME

3. UYGULAMA KAPATMA

4. Bilgisayar Bilgileri

*********
""")

while True:

    işlem=input("Yapmak İstediginiz İşlemi Seçiniz:")

    if (işlem=="ALT+F4"):
        print("Bilgisayar Kapatılıyor...")
        break

    elif (işlem =="1"):

        bilgisayar1.uygulama_acma()

    elif (işlem =="2"):

        bilgisayar1.uygulama_indirme()

    elif (işlem =="3"):

        bilgisayar1.Uygulama_Kapatma()

    elif (işlem == "4"):

        print("Calısan Uygulama:",bilgisayar1.calısan_uygulama)
        print("Tur:",bilgisayar1.tur)
        print("Marka:",bilgisayar1.marka)
        print("Hafıza:",bilgisayar1.hafıza)
        print("Ekran Kartı:",bilgisayar1.ekran_kartı)
        print("Uygulama Listesi:",bilgisayar1.uygulama_list)



    else:
        print("Lütfen Geçerli Bir İşlem Giriniz!!!")

















