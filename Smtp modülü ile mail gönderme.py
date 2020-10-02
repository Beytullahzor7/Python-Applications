import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj= MIMEMultipart()

mesaj["From"] = "beytullahzor7@gmail.com"

mesaj["To"] = "beytullahzor7@gmail.com"

mesaj["subject"] = "Smtp Mail Gönderme"

yazi = """

Smtp ile mail gönderiyorum

Beytullah ZOR

"""

mesaj_govdesi = MIMEText(yazi,"plain")


mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587) #hangi gmail severine baglanmak sitedigimi ilk deger olarak veriyorum
#virgülden sonraki 587 yazan kısım ise serverin portunu belirtir

    mail.ehlo() #smtp serverine kendimizi tanıttık

    mail.starttls() #kullanıcı bilgilerimizin şifrelenmesini sağladık


    #bu iki fonk. kullanmazsak mailimiz kesinlikle gitmeyecektir

    mail.login("beytullahzor7@gmail.com","Beytullah55?")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Basarıyla Gönderildi...")

    mail.close()


except:
    sys.stderr.write("Bir sorun olustu!")

    sys.stderr.flush()
    
