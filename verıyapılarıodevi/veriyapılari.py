class Dugum:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None


class BagliListe:
    def __init__(self):
        self.baslangic = None

    def ekle(self, veri):
        yeni_dugum = Dugum(veri)
        if self.baslangic is None:
            self.baslangic = yeni_dugum
        else:
            son_dugum = self.baslangic
            while son_dugum.sonraki:
                son_dugum = son_dugum.sonraki
            son_dugum.sonraki = yeni_dugum

    def sil(self, indeks):
        if self.baslangic is None:
            print("Liste boş!")
            return
        if indeks == 0:
            self.baslangic = self.baslangic.sonraki
            return
        dugum = self.baslangic
        onceki_dugum = None
        for i in range(indeks):
            onceki_dugum = dugum
            dugum = dugum.sonraki
            if dugum is None:
                print("Geçersiz indeks!")
                return
        onceki_dugum.sonraki = dugum.sonraki

    def eleman_sayisi(self):
        sayac = 0
        dugum = self.baslangic
        while dugum:
            sayac += 1
            dugum = dugum.sonraki
        return sayac

    def ters_yazdir1(self, dugum):
        if dugum is None:
            return
        self.ters_yazdir1(dugum.sonraki)
        print(dugum.veri)

    def ters_yazdir(self):
        print("Listenin ters hali:")
        self.ters_yazdir1(self.baslangic)

    def ara(self, veri):
        indeks = 0
        dugum = self.baslangic
        while dugum:
            if dugum.veri == veri:
                print(f"{veri} listenin {indeks}. elemanında.")
                return
            indeks += 1
            dugum = dugum.sonraki
        print(f"{veri} listede yok!")


liste = BagliListe()

while True:
    print("\n1-Listeye ekle\n2-Listeden sil\n3-Eleman sayısını göster\n4-Ters çevirip yazdır\n5-Arama yap\n6-Çıkış")
    secim = int(input("Seçiminiz: "))

    if secim == 1:
        veri = input("Eklenecek veri: ")
        liste.ekle(veri)
    elif secim == 2:
        indeks = int(input("Silinecek elemanın indeksi: "))
        liste.sil(indeks)
    elif secim == 3:
        print(f"Listedeki eleman sayısı: {liste.eleman_sayisi()}")
    elif secim == 4:
        liste.ters_yazdir()
    elif secim == 5:
        veri = input("Aranacak veri: ")
        liste.ara(veri)
    elif secim == 6:
        print("Program sonlandırıldı.")
        break
    else:
        print("Geçersiz Seçim")

