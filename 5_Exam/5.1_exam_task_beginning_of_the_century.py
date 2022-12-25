# Начало столетия

# Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается,
# то выведите «YES», иначе выведите «NO».
#
# Формат входных данных
# На вход программе подаётся натуральное число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

a = int(input())
if a % 100 == 0:
    print("YES")
else:
    print("NO")

# ------------------------------------------------------------------------------------------------------------

# Шахматная доска
#
# Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет.
# Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».
#
# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой
# клетки, потом для второй клетки.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if (x1 + x2 + y1 + y2) % 2 == 0:
    print("YES")
else:
    print("NO")

# ------------------------------------------------------------------------------------------------------------

# Girls only
#
# Футбольная команда набирает девочек от 10 до 15 лет включительно. Напишите программу, которая запрашивает возраст
# и пол претендента, используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина) и определяет
# подходит ли претендент для вступления в команду или нет. Если претендент подходит, то выведите «YES», иначе выведите
# «NO».
#
# Формат входных данных
# На вход программе подаётся натуральное число – возраст претендента и буква обозначающая пол m (мужчина) или f
# (женщина).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

age = int(input())
gender = str(input())
if 10 <= age <= 15 and gender == "f":
    print("YES")
else:
    print("NO")

# ------------------------------------------------------------------------------------------------------------

# Римские цифры

# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число
# находится вне диапазона 1-10, то программа должна вывести текст «ошибка».
#
# В таблице приведены римские цифры для чисел от 1 до 10.

# Формат входных данных
# На вход программе подаётся целое число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

number = int(input())
if 1 <= number <= 10:
    if number == 1:
        print("I")
    elif number == 2:
        print("II")
    elif number == 3:
        print("III")
    elif number == 4:
        print("IV")
    elif number == 5:
        print("V")
    elif number == 6:
        print("VI")
    elif number == 7:
        print("VII")
    elif number == 8:
        print("VIII")
    elif number == 9:
        print("IX")
    elif number == 10:
        print("X")
else:
    print("ошибка")


# Второй вариант

n = int(input())
if not 0 < n < 11:
    print('ошибка')
elif n < 4:
    print(n*'I')
elif n == 4:
    print('IV')
elif n < 9:
    print('V' + (n-5)*'I')
elif n < 11:
    print((10-n)*'I' + 'X')

# ------------------------------------------------------------------------------------------------------------

# YES or NO вот в чем вопрос
#
# Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
#
# Условия:
#
# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».
# Формат входных данных
# На вход программе подаётся натуральное число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

number = int(input())
if 2 <= number <= 5 and number % 2 == 0:
    print("NO")
elif 6 <= number <= 20 and number % 2 == 0:
    print("YES")
elif 20 < number and number % 2 == 0:
    print("NO")
else:
    print("YES")

# ------------------------------------------------------------------------------------------------------------

# Ход слона.

# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с
# первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер
# столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если
# из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.
#
# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Шахматный слон ходит по диагоналям.

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if x1 - y1 == x2 - y2 or x1 - y1 == y1 + y2 or x1 + x2 == y1 + y2:
    print("YES")
elif x1 + y1 != x2 + y2:
    print("NO")
else:
    print("NO")

# ------------------------------------------------------------------------------------------------------------

# Ход коня
#
# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь попасть с первой
# клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер
# строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом
# коня можно попасть во вторую или «NO» в противном случае.
#
# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Шахматный конь ходит буквой «Г».

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 1 and x1 != x2 and y1 != y2:
    print("YES")
else:
    print("NO")

# ------------------------------------------------------------------------------------------------------------
