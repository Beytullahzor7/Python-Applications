#Zaman Ve Tarih işlemleri için kullandıgımız hazır bir modüldür
#eger bilgileri türkçe istersek:
import locale
locale.setlocale(locale.LC_ALL,"")
##############################
from datetime import datetime

şuan =datetime.now()

print(şuan.year)
print(şuan.minute)
print(şuan.microsecond)


#####################
#ctime() fonksiyonu
#Şu anki zamanı daha güzel göstermek için ctime() fonksiyonunu kullanabiliriz.

print(datetime.ctime(şuan)) #daha düzgün gösterir .ctime metodu
######################

#strftime() fonksiyonu¶
   #Yıl bilgisini almak için : %Y

   #Ay ismini almak için : %B

   #Gün ismini almak için : %A

   #Saat bilgisini almak için : %X

   #Gün bilgisini almak için : %D

print(datetime.strftime(şuan,"%Y %X"))
print(datetime.strftime(şuan,"%D"))
print(datetime.strftime(şuan,"%Y %B %A"))

##############################
#timestamp() şuanki zamanın degerini saniye cinsinden basar
şuan = datetime.now()
saniye = datetime.timestamp(şuan)
print(saniye)
#fromtimestamp saniye cinsinden verilen degeri şuana çevirir
şuan2 = datetime.fromtimestamp(saniye)
print(şuan2)

###############################
tarih = datetime(2020,12,10)
suan3 = datetime.now()
print(tarih-suan3) #2 tarih arası fark bulmak


