# UYGULAMA 34: Öğrenci bilgilerini JSON dosyasına kaydetme

# JSON kütüphanesini ekliyoruz
import json

# Öğrenci bilgilerini sözlük olarak tanımlıyoruz
ogrenci = {
    "ad": "Ayşe",
    "yas": 20,
    "not": 85
}

# JSON dosyasını oluşturuyoruz
with open("ogrenci.json", "w", encoding="utf-8") as dosya:

    # Sözlüğü JSON dosyasına kaydediyoruz
    json.dump(ogrenci, dosya, ensure_ascii=False, indent=4)

print("Öğrenci bilgileri JSON dosyasına kaydedildi.")




# UYGULAMA 35: JSON dosyasındaki bilgileri okuma

# JSON kütüphanesini ekliyoruz
import json

# Önceki uygulamada oluşturduğumuz dosyayı açıyoruz
with open("ogrenci.json", "r", encoding="utf-8") as dosya:

    # JSON verilerini Python sözlüğüne dönüştürüyoruz
    ogrenci = json.load(dosya)

# Bilgileri yazdırıyoruz
print("Öğrenci adı:", ogrenci["ad"])
print("Öğrenci yaşı:", ogrenci["yas"])
print("Öğrenci notu:", ogrenci["not"])