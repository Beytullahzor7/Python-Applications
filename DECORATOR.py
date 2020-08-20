#decorator fonksiyonlar, pythonda fonksiyonlarımıza dinamik olarak ekstra özellik ekledigimiz
#fonksiyonlardır ve decorator fonk. kullanımı kod tekrarı yapmamızı engeller
#pythonda decorator fonk. flask gibi framworklerde oldukca fazla kullanılır.

import time

def kareleri_hesapla(sayılar):
    
    sonuc = list()
    baslama = time.time()
    
    for i in sayılar:
        sonuc.append(i ** 2)
        
    bitis = time.time()

    print("Bu fonksiyon "+ str(bitis-baslama)+" saniye sürdü")
    return sonuc

def küpleri_hesapla(sayılar):

    sonuc =list()
    baslama = time.time()

    for i in sayılar:
        sonuc.append(i ** 3)

    bitis = time.time()

    print("Bu fonksiyon " + str(bitis-baslama)+" saniye sürdü")
    

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))
#bu fonksiyonda decorator fonk kullanmadık ve aynı işlemleri tekrarladık
#şimdi bu fonksiyonu decorator yardımı ile yapalım



import time

def zaman_hesapla(func):
    
    def wrapper(sayılar): #decorator fonk wrapper ile aktif ettik
        baslama = time.time()

        sonuc = func(sayılar)

        bitis = time.time()

        print(func.__name__+ " " + str(bitis-baslama) + " saniye sürdü.")
        return sonuc
    return wrapper

@zaman_hesapla
def kareleri_hesapla(sayılar):    
    sonuc = list()   
    
    for i in sayılar:
        sonuc.append(i ** 2)
    
    return sonuc
@zaman_hesapla
def küpleri_hesapla(sayılar):  
    sonuc = list()
   
    for i in sayılar:
        sonuc.append(i ** 3)

    return sonuc

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))








