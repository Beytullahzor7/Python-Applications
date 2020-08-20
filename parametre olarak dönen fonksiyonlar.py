def anafonksiyon(işlem_adı):

    def toplama(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam
       

    def carpım(*args):
        carpım=1
        for i in args:
            carpım*=i
        return carpım   

    if işlem_adı == ("toplama"):
        return toplama
    else:
        return carpım

fonksiyon = anafonksiyon("toplama")
print(fonksiyon(1,2,3,4,5,6,7))
fonksiyon2 = anafonksiyon("carpım")
print(fonksiyon2(3,4,5))

##################################
def toplama(a,b):
    return a+b
def cıkarma (a,b):
    return a-b
def carpma (a,b):
    return a*b
def bölme (a,b):
    return a/b
def anafonksiyon(func1,func2,func3,func4,işlem_adı):

    if işlem_adı == "toplama":
        print(func1(3,4))
    elif işlem_adı == "cıkarma":
        print(func2(10,4))
    elif işlem_adı == "carpma":
        print(func3(9,4))
    elif işlem_adı == "bölme":
        print(func4(25,4))
    else:
        print("Geçersiz İşlem....")

anafonksiyon(toplama,cıkarma,carpma,bölme,"cıkarma")
anafonksiyon(toplama,cıkarma,carpma,bölme,"bölme")    
        

