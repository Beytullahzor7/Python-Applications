liste=["a","b","c","d","e","f","g"]

for i,j in enumerate(liste):

    if i % 2 ==0: #sadece indeks numarası çift olanları bastırdık
        print(j)

######################################################

liste1 = ["elma", "armut","muz","kiraz","karpuz","kavun"]

i=0

enumerate(liste1)
list(enumerate(liste1))
print(list(enumerate(liste1)))

###################################(all fonksiyonu kullanımı)
liste5=[True,False,True,True,False,False]
print(all(liste5))

liste6=[True,True,True]
print(all(liste6))

liste7=[0,0,0,0,0,0]
print(all(liste7))

#########################################################(any fonksiyonu)

liste9=[False,False,False,False,False,False,False,False,False,False,False,True]
print(any(liste9))