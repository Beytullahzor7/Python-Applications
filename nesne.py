class Araba():
    def __init__(self,model,renk,silindir):
        self.model=model
        self.renk=renk
        self.silindir=silindir

araba1=Araba("renault","beyaz",4)
araba2=Araba("audi","gümüş",3)

print(araba1.model)
print(araba2.model)