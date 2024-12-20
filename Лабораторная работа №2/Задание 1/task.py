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
    Класс, служит для описания книги
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
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:      # Прверка что парметр отвечающий за страницы это положительное число
            raise ValueError("Количество страниц должно быть положительно")
        # Создание характеристик объекта класса и присуждение им значений
        self.id_ = id_
        self.name = name
        self.pages = pages

    # Создаю метод __str__ для отображения информации об объекте класса для пользователей
    # (например, для функций print, str)
    def __str__(self) -> str:
        """
        Метод создает строку которая сообщает название книги
        для отображения информации об объекте класса для пользователей
        к примеру в функциях print, str
        :return: объект str формата Книга "название_книги"
        """
        return f'Книга "{self.name}"'
    # Создаю метод __repr__ для отображения информации об объекте класса в режиме отладки
    def __repr__(self) -> str:
        """
        Метод возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        для отображения информации об объекте класса в режиме отладки
        :return: str формата "Book(id_=1, name='test_name_1', pages=200)"
        """
        return f"{self.__class__.__name__}(id_={self.id_}, name=\'{self.name}\', pages={self.pages})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
