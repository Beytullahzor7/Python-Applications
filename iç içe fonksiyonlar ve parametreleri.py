def fonksiyon(isim,*args):
    
    print("İsim:",isim)


    print("-------------")
    for i in args:
        print(i)


fonksiyon("murat",1,2,3,4)

##################################

def fonksiyon(**kwargs):
    print(kwargs)

fonksiyon(isim = "murat",soyisim = "coskun",numara =12345)

###################################

def fonksiyon(**kwargs):
    for i,j in kwargs.items():
        print("Argüman İsmi:",i,"Argüman Değeri:",j)

fonksiyon(isim ="murat",soyisim ="coskun",numara=12345)
###################################

def fonksiyon(*args,**kwargs):
    for i in args:
        print(i)

    print("---------------")

    for i,j in kwargs.items():
        print(i,j)
        
fonksiyon(1,2,3,4,5,6,isim = "murat",soyisim = "coskun",numara =12345)

####################################

def selamla(isim):
    print("Selam",isim)
merhaba=selamla
merhaba("Ayse")

#####################################

merhaba("kemal")

#####################################
def fonksiyon():

    def fonksiyon2():
        print("kücük fonksiyondan herkese merhaba")

    fonksiyon2()
    print("büyük fonksiyondan herkese merhaba")

fonksiyon()
#####################################

def fonksiyon(*args):

    def toplama(args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    print(toplama(args))
fonksiyon(1,2,3,4,5)
####################################

def fonksiyon(*args):
    def carpma(args):
        carpma=1
        for i in args:
            carpma*=i
        return carpma
    print(carpma(args))

fonksiyon(8,2,3)
###########################
def fonksiyon(takım):
    print("Takım:",takım)
fonksiyon("galatasaray")

######################################
def fonksiyon(Şehir,*args):
    print("şehir:",Şehir)
    for i in args:
        print (i)
fonksiyon("ankara","mugla")
#####################################

def selamla(isim):
    print("Selamla:",isim)
selamla("ali")
selamla=merhaba
merhaba("ali")
#####################
def fonksiyon(*args): #istedigimiz sayıda değişken atadık
    def topla(args):
        topla=0
        for i in args:
            topla+=i
        return topla
    print(topla(args))
fonksiyon(1,2,3,4,5,6)
    

              
