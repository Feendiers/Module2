import math


# TODO: Подробно описать три произвольных класса

# TODO: описать класс

class LocalTrain:
    """
    Класс описывает пригородный электропоез(электричка)
    у данного класса три атрибута, а именно маршрут,
    количество вагонов и скорость в данный момент.
    Пример использования:
    >>> trein1 = Local_train('Финляндский-НевскаяДубровка', 8, 60)
    >>> trein1.change_speed(-40)
    Скорость уменьшена на 40 км/ч и теперь составляет 20 км/ч
    20
    >>> print(trein1.direction(5))
    НевскаяДубровка
    """

    def __init__(self, itinerary: str, number_of_wagons: int, speed: (float, int)):
        """
        Конструктор, создает объект класса
        :param itinerary: Маршрут следования, должен быть записан через - между двумя крайними точками
        :param number_of_wagons: Отвечает за количество вагонов, должен быть целым положительным числом
        :param speed: Отвечает за текущую скорость(км/ч), может быть любым числом
        """
        # Проверка переданных аргументов
        if not isinstance(itinerary, str) or '-' not in itinerary:
            raise TypeError("Маршрут следования должен быть строкой, "
                            "а также - должен присутвовать в обозначении маршрута")
        if not isinstance(number_of_wagons, int) or number_of_wagons <= 0:
            raise ValueError("Количество вагонов должно быть целым положительным числом")
        if not isinstance(speed, (float, int)):
            raise TypeError
        # Присждение значений аргументов характеристикам объекта
        self.itinerary = itinerary
        self.number_of_wagons = number_of_wagons
        self.speed = speed

    def direction(self, num: int):
        """
        Генератор выбора текущего направления, если передан параметр, кратный двум
        Вовращает напрвление до -, если нет, то после
        :param num: Вводимое целое положительное число, отвечает за выбор напрвления
        :return: Возвращается строковый объект, отвечающий на текущее направление
        """
        # Проверка аргумента
        if not isinstance(num, int) or num <= 0:  # Проверка переданного значения
            raise ValueError('в качестве параметра необходимо передать целое положительное число')

        i = num % 2  # Определяют остаток деления параметра на 2
        if i == 0:
            direction = self.itinerary[:self.itinerary.index('-')]
        else:
            direction = self.itinerary[self.itinerary.index('-') + 1:]
        return direction

    def change_speed(self, change: (float, int)):
        """
        Метод отвечает за изменение скорости
        после выполнения выводит отчет о произошедших изменениях
        :param change: Отвечает за то насколько меняется скорость
        :return: Возвращает текущее значение скорости
        """
        # Проверка правильности переданного параметра
        if not isinstance(change, (float, int)):
            raise TypeError
        self.speed += change  # Операция изменения скорости
        # В зависимости от того увеличена или уменьшена скорость
        # выводится сообщение о произошедших изменениях
        if change < 0:
            print(f'Скорость уменьшена на {abs(change)} км/ч и теперь составляет {self.speed} км/ч')
        else:
            print(f'Скорость увеличена на {change} км/ч и теперь составляет {self.speed} км/ч')
        return self.speed


# TODO: описать ещё класс
class Triangle:
    """
    Класс описывает треугольник
    во время создания объекта класса в качестве аргументов
    передаются название их 3-х символов и длины 3 сторон, длины сторон необходимо
    присуждать в соответсвии с названием тоесть для треугольника (ABC, 3, 4, 5)
    сторона AB = 3, BC = 4, CA = 5
    Пример работы:
    >>> tre1 = Triangle('ABC', 6, 8, 10)
    >>> tre1.square()
    Площадь треугольника ABC = 24.0
    24.0
    >>> tre1.find_angle('B')
    Угол B треугольника ABC = 90.0
    90.0
    """

    def __init__(self, name: str, side1: (int, float), side2: (int, float), side3: (int, float)):
        """
        Конструктор предназначенный для создания объекта класса
        :param name: Строка из 3-х символов, обозначающая название треугольника
        :param side1: Длина стороны 1(1 и 2 символы названия)
        :param side2: Длина стороны 2(2 и 3 символы названия)
        :param side3: Длина стороны 3(3 и 1 символы названия)
        """
        # Проверка переданных параметров
        if not isinstance(name, str) or len(name) != 3 or len(set(name)) != len(name):
            raise TypeError("Название треугольника должно быть строкой из трех различных символов")
        if not isinstance(side1, (int, float)) or side1 <= 0:
            raise ValueError("Длина стороны 1 должна быть положительным числом")
        if not isinstance(side2, (int, float)) or side2 <= 0:
            raise ValueError("Длина стороны 2 должна быть положительным числом")
        if not isinstance(side3, (int, float)) or side3 <= 0:
            raise ValueError("Длина стороны 3 должна быть положительным числом")

        # Присуждение значений параметров в характеристики объекта класса
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def square(self):
        """
        Функция подсчета площади треугольника
        в результате выполнения выводит сообщение
        :return: Возвращает найденное значение площади типа float
        """
        p = (self.side1 + self.side2 + self.side3) / 2  # Определение полупериметра
        S = (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5  # Нахождение площади по формуле
        print(f'Площадь треугольника {self.name} = {S}')  # Вывод сообщения оо проведенной операции
        return S

    def find_angle(self, name_of_angle: str):
        """
        Функция нахождения угла треугольника в градусах
        :param name_of_angle: Объект типа str должен состоять из одного символа входящего в название треугольника
        :return: Возвращает значение найденного угла в градусах, объект типа float
        """
        # Проверка аргумента функции
        if not isinstance(name_of_angle, str) or len(name_of_angle) != 1 or name_of_angle not in self.name:
            raise ValueError("Название угла должно состоять из одного символа, "
                             "который должен входить в название треугольника")
        # Подсчет размера угла в соответсвии с его расположением при помощи теоремы косинусов
        if name_of_angle == self.name[0]:
            angel = round(math.acos((self.side1 ** 2 + self.side3 ** 2 - self.side2 ** 2)
                                    / (2 * self.side1 * self.side3)) * 57.3, 1)
        elif name_of_angle == self.name[1]:
            angel = round(math.acos((self.side1 ** 2 + self.side2 ** 2 - self.side3 ** 2)
                                    / (2 * self.side1 * self.side2)) * 57.3, 1)
        elif name_of_angle == self.name[2]:
            angel = round(math.acos((self.side3 ** 2 + self.side2 ** 2 - self.side1 ** 2)
                                    / (2 * self.side3 * self.side2)) * 57.3, 1)
        print(f'Угол {name_of_angle} треугольника {self.name} = {angel}')  # Выведение сообщения
        return angel


# TODO: и ещё один
class House:
    """
    Класс для описания дома
    создается при помощи двух аргументов: материала из которого он построен и количества этажей
    Пример использования:
    >>> house1 = House('Дерево', 4)
    >>> house1.decide_type()
    'Multifamily house'
    >>> house1.change_floor(3, '-')
    Количество этажей уменьшенно на 3, и теперь составляет 1
    >>> house1.decide_type()
    'Private'
    """

    def __init__(self, material: str, floors: int):
        """
        Конструктор, отвечающий за создание объекта класса
        :param material: Объекта типа str, отвечает за описание материала
        :param floors: Объект типа int, отвечает за количество этажей и должен быть целым положительным числом
        """
        # Проверка переданных аргументов
        if not isinstance(material, str):
            raise TypeError("Материал из которого построен дом должен быть строкой")
        if not isinstance(floors, int) or floors <= 0:
            raise ValueError("Количество этажей должно быть целым положительным числом")
        # Присуждение значений параметров в характеристики объекта класса
        self.material = material
        self.floors = floors

    def change_floor(self, num: int, action: str):
        """
        Функция для изменения количества этажей дома
        :param num: Количетсов этажей для изменения(тип int) должен не превыщать изначальное количество этажей если
        планируется их уменьшение, а также быть целым положительным числом
        :param action: Аргумент типа str должен быть либо '-', либо '+', отвечает за дейстие соответсвенно '+' -
        добавить, '-' - убавить
        :return: None, функция ничего не возвращает, только выводит сообщение об операции и выполняет изменение
        характеристик внутри объекта класса
        """
        # Проверка переданных параметров
        if not isinstance(num, int) or num < 0:
            raise ValueError(
                "Количество этажей, с которыми совершается действие должно быть целым не отрицательным числом")
        if not isinstance(action, str) or action not in ['+', '-']:
            raise ValueError("Действие должно быть строкой и соответсвовать двум варантам: + или -")
        # Выполнения действия с этажами
        if action == '+':
            self.floors += num
            print(f'Количество этажей увеличенно на {num}, и теперь составляет {self.floors}')
        else:
            if num > self.floors:  # Проверка того что необходимо снести меньше этажей чем было изначально
                raise ValueError("Количество этажей для сноса не должно превышать изначальное количество")
            self.floors -= num
            print(f'Количество этажей уменьшенно на {num}, и теперь составляет {self.floors}')

    def decide_type(self):
        """
        Функция выполнеяет определение типа дома в зависимости от текущего количества этажей
        :return: Возвращает объект типа str обозначающий тип дома
        """
        if self.floors < 3:
            typ = 'Private'
        else:
            typ = 'Multifamily house'
        return typ
