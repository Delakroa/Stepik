"""В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет
номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 1).

Формат входных данных
На вход программе подаётся целое число – место с заданным номером в вагоне.

Формат выходных данных
Программа должна вывести одно число – номер купе, в котором находится указанное место.
"""


# coupe1 = [1, 2, 3, 4]
# coupe2 = [5, 6, 7, 8]
# coupe3 = [9, 10, 11, 12]
# coupe4 = [13, 14, 15, 16]
# coupe5 = [17, 18, 19, 20]
# coupe6 = [21, 22, 23, 24]
# coupe7 = [25, 26, 27, 28]
# coupe8 = [29, 30, 31, 32]
# coupe9 = [33, 34, 35, 36]


def place_in_the_car() -> int:
    """Мое задание на собеседование которое я провалил"""
    data_input = int(input("Введите номер места в вагоне купе: "))
    coupe = data_input // -4
    return -coupe


print(place_in_the_car())
