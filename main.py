import os

class Book:
    def __init__(self, book_id, title, author, year, status="в наличии"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"ID: {self.book_id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"

    def to_string(self):
        return f"{self.book_id};{self.title};{self.author};{self.year};{self.status}"


class Library:
    def __init__(self, filename='books.txt'):
        self.books = []
        self.next_id = 1
        self.filename = filename
        self.load_books()

    def add_book(self, title, author, year):
            # Проверка на наличие книги
        if any(book.title == title and book.author == author and book.year == year for book in self.books):
            print("Эта книга уже существует в библиотеке.")
            return
        new_book = Book(self.next_id, title, author, year)
        self.books.append(new_book)
        self.next_id += 1
        print(f"Книга '{title}' добавлена в библиотеку.")
        self.save_books()

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Книга '{book.title}' удалена из библиотеки.")
                self.save_books()
                return
        print("Книга с таким ID не найдена.")

    def find_book(self, title=None, author=None, year=None):
        results = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (year and year == book.year):
                results.append(book)
        return results

    def update_book_status(self, book_id, new_status):
        for book in self.books:
            if book.book_id == book_id:
                book.status = new_status
                print(f"Статус книги '{book.title}' изменен на '{new_status}'.")
                self.save_books()
                return
        print("Книга с таким ID не найдена.")

    def display_books(self):
        if not self.books:
            print("Библиотека пуста")
        else:
            for book in self.books:
                print(book)

    def save_books(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            for book in self.books:
                f.write(book.to_string() + '\n')


    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    book_id, title, author, year, status = line.strip().split(';')
                    book = Book(int(book_id), title, author, year, status)
                    self.books.append(book)
                    self.next_id = max(self.next_id, int(book_id) + 1)
            print("Книги загружены из файла.")
        else:
            print("Файл с книгами не найден, создается новая библиотека.")



def main():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)

        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)

        elif choice == '3':
            title = input("Введите название книги для поиска (или оставьте пустым): ")
            author = input("Введите автора книги для поиска (или оставьте пустым): ")
            year = input("Введите год издания для поиска (или оставьте пустым): ")
            results = library.find_book(title, author, year)
            if results:
                print("Найденные книги:")
                for book in results:
                    print(book)
            else:
                print("Книги не найдены.")

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ").strip().lower()
            if new_status in ["в наличии", "выдана"]:
                library.update_book_status(book_id, new_status)
            else:
                print("Неверный статус. Пожалуйста, введите 'в наличии' или 'выдана'.")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
