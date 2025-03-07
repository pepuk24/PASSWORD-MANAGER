from Modul.ekle import ekleme
from Modul.listeleme import listele
from Modul.arama import ara
from Modul.guncelleme import guncelle
from Modul.silme import sil

def anamenu():
    while True:  
        print("                               ╔══════════════════════════════════════════════╗")
        print("                               ║                                              ║")
        print("                               ║             PASSWORD MANANGER                ║")
        print("                               ║                                              ║")
        print("                               ╚══════════════════════════════════════════════╝")

        print("                               ╔══════════════════════════════════════════════╗")
        print("                               ║                                               ║") 
        print("                               ║        1 - Şifre Ekle                        ║")
        print("                               ║                                              ║")
        print("                               ║        2 - Şifreleri Listele                 ║")
        print("                               ║                                              ║")                             
        print("                               ║        3 - Şifre Ara                         ║")
        print("                               ║                                              ║")
        print("                               ║        4 - Şifre Güncelle                    ║") 
        print("                               ║                                              ║") 
        print("                               ║        5 - Şifre Sil                         ║") 
        print("                               ║                                              ║")
        print("                               ║        6 - Çıkış                             ║")
        print("                               ║                                              ║")      
        print("                               ║                                              ║")
        print("                               ║         SEÇİMİNİZİ YAPINIZ                   ║")
        print("                               ║                                              ║")
        print("                               ╚══════════════════════════════════════════════╝")

        secim = input("Lütfen seçiminizi yapınız: ")

        if secim == "1":
            ekleme()
        elif secim == "2":
            listele()
        elif secim == "3":
            ara()
        elif secim == "4":
            guncelle()
        elif secim == "5":
            sil()
        elif secim == "6":
            print("Çıkılıyor...")
            exit()  
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")
        
       
        input("Ana menüye dönmek için Enter'a basın...")


anamenu()
