def faktoriyel(sayı):

    faktoriyel=1

    if (sayı ==0 or sayı ==1):

        print("Faktoriyel:",faktoriyel)

    else:

        while(sayı>=1):

            faktoriyel*=sayı

            sayı-=1

        print("Faktoriyel:",faktoriyel)

faktoriyel(1)
faktoriyel(2)
faktoriyel(3)
faktoriyel(4)
faktoriyel(5)
faktoriyel(6)
