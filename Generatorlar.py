#Generatorlar bellekte herhangi bir yer kaplamaz ve
#iterable objeleri olusturmak için kullanılan objelerdir
#generatorlar bir kere for döngüsü içinde kullanılır sonra kaybolur
#uzun degerler basacaksak ve sadece deger basacaksak böyle durumda
#her seferinde deger üretmemizi saglayan generator kullanabiliriz
def kareleri_al():

    sonuc=[]

    for i in range(1,6):
        sonuc.append(i**2)
    return sonuc

print(kareleri_al())

#######################################

def kareleri_al():
    for i in range(1,6):
        yield i ** 2

generator = kareleri_al()
print(generator)

iterator = iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#########################################
liste = [i * 3 for i in range(5)]
print(liste)

generator = (i * 3 for i in range(5))
print(generator)

iterator = iter (generator)
print(next(iterator))

#########################################

def carpimtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield(" {} x {} = {}".format(i,j,i*j))
#yield kullanılması generator kullanıldıgının kanıtıdır

for i in carpimtablosu():
    print(i)
    























