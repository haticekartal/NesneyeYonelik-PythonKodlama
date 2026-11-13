# UYGULAMA 11: Öğrencinin not ortalamasını hesaplama

# Ortalama hesaplayan fonksiyon
def ortalama_hesapla(not1, not2):
    ortalama = (not1 + not2) / 2
    return ortalama

# Kullanıcıdan notları alıyoruz
vize = float(input("Birinci notu giriniz: "))
final = float(input("İkinci notu giriniz: "))

# Fonksiyonu çağırıyoruz
ortalama = ortalama_hesapla(vize, final)

# Sonucu ekrana yazdırıyoruz
print("Not ortalaması:", ortalama)