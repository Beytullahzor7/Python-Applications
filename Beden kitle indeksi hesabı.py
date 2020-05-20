Boy=float(input("Boyunuzu Giriniz:"))
Kilo=float(input("Kilonuzu Giriniz:"))

beden_kitle_indeksi=(Kilo/(Boy ** 2))

if beden_kitle_indeksi < 18.5:

    print("ZAYIF")

elif beden_kitle_indeksi >=18.5 and beden_kitle_indeksi < 25:
    print("NORMAL")

elif beden_kitle_indeksi >=25 and beden_kitle_indeksi <30:
    print("FAZLA KİLOLU")

else:
    print("OBEZ")