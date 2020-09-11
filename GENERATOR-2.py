#Generator Fibonacci serisi olusturma

def fibonacci():
    a=1
    b=1
    yield a
    yield b

    while True: #bizden deger istendigi sürece
#sonsuza kadar deger üretmek için while true kullandık

        a,b = b,a+b

        yield b

for sayı in fibonacci():

    if (sayı > 100000):
        break
    print(sayı)

