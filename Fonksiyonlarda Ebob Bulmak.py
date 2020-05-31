def ebob_bulmak(sayı1,sayı2):

    i=1
    ebob=1

    while (i<= sayı1 and i<=sayı2):

        if (not (sayı1 % i)  and not  (sayı2 % i)):

            ebob=i

        i+=1

    return ebob

sayı1=int(input("1. Sayı:"))
sayı2=int(input("2. Sayı:"))

print("Ebob:",ebob_bulmak(sayı1,sayı2))