def not_hesapla(satır): #fonksiyon içerisine sonuclar.txt de bulunan her bir satırı göndermek için (satır) komutu kullandık

    satır = satır[:-1] #dosya içerisinde bulunan \n ifadesine bu komutla devre dısı bırakırız

    liste = satır.split(",") #stringler virgüle göre ayrılmıs oldu
    #üsste kullandıgımız split fonk sayesinde her bir parametreyi kendi içinde listeleştirdik

    isim = liste[0] #listenin 0. elemanı isime eşittir

    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])


    son_not=not1*(3/10)+not2*(3/10)+not3*(4/10)

    if (son_not >= 90):
        harf="AA"
    elif (son_not >= 85):
        harf="BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf=("FF")

    return isim+ "-------------------> " + harf + "\n"

def kalanlar(satır):

    satır = satır[:-1]
    liste=satır.split(",")
    isim=liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)
    if son_not <= 70:
        return isim + "---------> Kaldı" + "\n"
    else:
        return "" #bunu koymamaka string hatasına sebep olur

def geçenler(satır):

    satır = satır[:-1]
    liste=satır.split(",")
    isim=liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)
    if son_not >= 70:
        return isim + "---------> Geçti" + "\n"
    else:
        return "" #bunu koymamak string hatasına sebep olur


with open("sonuclar.txt","r",encoding="utf-8") as file:

    eklenecekler_listesi = []
    eklenecekler = []
    eklenecekler2 = []


    for i in file:


        eklenecekler_listesi.append(not_hesapla(i))
        eklenecekler.append(kalanlar(i))
        eklenecekler2.append(geçenler(i))

    with open("notlar.txt","w",encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)

    with open("Kalanlar.txt","w",encoding="utf-8") as file3:

        for i in eklenecekler:
            file3.write(i)

    with open("Geçenler.txt","w",encoding="utf-8") as file4:

        for i in eklenecekler2:
            file4.write(i)



