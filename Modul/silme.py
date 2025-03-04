def sil():
    yeni_satirlar=[]
    girdi=input("Lütfen silmek istediğiniz adresi yazın: ")
    with open("dosya.txt","r",encoding="utf8") as dosya : 
        
        satirlar=dosya.readlines()
         
        for a in satirlar:
            site,sifre,user=a.strip().split("|")

            if girdi==site:
                continue
            yeni_satirlar.append(a)

    with open("dosya.txt", "w", encoding="utf8") as dosya:
        for satir in yeni_satirlar:
            dosya.write(satir + "\n") 
