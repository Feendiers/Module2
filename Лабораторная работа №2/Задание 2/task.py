
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


# TODO: написать класс Book
class Book:
    """
    Класс служит для описания книги
    """
    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор, служит для создания объекта класса
        :param id_: идентификатор книги тип int
        :param name: Название книги тип str
        :param pages: Количество страниц в книге, тип int, должен быть больше 0
        """
        # Проверка переданных в конструктор параметров
        if not isinstance(id_, int):
            raise TypeError("Идентификатор должен быть целым числом типа int")
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str (строкой)")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть целым положительным числом типа int")
        # Создание характеристик объекта класса и присуждение им значений
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Метод создает строку которая сообщает название книги
        для отображения информации об объекте класса для пользователей
        к примеру в функциях print, str
        :return: объект str формата Книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Метод возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        для отображения информации об объекте класса в режиме отладки
        :return: str формата "Book(id_=1, name='test_name_1', pages=200)"
        """
        return f"{self.__class__.__name__}(id_={self.id_}, name=\'{self.name}\', pages={self.pages})"
# TODO: написать класс Library
class Library:
    """
    Класс для работы с массивом объектов типа Book
    """
    def __init__(self, books=None):
        """
        Конструктор для создания объекта класса
        :param books: объект типа list, содержит массив объектов Book
        """
        if books == None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        :return: если len(self.books) == 0, тогда 1, иначе id последней книги +1
        """
        # Проверка на содержание объектов внутри массива
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):
        """
        Метод для проверки существования книги с списке
        :param id_: int, должен быть валидным для создания объекта типа Book
        :return: id книги если она существует и возращает ошибку если нет
        """
        # Проверка переданных параметров
        if not isinstance(id_, int):
            raise TypeError("Идентификатор должен быть целым числом типа int")
        for i in self.books:
            if i.id_ == id_:    # Проверка соответсвия характеристики объекта и переданного id
                return self.books.index(i)

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
