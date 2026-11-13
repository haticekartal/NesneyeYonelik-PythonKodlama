# UYGULAMA: Metindeki sesli harf, sessiz harf ve boşluk sayısını hesaplama

metin = "python ile programlama çok eğlenceli"

sesliler = "aeıioöuü"

harf = sesli = sessiz = bosluk = 0

for karakter in metin:
    if karakter == " ":
        bosluk += 1
    #karakterin harf olup olmadığını kontrol et
    elif karakter.isalpha():
        harf += 1

        if karakter in sesliler:
            sesli += 1
        else:
            sessiz += 1

print("Toplam karakter:", len(metin))
print("Harf:", harf, "| Sesli:", sesli, "| Sessiz:", sessiz)
print("Boşluk:", bosluk)