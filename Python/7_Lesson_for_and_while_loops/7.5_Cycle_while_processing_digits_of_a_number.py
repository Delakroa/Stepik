# ��������� ���� �����

# ��� �������� ����� ����� (��� ������ int), �� �������� ��� �������� �������������� ������� // � �������� ����������
# ������� �� ������� ������ ������ ����� �� ������ %. ��������� ���� while � ��� ������ ��������, ����� ���������� �����
# ����� � ������������ ����������� �������� (����).
#
# ����� ���� ����������� ����� n. �����:

# ����������� �������� n % 10 � �������� ��������� ����� �����;
# ����������� �������� n // 10 � �������� ����� � ��������� ��������� ������.

# ������� ���������, ������� ��������� ����������� ����� (����� �������������) � ������������ ��� �����.

n = int(input())
while n != 0:  # ���� � ����� ���� �����
    last_digit = n % 10  # �������� ��������� �����
    # ��� ��������� ��������� �����
    n = n // 10  # ������� ��������� ����� �� �����

# ���� while �������� �� ��� ��� ���� � ����� ���� �������������� �����. ���� ����� ��������:

# 1. ��������� ��������� ��������� ����� last_digit = n % 10;
# 2. ��� ��������� ��������� �����;
# 3. ��������� �������� ��������� ����� �� ����� n = n // 10.

# � �������� ��������� ��������� ����� ���� ���, ��� ������: ����� ����, ���������� �����, ������������ ����, ����������
# ���������� ��� ���������� �����, ������� ���� ��������������� ���������� ������� � �.�.
#
# ������� ���������, ������� ���������� ���� �� � ����� ����� 7.

num = int(input())
has_seven = False  # ���������� �����

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')

# ----------------------------------------------------------------------------------------------------------------

# �������� ������� 1
#
# ���� ����������� �����. �������� ���������, ������� ������� ��� ����� � ������� � �������� �������.
#
# ������ ������� ������
# �� ���� ��������� �������� ���� ����������� �����.
#
# ������ �������� ������
# ��������� ������ ������� ����� ���������� ����� � ������� � �������� �������.

n = int(input())
while n != 0:
    last_digits = n % 10
    n //= 10
    print(last_digits)

# ----------------------------------------------------------------------------------------------------------------

# �������� ������� 2
#
# ���� ����������� �����. �������� ���������, ������� ������ ������� ���� ����� �� ��������.
#
# ������ ������� ������
# �� ���� ��������� �������� ���� ����������� �����.
#
# ������ �������� ������
# ��������� ������ ������� �����, ���������� � �������� �������.

n = int(input())
while n != 0:
    last_digits = n % 10
    n //= 10
    print(last_digits, end='')

# ----------------------------------------------------------------------------------------------------------------

# max � min
#
# ���� ����������� ����� n,( n >= 10). �������� ���������, ������� ���������� ��� ������������ � ����������� �����.
#
# ������ ������� ������
# �� ���� ��������� �������� ���� ����������� �����.
#
# ������ �������� ������
# ��������� ������ ������� ������������ � ����������� ����� ���������� ����� (� ���������� ��������).

num: int = int(input())
min_num = 9
max_num = 0
while num != 0:
    last_digit = num % 10
    if last_digit < min_num:
        min_num = last_digit
    if last_digit > max_num:
        max_num = last_digit
    num //= 10
print('������������ ����� �����', max_num)
print('����������� ����� �����', min_num)

# ----------------------------------------------------------------------------------------------------------------

# ��� ������

# ���� ����������� �����. �������� ���������, ������� ���������:

# ����� ��� ����;
# ���������� ���� � ���;
# ������������ ��� ����;
# ������� �������������� ��� ����;
# ��� ������ �����;
# ����� ��� ������ � ��������� �����.
# ������ ������� ������
# �� ���� ��������� �������� ���� ����������� �����.

# ������ �������� ������
# ��������� ������ ������� �������� ��������� ������� � ��������� �������.

number = int(input())
count_sum = 0  # ������� �����
quantity_counter = 0  # ���-��
product_counter = 1  # ������������
first_digit = 0  # ������� ��� ��������� �����
last_digit = number % 10  # ��������� �����
while number != 0:
    digit = number % 10  # ����� ���� �������� � ����� �� ������� ������ �����
    first_digit = digit
    count_sum += digit  # �����
    quantity_counter += 1  # ������� ���-��
    product_counter *= digit  # ������������
    average = count_sum / quantity_counter
    sum_f_l = first_digit + last_digit
    number //= 10  # ������� ��������� �����
print(count_sum)
print(quantity_counter)
print(product_counter)
print(average)
print(first_digit)
print(sum_f_l)

# ----------------------------------------------------------------------------------------------------------------

# ������ �����

# ���� ����������� ����� n(n > 9). �������� ���������, ������� ���������� ��� ������ (� ������) �����.

# ������ ������� ������
# �� ���� ��������� �������� ���� ����������� �����, ��������� ��� ������� �� ���� ����.

# ������ �������� ������
# ��������� ������ ������� ��� ������ (� ������) �����.

n = int(input())
while n > 9:
    last_digit = n % 10
    n //= 10
print(last_digit)

# ----------------------------------------------------------------------------------------------------------------
