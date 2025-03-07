def sil():
    site_sil = input("Lütfen silmek istediğiniz adresi yazın: ")

    # Dosyayı oku
    with open("dosya.txt", "r", encoding="utf8") as f:
        satirlar = f.readlines()

    yeni_satirlar = []
    bulundu = False

    for satir in satirlar:
        satir = satir.strip()  

       
        if not satir or '|' not in satir:
            yeni_satirlar.append(satir + '\n')
            continue

       
        try:
            site, sifre, user = satir.split("|")
        except ValueError:
            print(f"Hatalı format: {satir}")
            yeni_satirlar.append(satir + '\n')  
            continue  

 
        if site_sil == site:
            bulundu = True
            print(f"{site} silindi.")
        else:
            yeni_satirlar.append(satir + '\n')  

    if not bulundu:
        print(f"Site {site_sil} bulunamadı.")

 
    with open("dosya.txt", "w", encoding="utf8") as f:
        f.writelines(yeni_satirlar)

