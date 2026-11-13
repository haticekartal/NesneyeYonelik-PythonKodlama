#Foreach, bir koleksiyonun elemanlarını tek tek dolaşmak için kullanılır.
#Python'da ayrıca foreach adlı bir komut yoktur. Bunun yerine doğrudan for döngüsü kullanılır.

# UYGULAMA : Öğrenci isimlerini ekrana yazdırma
# Öğrenci listesi oluşturalım
ogrenciler = ["Ayşe", "Mehmet", "Zeynep", "Ahmet"]

# Listedeki her öğrenciyi dolaşalım
for ogrenci in ogrenciler:

    # Öğrenci ismini yazdıralım
    print("Öğrenci:", ogrenci)





# UYGULAMA: Listedeki sayıların karelerini hesaplama
sayilar = [2, 4, 6, 8, 10]

# Listedeki her sayıyı tek tek alalım
for sayi in sayilar:

    # Sayının karesini hesaplayalım
    kare = sayi ** 2

    # Sonucu yazdıralım
    print(sayi, "sayısının karesi:", kare)





# UYGULAMA: Bir kelimenin harflerini alt alta yazdırma

kelime = input("Bir kelime giriniz: ")

# Kelimenin her harfini dolaşalım
for harf in kelime:

    # Harfi ekrana yazdıralım
    print(harf)