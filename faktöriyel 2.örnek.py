print("""
***********
Faktöriyel programı

cıkmak için "q" ya basınız
***********
""")


while True:
    sayi =input("sayi:")

    if (sayi == "q"):
        print("programdan cıkılıyor")
        break
    else:

        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):

            faktoriyel *=i

        print("{} sayisinin faktoriyeli {} sayisina eşittir".format(sayi,faktoriyel))