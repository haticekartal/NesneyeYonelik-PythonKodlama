# UYGULAMA : Sayıları küçükten büyüğe sıralama

# Karışık sayılardan oluşan liste
sayilar = [45, 12, 89, 23, 5, 67]

# Listenin ilk halini yazdıralım
print("İlk liste:", sayilar)

# Sayıları küçükten büyüğe sıralayalım
sayilar.sort()

print("Küçükten büyüğe:", sayilar)

# Sayıları büyükten küçüğe sıralayalım
sayilar.sort(reverse=True)

print("Büyükten küçüğe:", sayilar)