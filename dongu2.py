 #####ATM sistemi######

bakiye=15000
dogru_sifre="1562"
hak=3

while hak>0:
    sifre=input("Lütfen 4 rakamdan oluşan şifrenizi giriniz.")
    if len(sifre) != 4:
        print("Şifreniz 4 haneli olmak zorundadır.")
        continue
    if not sifre.isdigit():
        print("Şifre rakamlardan oluşmak zorundadır.")
        continue

    if sifre==dogru_sifre:
        print("Hoşgeldiniz!")

        while True:
            #print("Yapmak istediğiniz işlemi seçiniz:\n1-Bakiye Sorgulama \n2-Para Çekme \n3-Çıkış Yap")
            secim=input("Yapmak istediğiniz işlemi seçiniz:\n1-Bakiye Sorgulama \n2-Para Çekme \n3-Çıkış Yap\n")
            
            if secim == "1" :
                print(f"Bakiyeniz: {bakiye}")
                menu=input("Çıkış yapmak için 4'ü, ana menüye dönmek için 5'i tuşlayınız. tuşlayınız.")
                if menu=="4":
                    break
                if menu=="5":
                    continue
                if menu != "4" or menu != "5" :
                    print("Hatalı tuşlama!")
                    break
            
            elif secim == "2" :
                istenen_tutar=int(input("Çekmek istediğiniz miktarı giriniz: "))

                if istenen_tutar > bakiye:
                    print("Yetersiz bakiye!")
                
                else:
                    bakiye -= istenen_tutar
                    print(f"Hesabınızdan {istenen_tutar}₺ çekilmiştir. Kalan bakiyeniz: {bakiye}")
                menu=input("Çıkış yapmak için 4'ü, ana menüye dönmek için 5'i tuşlayınız.")
                if menu=="4":
                    break
                if menu=="5":
                    continue
                if menu != "4" or menu != "5" :
                    print("Hatalı tuşlama!")
                    break
            
            elif secim == "3" :
                print("Çıkış yapılıyor. Hoşça kalın!")
                break
            else:
                print("Yanlış tuşlama yapılmıştır. Tekrar deneyiniz.")
        break
    else:
        hak-=1
        print(f"Hatalı şifre, kalan hakkınız: {hak}")

if hak==0:
    print("3 kere yanlış girdiniz! Kartınız bloke oldu.")