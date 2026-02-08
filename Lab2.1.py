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
        Raises:
            ValueError: Если id или pages отрицательные, или name пустая строка
        """
        if id_ <= 0:
            raise ValueError("ID книги должен быть положительным числом")
        self.id = id_
        if not name.strip():
            raise ValueError("Название книги не может быть пустой строкой")
        self.name = name
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages
    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        """Возвращает строку для инициализации экземпляра."""
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"
    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство двух книг по id, name и pages.
        Args:
            other (object): Другой объект для сравнения
        Returns:
            bool: True если книги равны, иначе False
        """
        if not isinstance(other, Book):
            return False
        return self.id == other.id and self.name == other.name and self.pages == other.pages

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
