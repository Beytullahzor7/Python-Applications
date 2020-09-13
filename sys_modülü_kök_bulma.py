import sys

def kok_bulma(a,b,c):

    delta = b ** 2 - 4 * a * c

    if delta<0:
        print("Reel Kök Yoktur...")
    else:
        x1 = (-b - delta ** 0.5) / 2*a
        x2 = (-b + delta ** 0.5) / 2*a

        return (x1,x2)
a=2
b=6
c=4
h=kok_bulma(a,b,c)
print(h)