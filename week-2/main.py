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


def exit():
    """

    :return tüm listeyi bastırır ve sistemden çıkış yapar:
    """
    for i in names:
        print(i)
    print("çıkış yapılıyor...")
    exit(0)


def learnSchoolNumber():
    """

    :return öğrencinin okul numarasını verir:
    """
    name = input("öğrencinin adını ve soyadını giriniz:")
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
        print("böyle bir öğrenci bulunamadı")


def register():
    """

    :return öğrenciyi sisteme kaydeder:
    """
    name = input("öğrencinin adını ve soyadını giriniz:")
    names.append(name.lower())
    for i in names:
        count = 0
        for j in names:
            if i == j:
                count += 1

    if count >= 2:
        print("öğrenci sistemde kayıtlıdır")
        names.remove(j)
    else:
        print("öğrenci sisteme eklenmiştir.")


def delete():
    """

    :return öğrencinin kaydını siler:
    """
    if len(names) != 0:
        select = input("Silinecek elemanı giriniz:")
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
            print("seçilen eleman silindi")
            print(names)
        else:
            print("Seçili eleman listede bulunmamaktadır...")

    else:
        print("Listede eleman bulunmamaktadır")


def control(list, value):
    """
    bir öğrenci silinecekse listede daha önceden var olup olmadığı kontrol edilir
    eğer bir öğrencinin okul numarası öğrenilecekse daha önceden sistemde kayıtlı olup olmadığına bakılır
    :param verileri içinde tutan liste:
    :param kontrol edilecek değişken:
    :return listede var olup olmaması:
    """
    for i in list:
        if i == value:
            return True
        else:
            continue
    return False


names = []
while True:
    choice = int(input(
        "Yapmak istediğiniz işlemi seçiniz:\n1-Öğrenci ekleme\n2-Öğrenci silme\n3-Öğrencinin okul numarasını öğren\n4-Sistemden çıkış\n:"))
    match choice:
        case 1:
            register()
        case 2:
            delete()
        case 3:
            learnSchoolNumber()
        case 4:
            exit()
