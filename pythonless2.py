#python intro less 2

#degisken tipleri,operatorler,ifadeler

#OPERATORLER  VE IFADELER

#less 1 de en bilindik 4 operatoru (+,-,*,/) kullandık.
#less 2 de gormedigimiz tum degisken tipi ve operatorleri yorum satırı olarak ekli halde kodlayarak aktarıyorum.

# "**" bir ifadenin ussunu almak istiyorsak cift * kullaniriz

a=15**4 #burada a degiskeni 15*15*15*15in atandigi bir degisken.
print("a'nin degeri:",a) #15 sayisinin 4. kuvvetini verir

# "%" bir sayinin modunu almaya yarar. yani bir sayının bir sayıya bolundugunde verdigi kalani gosterir

c=15%4 # 15 sayisi 4'e bolundugunde 3 kalanını verir,yani ekrana 3 degeri gelecek
print("mod sonucu:",c)

# "==" operatoru esit mi? kontrolu yapar ve size true yada false yani dogru yada yanlis olarak bir ifade dondurur
d=5
k=15
print("d,k'ya esit mi?",d==k)

#"!=" esit degil mi kontrolu yapar. yukaridaki iki deger uzerinden gidersek ekrana true bastırmalı cunku d ifadesi k dan farklı
print("d,k'ya esit degil mi?",d!=k)

#<,> operatorleri de bir sayı bir sayıdan kucukturu yada buyukturu temsil eder. ekrana yine true yada false seklinde bir ifade gelir
#ki biz bu tip ifadelere yukaridan a hatirlamak gerekirse "boolean degerler" deriz.


print("a,5'ten buyuktur:",a>5)
print("a,156'dan kucuktur:",a<156)

#"<=" ve ">=" operatorleri kucuk esit ve buyuk esit durumlarini ifade eder.

sayi = 5
if sayi <= 5 :
    print("sayi 5'ten kucuktur.",sayi)
else:
    print("sayi 5'ten buyuktur.",sayi)
