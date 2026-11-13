# UYGULAMA 32: Öğrenci bilgilerini TXT dosyasına kaydetme

# Kullanıcıdan bilgileri alıyoruz
ad = input("Öğrencinin adını giriniz: ")
yas = input("Öğrencinin yaşını giriniz: ")

# Dosyayı yazma modunda açıyoruz
with open("ogrenci.txt", "w", encoding="utf-8") as dosya:

    # Öğrenci bilgilerini yazıyoruz
    dosya.write("Öğrenci adı: " + ad + "\n")
    dosya.write("Öğrenci yaşı: " + yas)

print("Öğrenci bilgileri kaydedildi.")