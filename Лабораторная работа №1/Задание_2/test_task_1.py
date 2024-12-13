
# TODO: импортируйте классы, созданные в ходе выполнения прошлого задани
# Добавляю 3 класса из первого задания
from task_1 import Local_train
from task_1 import Triangle
from task_1 import House
if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    # Создаю объекты для всех трех классов
    train = Local_train('Невская_Дубровка-Финляндский_вокзал', 8, 60)
    tre = Triangle('ABC', 3, 4, 5)
    house = House('Камень', 5)
    # Пробую вызвать методы с неправильными аргументами
    try:    # TODO: вызвать метод с некорректными аргументами(b)
        train.direction(-5)
    except ValueError:
        print('Ошибка: неправильные данные')

     # TODO: вызвать метод с некорректными аргументами(a)
    try:
        house.change_floor(-5, 'y')
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        tre.find_angle('D')
    except ValueError:
        print('Ошибка: неправильные данные')

