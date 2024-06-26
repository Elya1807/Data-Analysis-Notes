
#ÖNEMLİ NOT: Ders Videodaki IMDB web sitesi arka kodaları değiştiği için videdaki işlemleri yapamadım.
# Benzer web sitesi bulup yapmaya çalıştım orda da yeni değişikliğinden dolayı bir takım hata çıktı sonucunda.
# Ama genel mantığı anladım.

import requests

from bs4 import BeautifulSoup

url = "https://www.sinemalar.com/filmler/en-iyi-filmler"

response = requests.get(url)

html_içeriği = response.content

soup = BeautifulSoup(html_içeriği,"html.parser")

a = float(input("Rting giriniz: "))

basliklar = soup.find_all("div",{"class":"name"})
ratingler = soup.find_all("div",{"class","right-top-info"})

for baslik, rating in zip(basliklar,ratingler):

    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if(float(rating)>a):
        print("Film ismi: {} Filmin Ratingi: {}".format(baslik,rating))