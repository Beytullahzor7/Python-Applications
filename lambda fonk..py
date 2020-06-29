#LAMBDA FONKSİYONU VE RETURN KULLANIMI

def ikiyleçarp(x):
    return x*2
print(ikiyleçarp(4))

#######################

ikiyleçarp=lambda x : x*2
print(ikiyleçarp(4))

###########

def toplama(x,y,z):
    return x+y+z
print(toplama(7,8,9))

###################

toplama = lambda x,y,z : x+y+z
print(toplama(7,8,9))

###############

def tersçevir(s):
    return s[::-1]
print(tersçevir("PYTHON"))

#############

terscevir=lambda s: s[::-1]
print(terscevir("PYTHON"))

##########ÇİFT TEK SAYI BULMA##########

def çifttek(sayı):
    return sayı % 2 ==0
print(çifttek(4))
print(çifttek(5))
##############
çifttek=lambda sayı: sayı % 2==0
print(çifttek(7))

######3333
import time
print("hello")
time.sleep(5)
print("world")
