def faktoriyel(sayı):
    faktoriyel=1
    if (sayı==0 or sayı==1):
        print("faktoriyel:",faktoriyel)
    else:
        while(sayı>=1):
            faktoriyel*=sayı
            sayı-=1
        print("faktoriyel:",faktoriyel)

faktoriyel(3)

#######################################

def toplama(a,b,c):
    return(a+b+c)
def ikiylecarp(a):
    return(a*2)
def dördeböl(a):
    return (a/4)

print(dördeböl(ikiylecarp(toplama(3,8,2))))

########################################

def selamla(isim="isimsiz"):

    print("selam",isim)

selamla()
selamla("ali")
################################
def toplama(*a):
    toplam=0

    for i in a:
        toplam+=i
    print(toplam)
toplama(5,6,3,5,4,6,4,5,3,4,5)

##################################

s="python"
def fonksiyon():
    print(s)
fonksiyon()
##################################
a=int("asdasd34124")

try:
    a = int("asdasd34124")
    print("program burada")
except:
    print("bir hata olustu")
print("bloklar sona erdi")

