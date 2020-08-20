#####İLERİ SEVİYE SAYILAR######

print(bin(4)) # 10 luk tabandaki sayıyı 2 lik tabanda yazmak
print(hex(32)) # 10 luk tabandaki sayıyı 16 lık tabanda yazmak
print(abs(-4)) #mutlak deger almak
print(round(4.6)) #sayıyı yuvarlamak
print(max(-2,8)) #büyük olan sayıyı döndürür
print(min(-3,-2)) # küçük olan sayıyı döndürür
print(sum([1,2,3,4,5,6])) #liste demet şeklinde verilen degerlerin toplamını döndürür
print(pow(3,4)) #Üs alma işlemini gerçekleştirir, 3 üzeri 4 tür verdigimiz deger
print("python".upper()) #küçük olan her harfi büyük harfe çevirir
print("PYThon".upper())
print("PYTHOn".lower()) #büyük olan her harfi küçük harfe dönüştürür
print("Galatasaray".replace("a","e")) #print içerisindeki ifadede belirli harfleri başka bir harfle değiştiririz
print("Fatih Terim".startswith("F")) #fonk içerisine koydugumuz harf ile başlayıp başlamadıgını dönüt olarak bize verir
print("Fatih Terim".endswith("m"))  #fonk içerisine koydugumuz harf ile bitip bitmedigini dönüt olarak bize verir
liste="python-java-php".split("-") #stringi parçalara ayırarak herbir elemanı listeleştirir
print(liste)
liste1="SAMPİYON GALATASARAY".split(" ")
print(liste1)
liste3=["21","02","2004"]
"/".join(liste3)
print(liste3) #.join metodu ile listenin elemanlarını bir string degeri ile birleştiririz.
print("ada kapısı yandan çarklı".count("a")) #count() fonk içerisinde verilen harfin kaç tane old sayar
print("ada kapısı yandan çarklı".count("a",2)) # , 2 kısmı verilen index degerinde itibaren say demektir.
print("araba".find("b")) #string içerisindeki ifadede "b" harfinin kacıncı indexte old. verir
print("araba".rfind("r"))#string içerisindeki ifadede "r" harfini sondan başlayarak kacıncı indexte oldugunu bulur
