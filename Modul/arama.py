def ara():
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



ara()