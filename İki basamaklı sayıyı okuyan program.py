birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunuş(sayı):

    birincibasamak= sayı % 10
    ikincibasamak= sayı // 10

    return onlar[ikincibasamak] + "" +birler[birincibasamak]

sayı=int(input("Sayı:"))

print(okunuş(sayı))