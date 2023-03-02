"""Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.

Формат входных данных
На вход программе подается одно целое число – длина ребра.

Формат выходных данных
Программа должна вывести текст и числа в соответствии с условием задачи.

Примечание. Объём куба и площадь полной поверхности можно вычислить по формулам V = a**3, S = 6a**2"""

# Формулы:
# V = a ** 3  Объем куба
# S = 6 * a ** 2  Площадь полной поверхности

a = int(input())
v = a ** 3  # Объем куба
s = 6 * a ** 2  # Площадь полной поверхности
print(f'Объем куба = {v}')
print(f'Площадь полной поверхности = {s}')