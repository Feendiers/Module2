class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        # Проверка переданных в конструктор параметров
        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        if not isinstance(author, str):
            raise TypeError('Автор книги должен быть типа str')
        # Делаю характеристики объекта класса закрытыми
        self.__name = name
        self.__author = author
    # Создаю геттер для характеристики имени книги
    @property
    def name(self):
        return self.__name
    # Создаю геттер для характеристики автора книги
    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):    # Делаю класс производным от базового Book
    def __init__(self, name: str, author: str, pages: int):
        # Делаю проверку для переданного в конструктор параметра
        if not isinstance(pages, int):
            raise TypeError("Количество страниц книги должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        super().__init__(name, author)    # Наследую конструктор базового класса
        self.__pages = pages    # Делаю характеристку отвечающую за страницу скрытой
    # Создаю геттер для страниц книги
    @property
    def pages(self):
        return self.__pages

    # Создаю сеттер для страниц книги
    @pages.setter
    def pages(self, pages: int):
        # Добавляю проверку для присуждаемого парметра значению характеристики
        if not isinstance(pages, int):
            raise TypeError("Количество страниц книги должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.__pages = pages

    # Наследую метод __str__ от базового класса
    def __str__(self):
        return super().__str__() + f". Cтраницы: {self.pages}"

    # Перегружаю метод __repr__
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        # Проверка переданного парметра в конструктор
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        super().__init__(name, author)    # Наследование конструктора у базового класса
        # Делаю характеристику класса скрытой
        self.__duration = duration

    # Создаю геттер для продолжительности книги
    @property
    def duration(self):
        return self.__duration
    # Cоздаю сеттер для продолжительности книги
    @duration.setter
    def duration(self, duration: float):
        # Проверка присуждаемого характеристике значения
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self.__duration = duration    # Присуждение нового значения

    # Наследую метод __str__ от базового класса
    def __str__(self):
        return super().__str__() + f". Продолжительность: {self.pages}"

    # Перегружаю метод __repr__
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

