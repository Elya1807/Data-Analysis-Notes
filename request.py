import requests
from bs4 import BeautifulSoup

url =  "https://www.paribucineverse.com/" # Site linkimiz
response =  requests.get(url ) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

 # Bu kullanımın anlamı div etiketlerinden class'ı yp-poi-box-2 yi al anlamına geliyor.
for i  in soup.find_all("div",{"class":"movie-info"}):
    print(i.text)
