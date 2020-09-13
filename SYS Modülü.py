#sys modülü bizim sistemimizde kurulu olan Python sürümünü yönettiğimiz standard bir modüldür.
# Bu modülü kullanarak Python sistemine özgü fonksiyonları ve özellikleri kullanabiliriz

import sys


##################

sys.stderr.write("bu bir hata mesajıdır\n")
sys.stderr.flush()
sys.stdout.write("bu normal bir yazıdır\n")

##################
print(sys.argv)