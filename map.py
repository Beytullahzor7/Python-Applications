def kare(sayi):
    return (sayi**2)
sayilar = range(1,10)
map(kare,sayilar)
list(map(kare,sayilar))
print(list(map(kare,sayilar)))
##############################################

def carp(sayi1,sayi2):
    return(sayi1*sayi2)

sayi1=[1,2,3,4]
sayi2=[3,4,5,6]

map(carp,sayi1,sayi2)

list(map(carp,sayi1,sayi2))
print(list(map(carp,sayi1,sayi2)))

###############################################

def double(x):
    return(x*2)

map(double,[1,2,3,4,5])
list(map(double,[1,2,3,4,5]))
print(list(map(double,[1,2,3,4,5])))

#################################################

list(map(lambda x: x**2,(1,2,3,4,5,6,7,8)))
print(list(map(lambda x: x**2,(1,2,3,4,5,6,7,8))))

#################################################

liste1=[1,2,3,4]
liste2=[3,4,5,6]
list(map(lambda x,y:x*y,liste1,liste2))
print(list(map(lambda x,y:x*y,liste1,liste2)))

#################################################

from functools import reduce 

reduce(lambda x,y : x *y ,[1,2,3,4,5])
print(reduce(lambda x,y : x *y ,[1,2,3,4,5]))

##################################################

def maksimum(x,y):
    if (x>y):
        return x
    else:
        return y

maksimum(3,4)
print(maksimum(3,4))

##################################################
reduce(maksimum,[-2,-3,4,8])
print(reduce(maksimum,[-2,-3,4,8]))

##################################################









