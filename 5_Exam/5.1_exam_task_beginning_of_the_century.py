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


