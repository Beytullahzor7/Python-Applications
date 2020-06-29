#ZİP FONKSİYONU ALDIGI PARAMETRELERDE FONKSİYON OLMAZ VE KISACA ZİP FONK. GRUPLANDIRMALAR İÇİN KULLANILIR

liste1 = [1,2,3,4]
liste2 = ["python", "java" ,"php","javascript"]

for i,j in zip(liste1,liste2):
    print("i:" ,i,"j:", j)

######################################

no=[1,2,3]
isim=["ali","veli","ahmet"]

zip1=zip(no,isim)
print(list(zip1))

#######################################

liste3= [1,3,6,8,9,12,13,14]
liste4= [4,5,10,13,15,19,20]

for i,j in zip(liste3,liste4):

    filter1= filter(lambda i: i %3 ==0,liste3)
    filter2= filter(lambda j: j %5 ==0,liste4)

print("3 ün katları",list(filter1))
print("5 in katları",list(filter2))

