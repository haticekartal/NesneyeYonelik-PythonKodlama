# UYGULAMA : Listedeki notların analizini yapma

# Öğrencilerin sınav notları
notlar = [60, 75, 90, 85, 100]

# Notların toplamını hesaplayalım
toplam = sum(notlar)

# Öğrenci sayısını bulalım
ogrenci_sayisi = len(notlar)

# Not ortalamasını hesaplayalım
ortalama = toplam / ogrenci_sayisi

# En yüksek notu bulalım
en_yuksek = max(notlar)

# En düşük notu bulalım
en_dusuk = min(notlar)

# Sonuçları ekrana yazdıralım
print("Notlar:", notlar)
print("Toplam:", toplam)
print("Ortalama:", ortalama)
print("En yüksek not:", en_yuksek)
print("En düşük not:", en_dusuk)