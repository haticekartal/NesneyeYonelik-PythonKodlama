# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 9: TEMEL VERİ TİPLERİ                                                       # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 9: Veri tipleri ---")          # Örneğin başlığını yazdırır
tam_sayi = 16                                     # int: tam sayı
ondalikli = 1.68                                  # float: ondalıklı sayı (ayırıcı nokta, virgül değil)
metin = "Elif"                                    # str: metin
mantiksal = True                                  # bool: True veya False
bos_deger = None                                  # NoneType: değer yok
karmasik = 3 + 4j                                 # complex: karmaşık sayı (j sanal kısmı gösterir)
print(type(tam_sayi))                             # <class 'int'> yazdırır
print(type(ondalikli))                            # <class 'float'> yazdırır
print(type(metin))                                # <class 'str'> yazdırır
print(type(mantiksal))                            # <class 'bool'> yazdırır
print(type(bos_deger))                            # <class 'NoneType'> yazdırır
print(type(karmasik))                             # <class 'complex'> yazdırır


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 10: SAYILAR (int ve float)                                                 # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 10: Sayılar ---")              # Örneğin başlığını yazdırır
ogrenci = 30                                      # int
sicaklik = -5                                     # Negatif int
buyuk = 1_000_000                                 # Alt çizgi yalnızca okunabilirlik içindir; değer 1000000
fiyat = 49.90                                     # float
bilimsel = 2.5e3                                  # Bilimsel gösterim: 2.5 x 10 üzeri 3 = 2500.0
print(ogrenci, sicaklik, buyuk, fiyat, bilimsel)  # 30 -5 1000000 49.9 2500.0 yazdırır
print(7 + 2, 7 - 2, 7 * 2)                        # Toplama, çıkarma, çarpma -> 9 5 14
print(7 / 2)                                      # Bölme: sonuç her zaman float -> 3.5
print(7 // 2)                                     # Tam bölme: ondalık kısım atılır -> 3
print(7 % 2)                                      # Mod: bölümden kalan -> 1
print(2 ** 10)                                    # Üs alma: 2 üzeri 10 -> 1024
print(0.1 + 0.2)                                  # Ondalıklı sayılarda küçük yuvarlama farkı -> 0.30000000000000004
print(round(0.1 + 0.2, 2))                        # round() ile 2 basamağa yuvarlama -> 0.3


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 11: METİNLER (str)                                                          # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 11: Metinler ---")             # Örneğin başlığını yazdırır
ad = "Elif"                                       # Çift tırnakla metin
soyad = 'Yılmaz'                                  # Tek tırnakla metin; ikisi de aynıdır
adres = "Atatürk Cad. No: 5\nAnkara"           # \n metnin içinde yeni satıra geçmeyi sağlar
tam_ad = ad + " " + soyad                         # + ile metinleri birleştirme
print(tam_ad)                                     # Elif Yılmaz yazdırır
print(adres)                                      # Adresi iki satır hâlinde yazdırır
print(len(ad))                                    # Metnin karakter sayısı -> 4
print(ad[0])                                      # İlk karakter (sıra 0'dan başlar) -> E
print(ad[-1])                                     # Son karakter -> f
print(ad.upper())                                 # Büyük harfe çevirir -> ELIF (Türkçe İ değil, I olur!)
print(ad.lower())                                 # Küçük harfe çevirir -> elif
print("-" * 20)                                   # Metni 20 kez tekrarlar -> --------------------
print(f"Ad: {ad}, harf sayısı: {len(ad)}")        # f-string: { } içindeki ifadeler metne yerleşir


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 12: MANTIKSAL DEĞERLER (bool) VE None                                       # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 12: bool ve None ---")         # Örneğin başlığını yazdırır
gecti = True                                      # True büyük harfle başlar
devamsiz = False                                  # False büyük harfle başlar
print(gecti, devamsiz)                            # True False yazdırır
puan = 72                                         # Karşılaştırma için bir puan
print(puan >= 50)                                 # 72, 50'den büyük veya eşit mi? -> True
print(puan == 100)                                # 72, 100'e eşit mi? -> False
print(bool(0), bool(""))                          # 0 ve boş metin False sayılır -> False False
print(bool(5), bool("a"))                         # Sıfır olmayan sayı ve dolu metin True sayılır -> True True
telafi_notu = None                                # Öğrenci telafiye girmedi: not henüz yok
print(telafi_notu)                                # None yazdırır
print(telafi_notu is None)                        # Değer yok mu? diye kontrol eder -> True


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 13: type() VE isinstance()                                                  # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 13: Tip kontrolü ---")         # Örneğin başlığını yazdırır
print(type(16))                                   # <class 'int'>
print(type("16"))                                 # <class 'str'>: tırnak içindeki her şey metindir!
yas = 16                                          # Kontrol edilecek değişken
print(isinstance(yas, int))                       # yas bir int mi? -> True
print(isinstance(yas, str))                       # yas bir str mi? -> False


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 14: TİP DÖNÜŞÜMÜ                                                            # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 14: Tip dönüşümü ---")         # Örneğin başlığını yazdırır
print(int("25") + 5)                              # "25" metni sayıya çevrilir, 5 eklenir -> 30
print(float("3.5"))                               # "3.5" metni ondalıklı sayıya çevrilir -> 3.5
print(str(100) + " TL")                           # 100 sayısı metne çevrilip birleştirilir -> 100 TL
print(int(3.99))                                  # int() yuvarlamaz, ondalık kısmı keser -> 3
print(round(3.99))                                # round() en yakın tam sayıya yuvarlar -> 4
print(int("05321234567"))                         # Telefon numarası sayıya çevrilirse baştaki 0 kaybolur -> 5321234567
# print(int("on altı"))                           # HATA ÖRNEĞİ: sayıya çevrilemeyen metin -> ValueError
# print("16" + 1)                                 # HATA ÖRNEĞİ: metin ile sayı toplanamaz -> TypeError


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 15: DEĞERE GÖRE DOĞRU TİPİ SEÇMEK                                          # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 15: Doğru tip seçimi ---")     # Örneğin başlığını yazdırır
ogrenci_sayisi = 32                               # Sayılabilen tam değer -> int
urun_fiyati = 49.90                               # Ondalık kısmı olan değer -> float
ad_soyad = "Elif Yılmaz"                          # Metin -> str
telefon = "05321234567"                           # Rakamlardan oluşsa da hesap yapılmaz, baştaki 0 korunmalı -> str
sinavi_gecti = True                               # Yalnızca iki durumu var -> bool
girilmemis_not = None                             # Henüz değeri olmayan bilgi -> None
print(ogrenci_sayisi, urun_fiyati, ad_soyad)      # İlk üç değeri yazdırır
print(telefon, sinavi_gecti, girilmemis_not)      # Son üç değeri yazdırır


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 16: AÇIKLAMA SATIRLARI                                                     # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 16: Açıklama satırları ---")   # Örneğin başlığını yazdırır
# Bu satır tamamen bir açıklamadır; Python bunu çalıştırmaz.  # Tek satırlık açıklama örneği
yaricap = 4          
PI =3.14159                             # Kodun sağına yazılan açıklama: santimetre cinsinden
alan = PI * yaricap ** 2                          # Daire alanı hesaplanır
# print("deneme")                                 # Yorum yapılan kod çalışmaz; geçici devre dışı bırakma
print("Alan:", alan)                              # Alan: 50.26544 yazdırır
"""Üç tırnak arasındaki metin de açıklama gibi kullanılabilir."""  # Bir değişkene atanmadığı için etkisizdir


def alan_hesapla(r):                              # Fonksiyon tanımı (Modül 3'te ayrıntılı göreceğiz)
    """Yarıçapı verilen dairenin alanını döndürür."""  # docstring: fonksiyonun ne yaptığını anlatan açıklama
    return PI * r ** 2                            # Hesaplanan alanı geri döndürür


print("Fonksiyonla alan:", alan_hesapla(4))       # Fonksiyonu 4 ile çağırır -> 50.26544
print(alan_hesapla.__doc__)                       # Fonksiyonun docstring açıklamasını yazdırır


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# UYGULAMA 1: ÖĞRENCİ BİLGİ KARTI                                                  # Uygulamanın başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- UYGULAMA 1: Öğrenci bilgi kartı ---")  # Uygulamanın başlığını yazdırır
OKUL_ADI = "Atatürk Anadolu Lisesi"               # Sabit: okulun adı
ad = "Elif"                                       # str: öğrencinin adı
soyad = "Yılmaz"                                  # str: öğrencinin soyadı
sinif = 10                                        # int: sınıf seviyesi
ortalama = 87.5                                   # float: not ortalaması
burslu_mu = True                                  # bool: burs durumu
print("=" * 30)                                   # 30 adet = karakterinden çizgi çizer
print(OKUL_ADI)                                   # Okul adını yazdırır
print(f"Öğrenci : {ad} {soyad}")                  # Ad ve soyadı yazdırır
print(f"Sınıf   : {sinif}")                       # Sınıfı yazdırır
print(f"Ortalama: {ortalama}")                    # Ortalamayı yazdırır
print(f"Burslu  : {burslu_mu}")                   # Burs durumunu yazdırır
print("=" * 30)                                   # Kartı kapatan çizgi
