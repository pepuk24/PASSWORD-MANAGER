def listele():
    with open("dosya.txt","r",encoding="utf8") as x :
        z=x.readlines()

    print("SİTE:          ŞİFRE :          KULLANICI ADI:")
    print("-----------------------------------------------------------")


    for satir in z:
        if not satir.strip():
            continue

        try:
            site,sifre,user=satir.strip().split("|")
            print(f"{site:<15} {sifre:<15}{user:<15}")

        except ValueError:
            print(f"Hata: {satir.strip()} formati yanlış.Lütfen dosyayı kontrol et")

       

def arama():
    anahtar=input("Herhangi birisini giriniz(Site ismi),(Şifre),(Kullanıcı ismi): ")
    with open("dosya.txt","r",encoding="utf8") as x :    
        bulundu=False 
        z=x.readlines()
        for satir in z:
            if anahtar in satir:
                site,sifre,user=satir.strip().split("|")
                print(f"Site:{site} | Şifre:{sifre} | Kullanıcı adı:{user}")
                bulundu=True

        if not bulundu:
            print("╔══════════════════════════╗")
            print("║ 🚫  K∆YIT BU£UN∆M∆DI! 🚫 ║")
            print("╚══════════════════════════╝")