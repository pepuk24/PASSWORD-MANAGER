

# print("                               ╔══════════════════════════════════════════════╗")
# print("                               ║                                              ║")
# print("                               ║             PASSWORD MANANGER                ║")
# print("                               ║                                              ║")
# print("                               ╚══════════════════════════════════════════════╝")

# print("                               ╔══════════════════════════════════════════════╗")
# print("                               ║                                               ║") 
# print("                               ║        1 - Şifre Ekle                        ║")
# print("                               ║                                              ║")
# print("                               ║        2 - Şifreleri Listele                 ║")
# print("                               ║                                              ║")                             
# print("                               ║        3 - Şifre Ara                         ║")
# print("                               ║                                              ║")
# print("                               ║        4 - Şifre Güncelle                    ║") 
# print("                               ║                                              ║") 
# print("                               ║        5 - Şifre Sil                         ║") 
# print("                               ║                                              ║")
# print("                               ║        6 - Çıkış                             ║")
# print("                               ║                                              ║")      
# print("                               ║                                              ║")
# print("                               ║         SEÇİMİNİZİ YAPINIZ                   ║")
# print("                               ║                                              ║")
# print("                               ╚══════════════════════════════════════════════╝")



# def ekleme():
#     site=input("Lütfen gireceginiz site ismini giriniz(örnek gmail.com,hotmail.com) ")
#     sifre=input("Lutfen güçlü bir şifre giriniz(max 8 karakter) ")
#     user=input("Lütfen kullanıcı adınızı giriniz: ")
#     if len(sifre) < 8:
#         print("Şifre en az 8 karakterli olmalı!!!")
#     else:

#         with open("dosya.txt","a",encoding="utf8") as x:
#             x.write(f"{site}|{sifre}|{user}\n")

          
#             print(f"{site} için şifre başarıyla oluşturuldu....")




# def listele():
#     with open("dosya.txt","r",encoding="utf8") as x :
#         z=x.readlines()

#     print("SİTE:          ŞİFRE :          KULLANICI ADI:")
#     print("-----------------------------------------------------------")


#     for satir in z:
#         if not satir.strip():
#             continue

#         try:
#             site,sifre,user=satir.strip().split("|")
#             print(f"{site:<15} {sifre:<15}{user:<15}")

#         except ValueError:
#             print(f"Hata: {satir.strip()} formati yanlış.Lütfen dosyayı kontrol et")

       

# def arama():
#     anahtar=input("Herhangi birisini giriniz(Site ismi),(Şifre),(Kullanıcı ismi): ")
#     with open("dosya.txt","r",encoding="utf8") as x :    
#         bulundu=False 
#         z=x.readlines()
#         for satir in z:
#             if anahtar in satir:
#                 site,sifre,user=satir.strip().split("|")
#                 print(f"Site:{site} | Şifre:{sifre} | Kullanıcı adı:{user}")
#                 bulundu=True

#         if not bulundu:
#             print("╔══════════════════════════╗")
#             print("║ 🚫  K∆YIT BU£UN∆M∆DI! 🚫 ║")
#             print("╚══════════════════════════╝")
        
# def guncelleme():
#     guncelle=input("LÜtfen şifresini güncelliyeceğiniz Siteyi giriniz: ")
    

#     with open("dosya.txt","r",encoding="utf8") as w : 
#             z=w.readlines() 
#     yeni_satirlar=[]
#     bulundu=False
#     for satir in z:
#         site,sifre,user=satir.strip().split("|")
#         if guncelle ==site:
#             yeni_sifre=input("Lütfen yeni şifreyi giriniz: ")
                
#             yeni_satir=f"{site}|{yeni_sifre}|{user}\n"
#             bulundu=True
#         else:
#             yeni_satir=satir
#         yeni_satirlar.append(yeni_satir)

#     if not bulundu:
#             print("╔══════════════════════════╗")
#             print("║ 🚫  K∆YIT BU£UN∆M∆DI! 🚫 ║")
#             print("╚══════════════════════════╝") 
        
#     with open("dosya.txt","w",encoding="utf8") as dosya : 
#         dosya.writelines(yeni_satirlar)    
      





# def silme():
#     yeni_satirlar=[]
#     girdi=input("Lütfen silmek istediğiniz adresi yazın: ")
#     with open("dosya.txt","r",encoding="utf8") as dosya : 
        
#         satirlar=dosya.readlines()
         
#         for a in satirlar:
#             site,sifre,user=a.strip().split("|")

#             if girdi==site:
#                 continue
#             yeni_satirlar.append(a)

#     with open("dosya.txt", "w", encoding="utf8") as dosya:
#         for satir in yeni_satirlar:
#             dosya.write(satir + "\n") 
# silme()         