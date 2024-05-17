# GlobalAIHub-Project-1
Project for GlobalAIHub
# Library Management System

Bu proje, nesne tabanlı programlama tekniklerini kullanarak "Kütüphane Yönetim Sistemi" oluşturmanızı sağlar. Bu program, her biri bir kitabı temsil eden satırlarla doldurulan `books.txt` adlı bir dosyayı veritabanı olarak kullanacaktır. Her bir satırda kitap adı, yazar, yayın tarihi ve sayfa sayısı bulunacak ve bu bilgiler virgülle ayrılmış olacaktır.

1. **Library** Sınıfını Oluşturun:

    a. `__init__` metodu, `books.txt` dosyasını açmak için kullanılır ve dosyayı kapatmak için `__del__` metodunu içerir. 
    İpucu: Eğer "a+" modu ile `books.txt` dosyasını açarsanız, dosyayı hem okuma hem de dosyaya satır ekleyebilirsiniz. Ve ayrıca, `books.txt` daha önce oluşturulmamışsa, bu mod dosyayı oluşturacaktır.

2. Kütüphane sınıfına aşağıdaki yöntemleri ekleyin:

    a. **List Books (Kitapları Listele):**
        - Dosyanın içeriğini okuyun.
        - Satırları `splitlines()` yöntemi kullanarak bir listeye ekleyin.
        - Şimdi listenin her elemanı tek bir kitap hakkında bilgi içerir.
        - Bu bilgileri kullanarak kitap adlarını ve yazarları yazdırın.

    b. **Add Book (Kitap Ekle):**
        - Kullanıcıdan kitap başlığı, yazar, ilk yayın yılı ve sayfa sayısı için giriş isteyin.
        - Bu bilgileri içeren bir dize oluşturun. Kitap başlığı, yazar, yayın yılı ve sayfa sayısı arasına virgül ekleyin.
        - Bu satırı dosyaya ekleyin.

    c. **Remove Book (Kitap Kaldır):**
        - Kaldırılacak kitabın başlığını kullanıcıdan alın.
        - Dosya içeriğini okuyun ve kitapları bir liste içine ekleyin (list_books metodunu oluştururken yaptığınız gibi).
        - Kitabın endeksini listede bulun.
        - Kitabı listeden kaldırın.
        - `books.txt` dosyasının içeriğini temizleyin.
        - Liste elemanlarını `books.txt` dosyasına ekleyin.

3. `lib` adlı bir nesne oluşturun ve bu nesne ile etkileşimde bulunmak için bir menü oluşturun.

4. Kullanıcıdan menü öğesi girişi alın ve `lib` nesnesinin ilgili yöntemini çalıştırmak için if-elif-else ifadesini kullanarak kontrol edin.

**Kullanım:**

```python
# Library sınıfı örneği oluştur
lib = Library()

# Sonsuz döngü içinde menüyü göster
while True:
    print("\n*** MENU ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Kaldır")
    print("q) Çıkış")

    # Kullanıcıdan menü seçeneğini al
    choice = input("Lütfen seçiminizi girin: ")

    # Kullanıcının seçimine göre işlem yap
    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice.lower() == 'q':
        print("Programdan çıkılıyor. Hoşça kalın!")
        break
    else:
        print("Geçersiz seçim. Lütfen 1 ile 3 arasında bir sayı veya 'q' girin.")
