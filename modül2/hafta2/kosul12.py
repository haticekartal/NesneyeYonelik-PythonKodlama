# Kullanıcıdan boy ve kilo bilgilerini alalım
boy = float(input("Boyunuzu metre cinsinden giriniz: "))
kilo = float(input("Kilonuzu kg cinsinden giriniz: "))

# Vücut kitle indeksini hesaplayalım
vki = kilo / (boy ** 2)

print("Vücut Kitle İndeksiniz:", round(vki, 2)) #virgülden sonra vki değerini 2 ondalık basamakla yazdırıyoruz

# VKİ değerine göre değerlendirme yapalım
if vki < 18.5:
    print("Zayıf")

elif vki < 25:
    print("Normal kilolu")

elif vki < 30:
    print("Fazla kilolu")

elif vki < 35:
    print("1. Derece obez")

elif vki < 40:
    print("2. Derece obez")

else:
    print("3. Derece obez")