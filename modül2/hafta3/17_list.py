# UYGULAMA 25: Kullanıcıdan alınan isimleri listeye ekleme

# Başlangıçta boş bir liste oluşturalım
isimler = []

# Kullanıcıdan 3 isim alalım
for i in range(3):

    # Kullanıcıdan isim alınır
    isim = input("Öğrenci adını giriniz: ")

    # Girilen isim listeye eklenir
    isimler.append(isim)

# Listeyi ekrana yazdıralım
print("Öğrenci listesi:", isimler)

# Listedeki isimleri alt alta yazdıralım
for isim in isimler:
    print(isim)