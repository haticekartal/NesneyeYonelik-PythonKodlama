# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 6: ANAHTAR KELİMELER                                                       # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 6: Anahtar kelimeler ---")     # Örneğin başlığını yazdırır
import keyword                                    # Anahtar kelime listesini içeren keyword modülünü projeye dahil eder
print("Anahtar kelime sayısı:", len(keyword.kwlist))  # Listedeki eleman sayısını yazdırır -> 35
print(keyword.kwlist)                             # Tüm anahtar kelimeleri liste hâlinde yazdırır
print(keyword.iskeyword("for"))                   # "for" anahtar kelime mi? -> True
print(keyword.iskeyword("yas"))                   # "yas" anahtar kelime mi? -> False (değişken adı olabilir)
print(keyword.iskeyword("True"))                  # "True" anahtar kelime mi? -> True (büyük harfle başlar)
print(keyword.iskeyword("true"))                  # "true" anahtar kelime mi? -> False (küçük harfle farklıdır)
# for = 3                                         # HATA ÖRNEĞİ: anahtar kelime değişken adı olamaz -> SyntaxError
class_ = "10-A"                                   # Anahtar kelimeyi kullanmak gerekirse sonuna _ eklenir
print("Sınıf:", class_)                           # Sınıf: 10-A yazdırır


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 7: BÜYÜK/KÜÇÜK HARF DUYARLILIĞI                                            # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 7: Büyük/küçük harf ---")      # Örneğin başlığını yazdırır
yas = 16                                          # küçük harfli yas
Yas = 30                                          # Büyük Y ile başlayan Yas: farklı bir değişken
YAS = 99                                          # Tamamı büyük harfli YAS: yine farklı bir değişken
print(yas, Yas, YAS)                              # 16 30 99 yazdırır; üçü ayrı değişkendir
# print(YAs)                                      # HATA ÖRNEĞİ: böyle bir değişken yok -> NameError


# ------------------------------------------------------------------------------  # Bölüm ayırıcı
# ÖRNEK 8: İYİ İSİM SEÇMEK                                                          # Örneğin başlığı
# ------------------------------------------------------------------------------  # Bölüm ayırıcı
print("\n--- ÖRNEK 8: İyi isimler ---")           # Örneğin başlığını yazdırır
k = 3600                                          # Kötü isim: k'nin ne olduğu anlaşılmıyor
m = k * 24                                        # Kötü isim: m'nin ne olduğu anlaşılmıyor
saatteki_saniye = 3600                            # İyi isim: değerin ne olduğunu anlatıyor
gunluk_saniye = saatteki_saniye * 24              # İyi isim: kod kendini açıklıyor
print(m, gunluk_saniye)                           # İkisi de 86400 yazdırır; sonuç aynı, okunabilirlik farklı
