while True:
    ürün_fiyatı=int(input("Ürünün fiyatını giriniz:"))

    if ürün_fiyatı >= 100:
        print("Bakiyeniz Yetersiz")
        break
    print("Kartınızdan ürün tutarı tahsil edilmiştir!")