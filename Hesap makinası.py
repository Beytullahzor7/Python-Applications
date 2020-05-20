print("""*********
HESAP MAKİNASI PROGRAMI

İşlemler;

1.toplama işlemi

2.çıkarma işlemi

3.çarpma işlemi

4.bölme işlemi
*********
""")

a=int(input("1. sayıyı giriniz:"))
b=int(input("2. sayıyı giriniz:"))

işlem=int(input("Yapmak istediginiz işlemi tuşlayınız:"))

if işlem == 1:
    print(" {} ile {} nın toplamı {} dır".format(a,b,a+b))
elif işlem ==2:
    print(" {} ile {} nın farkı {} dır".format(a,b,a-b))
elif işlem == 3:
    print(" {} ile {} nın carpımı {} dır".format(a,b,a*b))
elif işlem == 4:
    print(" {} ile {} nın bölümü {} dır".format(a,b,a/b))
else:
    print("Geçersiz işlem")

