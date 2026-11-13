# UYGULAMA 44: Basit alışveriş sepeti

# Alışveriş sepetini oluşturalım
sepet = []

# Menü sürekli gösterilsin
while True:

    print("\n----- ALIŞVERİŞ MENÜSÜ -----")
    print("1 - Ürün ekle")
    print("2 - Sepeti görüntüle")
    print("3 - Sepetteki ürün sayısını göster")
    print("4 - Çıkış")

    secim = input("Seçiminiz: ")

    # Kullanıcının seçimine göre işlem yapalım
    match secim:

        case "1":

            # Kullanıcıdan ürün adı alalım
            urun = input("Ürün adı: ")

            # Ürünü sepete ekleyelim
            sepet.append(urun)

            print("Ürün sepete eklendi!")

        case "2":

            # Sepetteki ürünleri yazdıralım
            print("Sepetiniz:", sepet)

        case "3":

            # Sepette kaç ürün var?
            print("Ürün sayısı:", len(sepet))

        case "4":

            # Programdan çıkalım
            print("Alışveriş tamamlandı.")
            break

        case _:
            print("Geçersiz seçim!")