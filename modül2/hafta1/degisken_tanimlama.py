# ==============================================================================  
# MODÜL 2 - DEĞİŞKENLER, VERİ TİPLERİ VE AÇIKLAMA SATIRLARI                         
# Python Programlama Kursu - Kod örnekleri                                         
# Hazırlayan: HATİCE KARTAL                                                        
# Çalıştırmak için terminalde: python ders1_degiskenler.py           # Dosyanın nasıl çalıştırılacağı
# ==============================================================================  


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 1: DEĞİŞKEN OLUŞTURMA VE KULLANMA                                          # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 1: Değişken oluşturma ---")    # Ekrana örneğin başlığını yazdırır (\n bir satır boşluk bırakır)
ad = "Elif"                                       # ad değişkenine "Elif" metnini atar (str)
soyad = "Yılmaz"                                  # soyad değişkenine "Yılmaz" metnini atar (str)
yas = 16                                          # yas değişkenine 16 tam sayısını atar (int)
boy = 1.68                                        # boy değişkenine 1.68 ondalıklı sayısını atar (float)
ogrenci_mi = True                                 # ogrenci_mi değişkenine True mantıksal değerini atar (bool)
print(ad, soyad)                                  # Ad ve soyadı aralarında boşlukla yazdırır -> Elif Yılmaz
print("Yaş:", yas)                                # Sabit metin ile değişkenin değerini birlikte yazdırır -> Yaş: 16
print("Boy:", boy)                                # Boy bilgisini yazdırır -> Boy: 1.68
print("Öğrenci mi:", ogrenci_mi)                  # Mantıksal değeri yazdırır -> Öğrenci mi: True
print("Gelecek yıl:", yas + 1)                    # yas + 1 hesaplanır ama yas değişmez -> Gelecek yıl: 17


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 2: DEĞİŞKENİN DEĞERİNİ DEĞİŞTİRMEK                                         # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 2: Değeri değiştirmek ---")    # Örneğin başlığını yazdırır
puan = 50                                         # puan değişkeni 50 değeriyle oluşturulur
print(puan)                                       # 50 yazdırır
puan = 80                                         # puan'a yeni değer atanır, eski değer (50) kaybolur
print(puan)                                       # 80 yazdırır
puan = puan + 10                                  # Önce sağ taraf hesaplanır (80 + 10), sonuç puan'a atanır
print(puan)                                       # 90 yazdırır
puan += 5                                         # Kısaltmalı atama: puan = puan + 5 ile aynıdır
print(puan)                                       # 95 yazdırır
puan -= 15                                        # puan = puan - 15 ile aynıdır
print(puan)                                       # 80 yazdırır
puan *= 2                                         # puan = puan * 2 ile aynıdır
print(puan)                                       # 160 yazdırır
puan /= 4                                         # puan = puan / 4 ile aynıdır; / sonucu her zaman float olur
print(puan)                                       # 40.0 yazdırır
puan = "Çok iyi"                                  # Aynı değişkene farklı tipte değer de atanabilir (önerilmez)
print(puan)                                       # Çok iyi yazdırır


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 3: ÇOKLU ATAMA VE DEĞER TAKASI                                             # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 3: Çoklu atama ---")           # Örneğin başlığını yazdırır
x, y, z = 10, 20, 30                              # Sağdaki değerler sırayla x, y ve z'ye atanır
print(x, y, z)                                    # 10 20 30 yazdırır
a = b = c = 0                                     # Üç değişkene aynı anda 0 değeri atanır
print(a, b, c)                                    # 0 0 0 yazdırır
sol, sag = "elma", "armut"                        # sol = "elma", sag = "armut" olur
print("Önce:", sol, sag)                          # Önce: elma armut yazdırır
sol, sag = sag, sol                               # İki değişkenin değerleri tek satırda yer değiştirir
print("Sonra:", sol, sag)                         # Sonra: armut elma yazdırır
# x, y = 1, 2, 3                                  # HATA ÖRNEĞİ: 2 değişkene 3 değer -> ValueError (bu yüzden yorumda)


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 4: SABİTLER                                                                # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 4: Sabitler ---")              # Örneğin başlığını yazdırır
PI = 3.14159                                      # Sabitler BÜYÜK harfle yazılır; pi sayısı
KDV_ORANI = 0.20                                  # KDV oranı sabiti (%20)
MAKS_DENEME = 3                                   # En fazla deneme hakkı sabiti
yaricap = 5                                       # Dairenin yarıçapı (değişken)
alan = PI * yaricap ** 2                          # Alan = pi x r kare; ** üs alma operatörüdür
print("Daire alanı:", alan)                       # Daire alanı: 78.53975 yazdırır
fiyat = 250                                       # Ürünün KDV hariç fiyatı
print("KDV dahil:", fiyat * (1 + KDV_ORANI))      # 250 x 1.20 -> KDV dahil: 300.0 yazdırır
print("Deneme hakkı:", MAKS_DENEME)               # Deneme hakkı: 3 yazdırır


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 5: DEĞİŞKEN İSİMLENDİRME KURALLARI                                         # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 5: Geçerli isimler ---")       # Örneğin başlığını yazdırır
isim = "Can"                                      # Geçerli: harfle başlıyor
_gizli = 42                                       # Geçerli: alt çizgi ile başlıyor
ogrenci_sayisi = 30                               # Geçerli: kelimeler alt çizgiyle ayrılmış (snake_case)
sinif2 = "10-A"                                   # Geçerli: rakam başta değil, sonda
toplamPuan = 450                                  # Geçerli ama Python'da snake_case (toplam_puan) tercih edilir
print(isim, _gizli, ogrenci_sayisi, sinif2, toplamPuan)  # Tüm geçerli değişkenleri yazdırır
# Aşağıdaki satırlar GEÇERSİZDİR; çalıştırılırsa SyntaxError verir, bu yüzden yorum içindedir:  # Uyarı
# 2sinif = "10-A"                                 # Geçersiz: rakamla başlıyor
# ogrenci sayisi = 30                             # Geçersiz: boşluk içeriyor
# ogrenci-sayisi = 30                             # Geçersiz: tire (-) içeriyor, Python bunu çıkarma sanır
# class = "Python"                                # Geçersiz: class bir anahtar kelime
# $fiyat = 99                                     # Geçersiz: $ özel karakteri içeriyor

