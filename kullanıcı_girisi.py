print(""""****************
KULLANICI GİRİŞİ PROGRAMI
*****************""")


sys_kullanıcı_adı="beytullah"
sys_parola="12345"
giriş_hakkı=3

while True:
    kullanıcı_adı=input("Kullanıcı adını giriniz:")
    parola= input("parolayı giriniz:")
    if (kullanıcı_adı != sys_kullanıcı_adı and parola ==sys_parola):
        print("kullanıcı adını hatalı girdiniz")
        giriş_hakkı -=1
    elif (kullanıcı_adı==sys_kullanıcı_adı and parola != sys_parola):
        print("Parolayı yanlış girdiniz!!!")
        giriş_hakkı -=1
    elif (kullanıcı_adı!=sys_kullanıcı_adı and parola != sys_parola):
        print("her ikisini de yanlış girdiniz")
        giriş_hakkı -=1
    else:
        print("Sisteme Başarı ile giriş yaptınız")
        break
    if giriş_hakkı == 0:
        print("Giriş Hakkınız Bitti!!!")
        break