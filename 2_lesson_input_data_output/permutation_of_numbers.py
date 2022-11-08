""" Перестановка цифр.
Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел,
образованных при перестановке цифр заданного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.

Формат выходных данных
Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке:
abc,acb,bac,bca,cab,cba."""

numbers = int(input())
data = numbers // 10
a = data // 10
b = data % 10
c = numbers % 10

print(f'{a}{b}{c}')
print(f'{a}{c}{b}')
print(f'{b}{a}{c}')
print(f'{b}{c}{a}')
print(f'{c}{a}{b}')
print(f'{c}{b}{a}')