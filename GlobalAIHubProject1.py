class Library: # Library sınıfı oluşturulur
    def __init__(self):
        self.file_path = 'books.txt'
        self.file = open(self.file_path, 'a+') # a+ modu kullanılarak bir txt dosyası oluşturulur

    def __del__(self): # destructor methodu
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        for line in book_lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_year = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully!")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        updated_books = [line for line in book_lines if title_to_remove not in line]
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines('\n'.join(updated_books))
        print("Book removed successfully!")


# Ana Program
lib = Library() # sınıfı çağırıyoruz

while True: # tekrar tekrar menu gelsin diye while içine aldık
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Exit")

    choice = input("Enter your choice : ") # kullanıcı neyi seçerse if else ile denetliyoruz

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q':
        print("Exiting the program. Goodbye!")
        break
    else: # olaki geçersiz bir şey girer ise
        print("Invalid choice. Please enter a number between 1 and 3 or q.")
