def guncelle():
    guncelle=input("LÜtfen şifresini güncelliyeceğiniz Siteyi giriniz: ")
    

    with open("dosya.txt","r",encoding="utf8") as w : 
            z=w.readlines() 
    yeni_satirlar=[]
    bulundu=False
    for satir in z:
        site,sifre,user=satir.strip().split("|")
        if guncelle ==site:
            yeni_sifre=input("Lütfen yeni şifreyi giriniz: ")
                
            yeni_satir=f"{site}|{yeni_sifre}|{user}\n"
            bulundu=True
        else:
            yeni_satir=satir
        yeni_satirlar.append(yeni_satir)

    if not bulundu:
            print("╔══════════════════════════╗")
            print("║ 🚫  K∆YIT BU£UN∆M∆DI! 🚫 ║")
            print("╚══════════════════════════╝") 
        
    with open("dosya.txt","w",encoding="utf8") as dosya : 
        dosya.writelines(yeni_satirlar)   
        print("Şifreniz başarıyla kaydedildi...") 
      
