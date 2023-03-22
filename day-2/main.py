"""
ÖDEV TANIMI:

Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

Bu öğrenci kayıt sistemine;

Aldığı isim soy isim ile listeye öğrenci ekleyen

Aldığı isim soy isim ile eşleşen değeri listeden kaldıran

Listeye birden fazla öğrenci eklemeyi mümkün kılan

Listedeki tüm öğrencileri tek tek ekrana yazdıran

Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan

Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)

fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.
"""


def exit1():
    """

    :return tüm listeyi bastırır ve sistemden çıkış yapar:
    """
    print("****All Students****")
    for i in names:
        print(i)
    print("logging out...")
    exit(1)


def learnSchoolNumber():
    """

    :return öğrencinin okul numarasını verir:
    """
    name = input("please enter student's name and surname:")
    name = name.lower()  # kontrol etmeyi kolaylaştırdığı için bu şekilde yaptım
    # bu kısımda kod tekrarı olmaması için control fonksiyonunu tanımladım
    # isHave=False
    # for i in names:
    #     if i==name:
    #         isHave=True
    #         break
    #     else:
    #         continue
    if control(names, name):
        print(names.index(name))
    else:
        print("student not exist")


def register():
    """

    :return öğrenciyi sisteme kaydeder:
    """
    name = input("please enter student's name and surname:")
    names.append(name.lower())
    for i in names:
        count = 0
        for j in names:
            if i == j:
                count += 1

    if count >= 2:
        print("student already registered")
        names.remove(j)
    else:
        print("registered.")


def delete():
    """

    :return öğrencinin kaydını siler:
    """
    if len(names) != 0:
        select = input("enter the name of the student to be deleted ")
        select = select.lower()
        # bu kısımda kod tekrarı olmaması için control fonksiyonunu tanımladım
        # aynı işlemler sadece parametreleri farklılık gösteriyor
        # for i in names:
        #     if i == select:
        #         isHas = True
        #         break
        #     else:
        #         continue
        if control(names, select):
            names.remove(select)
            print("student deleted")
            print(names)
        else:
            print("student not exist")

    else:
        print("no registered students ")


def control(list, value):
    """
    bir öğrenci silinecekse listede daha önceden var olup olmadığı kontrol edilir
    eğer bir öğrencinin okul numarası öğrenilecekse daha önceden sistemde kayıtlı olup olmadığına bakılır
    :param verileri içinde tutan liste:
    :param kontrol edilecek değişken:
    :return listede var olup olmaması:
    burada böyle bir fonk yerine index methodu ile try except kullanarak da yapabiliriz.
    # for i in list:
    #     if i == value:
    #         return True
    #     else:
    #         continue
    # return False
    index methodu aranılan değer varsa o değerin indexini verirken eğer yoksa hata veren bir methodtur. hata vermesi durumu için try-except kullandım.

    """
    try:
        index = list.index(value)
    except:
        return False
    else:
        return True


names = []
while True:
    choice = int(input("Please make a dicision:\n1-Register\n2-Remove\n3-Learn school number\n4-Exit\n:"))
    if choice > 0 and choice < 5:
        match choice:
            case 1:
                register()
            case 2:
                delete()
            case 3:
                learnSchoolNumber()
            case 4:
                exit1()
    else:
        print("Something went wrong...\nTry again")
