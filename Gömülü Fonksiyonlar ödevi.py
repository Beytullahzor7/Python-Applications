#DİKDÖRTGEN ALANI BULMAK

def diktörtgen_alanı(liste):

    return (liste[0] * liste[1])

liste=[(3,4),(10,3),(5,6),(1,9)]

print(list(map(diktörtgen_alanı,liste)))

#ÜÇGEN OLUP OLMADIGINI BULMAK

def üçgen_mi(demet):
    if (abs(demet[0] + demet[1]) > demet[2] and abs(demet[0] + demet[2]) > demet[1] and abs(demet[1] + demet[2]) >
            demet[0]):
        return True
    else:
        return False

liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(üçgen_mi,liste)))

###########################################

from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]

filtre =list(filter(lambda x:x%2==0,liste))

print(reduce(lambda x,y: x+y,filtre))

###########################################

isimler =["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisimler =["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

zip(isimler,soyisimler)

for i,j in zip(isimler,soyisimler):
    print(i,j)







