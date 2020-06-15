class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maaş=maaş
        self.diller=diller

    def BilgileriGöster(self):
        print("""
        YAZILIMCI OBJESİNİN ÖZELLİKLERİ
        
        İSİM= {}
        
        SOYİSİM={}
        
        NUMARA={}
        
        MAAŞ={}
        
        DİLLER={}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))

    def zam_yap(self,zam_miktarı):
        print("Zam Yapılıyor...")
        self.maaş +=zam_miktarı


    def dil_ekle(self,yeni_dil):
        print("Dil Ekleniyor...")
        self.diller.append(yeni_dil)


yazılımcı = Yazılımcı("Mehmet", "YILMAZ", 1998, 4000, ["python", "java"])
yazılımcı.BilgileriGöster()

yazılımcı.dil_ekle("Flutter")
yazılımcı.zam_yap(500)
yazılımcı.BilgileriGöster()




