class Kuvvet3():
    def __init__(self,max = 0):
        self.max = max
        self.kuvvet = 0

    def __iter__(self):

        return  self #direkt objemizi döndürdük

    def __next__(self):
        if (self.kuvvet <= self.max):
            sonuc = 3 ** self.kuvvet

            self.kuvvet += 1

            return sonuc

        else: #kuvvetimiz maxı geçmişse

            raise   StopIteration

kuvvet = Kuvvet3(6) #max degerimiz 6 oldu ve en fazla
# 3ün 6. kuvvetini görebilecegiz

iterator = iter(kuvvet)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#0. kuvvetten başlattıgımız için 3 ün sıfırıncı kuvvveti
#ilk olarak yazdırdık

