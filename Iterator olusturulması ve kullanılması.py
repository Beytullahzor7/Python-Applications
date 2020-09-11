#kendi iterable objelerimizi olusurmak için
#olusturugumuz sınıfın mutlaka __iter()__ ve __next()__ metodu
#içermesi gerekir

#simdi 1 örnekle açıklayalım

class Kumanda():
    def __init__(self,kanal_listesi):

        self.kanal_listesi = kanal_listesi
        self.index = -1 #-1den baslatma sebebimiz 1 ekleyerek gittigimizde direkt 0 lamıs olmamız

    def __iter__(self): #iterator olusturmak için kullanılacak

        return self
    def __next__(self):
        self.index += 1

        if self.index <= len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration

kumanda = Kumanda(["ATV","TRT","BLOOMBERG","KANAL D"])
iterator = iter(kumanda)
print(next(iterator))

for i in kumanda:
    print(i)



        
        
