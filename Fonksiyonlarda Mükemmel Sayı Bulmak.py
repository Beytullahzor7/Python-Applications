#Mükemmel sayı=Tam bölenlerinin toplamı kendisine eşit olan sayılardır.

def mükemmelsayı(sayı):

    toplam=0

    for i in range(1,sayı):

        if (sayı % i == 0):
            toplam+=i
    return toplam==sayı

for i in range (1,101):

    if (mükemmelsayı(i)):

        print("Mükemmel Sayı:",i)