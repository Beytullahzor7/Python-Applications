print("""
**********
ATM MAKİNASINA HOŞGELDİNİZ


İŞLEMLER;

1.BAKİYE SORGULAMA

2.PARA YATIRMA

3.PARA ÇEKME

Programdan cıkmak için 'q' ya basınız
************
""")
bakiye=1000
while True:
    işlem=input("Yapmak istediginiz işlemi seçiniz:")

    if (işlem == 'q'):
        print("yine bekleriz")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif (işlem=="2"):
        miktar=int(input("Miktarı giriniz:"))

        bakiye+=miktar

    elif (işlem=="3"):
        miktar=int(input("miktarı giriniz:"))

        if (bakiye-miktar <0):
            print("böyle bir miktar çekemezsiniz")
            continue
        bakiye-=miktar

    else:
        print("geçersiz işlem")