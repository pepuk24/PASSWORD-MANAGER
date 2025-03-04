def ekleme():
    site=input("Lütfen gireceginiz site ismini giriniz(örnek gmail.com,hotmail.com) ")
    sifre=input("Lutfen güçlü bir şifre giriniz(max 8 karakter) ")
    user=input("Lütfen kullanıcı adınızı giriniz: ")
    if len(sifre) < 8:
        print("Şifre en az 8 karakterli olmalı!!!")
    else:

        with open("dosya.txt","a",encoding="utf8") as x:
            x.write(f"{site}|{sifre}|{user}\n")

          
            print(f"{site} için şifre başarıyla oluşturuldu....")
