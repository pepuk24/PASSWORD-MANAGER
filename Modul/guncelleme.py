def guncelle():
    guncelle = input("Lütfen şifresini güncelleyeceğiniz Siteyi giriniz: ")
    
    with open("dosya.txt", "r", encoding="utf8") as w:
        z = w.readlines()

    yeni_satirlar = []
    bulundu = False 

    for satir in z:
        satir = satir.strip()

       
        if not satir or '|' not in satir:
            yeni_satirlar.append(satir + '\n')
            continue

      
        try:
            site, sifre, user = satir.split("|")
        except ValueError:
            print(f"Hatalı satır atlandı: {satir}")
            yeni_satirlar.append(satir + '\n')
            continue

        if guncelle == site:
            yeni_sifre = input("Lütfen yeni şifreyi giriniz: ")
            yeni_satir = f"{site}|{yeni_sifre}|{user}\n"
            bulundu = True  
        else:
            yeni_satir = satir + '\n'

        yeni_satirlar.append(yeni_satir)

  
    if not bulundu:
        print("╔══════════════════════════╗")
        print("║ 🚫  K∆YIT BU£UN∆M∆DI! 🚫 ║")
        print("╚══════════════════════════╝") 
        return  

   
    with open("dosya.txt", "w", encoding="utf8") as dosya:
        dosya.writelines(yeni_satirlar)

    print(" Şifreniz başarıyla güncellendi!") 

guncelle()
