import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()
################################################
# KENDİ MAİLİNİZİ VE ŞİFRENİZİ GİRİNİZ.
e_mail = "MAİL ADRESİNİZ"
e_mail_şifre = "ŞİFRENİZ"
################################################

mesaj["From"] = e_mail
mail_atılacaklar = ['xxxx@gmail.com', 'xxx@gmail.com']

mesaj["Subject"] = "TOPLU MESAJ"

yazi = """
Selam....

Ad Soyad
"""

mesaj_gövdesi = MIMEText(yazi, "plain")

mesaj.attach(mesaj_gövdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()

    mail.login(e_mail, e_mail_şifre)

    for her_bir_mail in mail_atılacaklar:
        mail.sendmail(mesaj["From"], her_bir_mail, mesaj.as_string())
        print("{} adresine mail gönderildi..".format(her_bir_mail))
    print("Mailler başarıyla gönderildi...")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu...")
    sys.stderr.flush()