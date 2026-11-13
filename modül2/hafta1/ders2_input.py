# Kullanıcıdan adını alalım
ad = input("Adınızı girin: ")
# Kullanıcıdan doğum yılını alalım
dogum_yili = int(input("Doğum yılınızı girin: "))
# Yaşı hesaplayalım
yas = 2026 - dogum_yili
# Sonucu ekrana yazdıralım
print("Merhaba", ad)
print("Yaşınız:", yas)



# --------------------------------------------------
# UYGULAMA 2: KDV'Lİ FİYAT HESAPLAMA
# --------------------------------------------------
print("\n--- UYGULAMA 2: KDV hesaplama ---")

# KDV oranını tanımlayalım (%20)
KDV_ORANI = 0.20

# Kullanıcıdan ürün bilgilerini alalım
urun = input("Ürün adı: ")
fiyat = float(input("Fiyat (TL): "))
adet = int(input("Adet: "))

# KDV hariç toplam tutarı hesaplayalım
ara_toplam = fiyat * adet

# KDV tutarını hesaplayalım
kdv = ara_toplam * KDV_ORANI

# KDV dahil toplam tutarı hesaplayalım
toplam = ara_toplam + kdv

# Sonuçları ekrana yazdıralım
print(f"\n{adet} adet {urun}")
print(f"Ara toplam: {ara_toplam:.2f} TL")
print(f"KDV: {kdv:.2f} TL")
print(f"Toplam: {toplam:.2f} TL")

print("\nProgram bitti.")




#INPUT ISLEMLERI
ad = input("Adınızı girin: ")
print("Merhaba", ad)



#KLAVYEDEN GİRİLEN 2 SAYIYI TOPLAMA
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
toplam = sayi1 + sayi2
print("Toplam:", toplam)



#DİKDÖRTGEN ALANI
kisa_kenar = int(input("Kısa kenarı girin: "))
uzun_kenar = int(input("Uzun kenarı girin: "))
alan = kisa_kenar * uzun_kenar
print("Dikdörtgenin alanı:", alan)



#SAYININ KARESİNİ ALMA
sayi = int(input("Bir sayı girin: "))
kare = sayi ** 2
print("Sayının karesi:", kare)






#SAYININ KÜPÜNÜ ALMA
# Kullanıcıdan bir sayı alalım
sayi = int(input("Bir sayı girin: "))
# Sayının küpünü hesaplayalım
kup = sayi ** 3
# Sonucu ekrana yazdıralım
print("Sayının küpü:", kup)






#ADEDE GÖRE FİYAT BULMA
fiyat = float(input("Ürün fiyatını girin: "))
miktar = int(input("Kaç adet alacaksınız? "))

toplam = fiyat * miktar

print("Ödenecek tutar:", toplam, "TL")





#YAŞ HESAPLAMA
# Kullanıcıdan adını alalım
ad = input("Adınızı girin: ")
# Kullanıcıdan doğum yılını alalım
dogum_yili = int(input("Doğum yılınızı girin: "))
# Yaşı hesaplayalım
yas = 2026 - dogum_yili
# Sonucu ekrana yazdıralım
print("Merhaba", ad)
print("Yaşınız:", yas)



