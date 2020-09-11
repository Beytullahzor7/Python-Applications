def asal_sayılar(sayı):

    i = 2

    while (i < sayı):
        if (sayı % i == 0 ):
            return False
        i +=1
        return True

def asal_generator():
    i=2
    while True:
        if(asal_sayılar(i)):
            yield i
        i+=1

for sayı in asal_generator():
    if(sayı > 1000):
        break
    print(sayı)


