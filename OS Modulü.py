#os modülü kullanılarak işletim sisteminde işlemler gerçekleştirebiliyoruz
#standart bir python modülüdür

import os
os.chdir("C:/Users/Monster/Desktop") #bulundugunu dizini bu yolla degiştiririz
print(dir(os))
print(os.getcwd()) #modülün hangi dizinde bulundugunu gösterir.
##################
#print(os.listdir()) #desktop altındaki dosyaları listeler
for i in os.listdir():
    print(i)
################
os.mkdir("Deneme1") #deneme1 adında klasör olusturduk
os.makedirs("deneme2/deneme3") #deneme2 klasörü altında deneme3 olustu
os.rmdir("deneme2/deneme3") #deneme2 klasörü altındaki deneme3 ü sildik
os.removedirs() #bu method ile parantez içine yazılan klasör ve alt klasörler silinir
print(os.stat("deneme2"))