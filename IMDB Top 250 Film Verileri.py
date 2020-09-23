import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_icerigi = response.content #response degiskeni içerisinden web sayfasının kaynagını almak

soup = BeautifulSoup(html_icerigi,"html.parser")

a = float(input("Rating'i giriniz:"))

baslıklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for baslık , rating in zip(baslıklar,ratingler):

    baslık=baslık.text
    baslık=baslık.strip() #basdaki ve sondaki boslukları siler
    baslık=baslık.replace("\n","") #\n yerine bosluk koyarız daha güzel bir görünüm için

    rating=rating.text
    rating=rating.strip()
    rating=rating.replace("\n","")

    if (float(rating) > a):
        print("Film İsmi: {} Film Ratingi: {}".format(baslık,rating))
        print("--------------->")
