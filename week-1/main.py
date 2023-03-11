"""
Veri tipleri

int=değeri tam sayı olan değişkenlerin veri tipi.

float=değeri ondalıklı olan değişkenleri veri tipi

complex=karmaşık sayıların veri tipidir.burda x= 2+9j ise x'in veri tipi complextir.

str=tek tırnak veya çift tırnak içine yazılan her şey bir strdir.
 içinde sayı veya harf olmasının bir önemi yoktur.

list=arraylere benzer ama burda belli bir değişken tipinde olaması gerekmez farklı değişken tiplerine
sahip elemanlardan da oluşabilir.

tuple=değiştirebilme durumu hariç listin özelliklerini taşır.sıralıdır(indexine erişilebilir).
bu veri tipinin sadece değerleri okunabilir değerler üzerinde bir oynama yapılamaz.

range=belli bir aralık verildikten sonra o yere kadarlık kısmı bir liste olarak oluşturur.

dict=belli keyler ve bu keylerin tuttuğu valuelardan oluşan bir veri tipidir.
listeden farkı listelerde elemana index ile erişilirken dictte key değeri ile erişilmesidir.

set=matematikteki kümelere benzer aynı değerde ve veri tipinde değeri istediğiniz kadar eklemeye çalışın
 sadece bir tanesini gösterir.sırasızdır(indexle çalışan metotlar burada istenilen işlemleri doğru yapmaz
  çünkü elemanları indexlemez.) elemanları tek tek ekleme/çıkarma yapabilir.


bool=bir durumun gerçekleşme eya doğruluk durumuna göre 2 değer alır.True/ False

NoneType=değeri bulunmayan değişkenlerin veri tipidir.
"""
#şartlandırma durumuna örnek olarak ilerleme durumunu sorgulayan soruya bağlı olarak ilerleme oranının artması/değişemesi
status=50
progress=input("bölümü bitirdiniz mi?\nBitirdiyseniz evet\nbitirmediyseniz hayır yazınız:")
isDone=progress.lower()=="evet"
if isDone:
    status+=10
    print("Bölümü bitirdiniz.İlerleme puanınız {}".format(status))
else:
    print("Maalesef bölümü tamamlayamadınız.İlerleme puanınız {}".format(status))
