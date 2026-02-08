BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# TODO написать класс Book
class Book:
    """Класс, представляющий книгу."""
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализирует экземпляр книги.
        Args:
            id_ (int): Уникальный идентификатор книги
            name (str): Название книги
            pages (int): Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages
    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.
        Returns:
            str: Строка в формате 'Книга "название_книги"'
        """
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать экземпляр.
        Returns:
            str: Строка в формате 'Book(id_=..., name=..., pages=...)'
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

# TODO написать класс Library
class Library:
    """Класс, представляющий библиотеку книг."""
    def __init__(self, books: list[Book] = None):
        """
        Инициализирует экземпляр библиотеки.
        Args:
            books (list[Book], optional): Список книг. По умолчанию None (пустой список)
        """
        if books is None:
            self.books = []
        else:
            self.books = books
    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги.
        Returns:
            int: Следующий доступный идентификатор книги
        """
        if not self.books:  # Если список книг пустой
            return 1
        # Находим максимальный id среди всех книг и добавляем 1
        return max(book.id for book in self.books) + 1
    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её идентификатору.
        Args:
            book_id (int): Идентификатор книги для поиска
        Returns:
            int: Индекс книги в списке
        Raises:
            ValueError: Если книги с таким id не существует
        """
        # Используем enumerate для получения пар (индекс, книга)
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        # Если книга не найдена, вызываем ошибку
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
