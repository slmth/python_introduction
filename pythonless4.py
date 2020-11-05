#python intro less 4

#input almak,if/else if/else komutlari

#INPUT (GIRDI) ALMAK

#bir degiskene bir veri atamak icin = operatorunu kullanıyorduk
#burada bir degisken bize soruldugunda vermek istedigimiz degeri
#bize soruldugu zaman bilgisayara ogretmeyi deneyecegiz

#sayisal ifadelerin girsini almak
#tam sayı,ondalikli sayı vb farklı sayi tipleri icin kullanicidan girdi almak
#input kismindan once kullanicinin sadece tek tipte bir girdide bulunmasini istiyorsak bunu belirtiriz

sayi1=int(input("Bir tam sayı degeri giriniz:")) #tam sayidan farkli bir deger kabul etmez
sayi2=float(input("Ondalıklı bir deger giriniz:")) #ondalikli sayidan farkli bir deger kabul etmez
sayi3=complex(input("True ya da False degeri giriniz:")) #True ya da False haric herhangi bir girdiyi kabul etmez
#kompleks sayiyi imaginerde j kullanarak giriniz 5+j gibi

print(sayi1,sayi2,sayi3)

#sozel ifade(string) icin kullanicidan girdi almak
#sozel ifadeler icin herhangi bir belirtec eklemeye gerek yoktur
kelime=input("Herhangi bir kelime giriniz:")
print(kelime)

#IF,ELSE IF,ELSE KOMUTLARI

#if komutu program yazarken eger ciktilarimizi ya da program calismasını
#bir sart baglamak istersek kullandigimiz temel komuttur

#else komutu ise bizim istedigimizin tam aksinin yerine getirilip getirilmedigini kontrol eder

#if-else birbirlerinin zit birer tamamlayicisi,kontrolcusu konumundadir
#if ve else komutlari ardindan : kullanmak python icin gerekli bir durumdur
#ayni zamanda bir else durumu girilen bir ife bagliysa o ifle ayni seviyede yer almalidir
#bunun sebebi ic ice dongulerde sorun yasanmamasi ve else'in if'e olan bagliligindandir

a=int(input("Bir sayi giriniz:"))
if a==8:
    print("Girdiginiz sayi 8'e eşittir.Sayi:",a)
else:
    print("Girdiginiz sayi 8'e esit degildir.Sayi:",a)

#else if bize if durumundan farkli bir sarti daha kosabilme secenegi sunar
#yani bir durumun gerceklesmesi icin birden fazla gerekce isteyebilme olanagi saglar

b=int(input("Bir sayi giriniz:"))
if b>10:
    print("Girdiginiz sayi 10'dan buyuktur.Sayi:",b)
elif b==10:
    print("Girdiginiz sayi 10'a esittir.Sayi:",b)
else:
    print("Girdiginiz sayi 10'dan kucuktur.Sayi:",b)





    
