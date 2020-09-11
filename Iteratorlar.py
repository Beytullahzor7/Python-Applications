#ITERATORLAR = en genel anlamıyla üzerinde gezinebilecek objelerdir ve bu obje
#her seferinde sadece 1 eleman döner.
#Bir objenin iterable olması için  __iter()__ ve __next()__ metodları mutlaka tanımlanmalı

liste = [1,2,3,4,5]

iterator = iter(liste)
print(iterator)

#listenin elemanlarına iterator üzerinden ulasmak için:

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

liste2=[11,22,33,44]
for i in liste2:
    print(i)
#biz bu döngüyü böyle görsekte python kendi içinde bu fonk. basarken
#iteratorları kullanarak liste üzerinde geziniyor

#aslında kendi içinde söyle yazıyor:

iterator = iter(liste)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

