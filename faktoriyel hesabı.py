print("""
***********
Faktoriyel Progamı

Çıkmak için 'q' ya basınız.
***********
""")

while True:
    sayi=input("Sayı:")
    if (sayi == "q"):
        print("Programı Sonlandır")
        break
    else:

        sayi=int(sayi)

        faktoriyel = 1
        for i in range(2,sayi+1):

            faktoriyel *=i

        print("Faktoriyel:" , faktoriyel)

