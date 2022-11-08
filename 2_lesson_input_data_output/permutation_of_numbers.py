""" Перестановка цифр.
Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел,
образованных при перестановке цифр заданного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.

Формат выходных данных
Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке:
abc,acb,bac,bca,cab,cba."""

numbers = int(input())
a = numbers // 100
b = (numbers // 10) % 10
c = numbers % 10

print(f'{a}{b}{c}')
print(f'{a}{c}{b}')
print(f'{b}{a}{c}')
print(f'{b}{c}{a}')
print(f'{c}{a}{b}')
print(f'{c}{b}{a}')


# ---------------------------------------------------------------------------------------------------

# Вариант сокурсников. Тут str по условю задачи нужно int.
# Ставить int в принтах некрасиво и не верно по условию задачи.
a, b, c = input()
print(a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a, sep='\n')

# -------------------------------------------------------------------------------------------------------

# Тут тоже самое разбивается строка, а потом склеивается. По условию не верно.
a = input()
b = a[0]
c = a[1]
d = a[2]
print(b + c + d, b + d + c, c + b + d, c + d + b, d + b + c, d + c + b, sep='\n')
