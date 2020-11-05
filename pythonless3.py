#python intro less 3

#VERI TIPLERI VE KULLANIMI

#veri tipleri nelerdir,donusum nasil yapilir?

note="veri tipleri onemlidir" #veri tipi stringtir
a=5 #veri tipi integerdir. (tam sayi)
b=15.85 #veri tipi floattir.(ondalik sayi)
c=5+3j #veri tipi complextir. (karmasik sayi)
d=["elma","cilek","armut"] #veri tipi listtir. (liste)
e=("elma","cilek","armut") #veri tipi tupledir. (demet)
f={"isim":"jasmine","yas":"18"} #veri tipi dictionarydir.(sozluk)
g=frozenset({"elma", "cilek", "armut"}) #veri tipi listdir fakat uzerinde degisiklik yapilamaz
#yani bu liste icine baska bir eleman ekleyip silemeziolani degistiremezsiniz
#bazen dongu durumlarinda listenin ilk halini korumasi icin gerekli bir fonksiyondur
h=True #veri tipi booleandır (mantiksal)
i=b"Nur" #veri tipi bytedir
j=bytearray(12) #veri tipi bytearraydir (bit dizisi)

print(a,b,c,d,e,f,g,h,i,j)
#verinin tipini kontrol etmek icin type() ifadesini kullaniriz
print("a degiskeninin tipi;",type(a))
print("d degiskeninin tipi;",type(d))

#verileri donusturmek
int() #tam sayiya donusturur
print(int(5.18))
float()#ondalik sayiya donusturur
print(float(5))
complex() #karmasik sayiya donustur
print(complex(12))
list() #listeye donusturur
print(list("kelime"))
tuple() #demete donusturur
frozenset() #dondurulmus,kisitlanmis kumeye donusturur
bool() #mantiksal veriye donusturur
print(chr(97)) #tam sayiyi karaktere donusturur
set() #verileri kumeye cevirir
print(ord("a"))#karakteri tam sayiya donusturur

