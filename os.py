import os

for yol,isim,dosya in os.walk("C:/Users/elsez/OneDrive/Masaüstü"):
    for i in dosya:
        if(i.endswith(".pdf")):
            print(i)