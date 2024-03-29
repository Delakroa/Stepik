# ���� �����: ��������� ��� ������

# 1.��������� ��� ������ str
# 2.������� len() � str()
# 3.������������ �����
# 4.��������� ������ �� �����
# 5.�������� in
# 6.������� �����

# ���������. ��������� � ��������� ���� ������ � �������� ������������ ���������� ������� len(), str(),
# � ����� �������� � ����������� +, *, in.

# ---------------------------------------------------------------------------------------------------------------

# ��������� ��� ������
#
# ��������� ��� ������, ��� � ��������, ����� ����� ������������ � ����������������. � Python ��������� ��� ������
# ����� �������� str (���������� �� string � ������, ���).
#
# ��� �������� ��������� ���������� (��������), �� ������ ��������� ����������� ����� � �������. � Python �����
# ������������ ��� ��������� �������, ��� � �������:

s1 = 'Python rocks!'
s2 = "Python rocks!"

# ��������, ��� �� ���������, ������� input() ��������� ������ ������ ������:

s = input()  # ���������� s ����� ��������� ��� str

# ��� ������� ������ ������, �� ���������� ��� ������� ����������� ����:

s1 = ''   # ������ ������
s2 = ' '  # ������ ��������� �� ������ ������� �������

# ---------------------------------------------------------------------------------------------------------------

# ����� ������

# ������ ������ ���������� ���������� �������� �� ������� ��� �������. ����� ��������� ����� ������ ����������
# ���������� ������� len() (�� ����� length � �����).

# ��������� ����������� ���:
s1 = 'abcdef'
length1 = len(s1)               # ������� ����� ������ �� ���������� s1
length2 = len('Python rocks!')  # ������� ����� ���������� ��������
print(length1)
print(length2)

# �������:
# 6
# 13

# !!! ��� �������� ����� ������ ��������� ��� �������, ������� �������. !!!

# ---------------------------------------------------------------------------------------------------------------

# �������������� ����� � ������

# ��� �������������� ������ � ����� �� ������������ ������� int() � float(). ��� ��������� ��������������,
# �� ���� �� ����� � ������ �� ���������� ������� str():
#
# ���������� ��������� ����������� ���:
num1 = 1777    # ����� �����
num2 = 17.77   # ����� � ��������� ������
s1 = str(num1) # ������������� ����� ����� � ������ '1777'
s2 = str(num2) # ������������� ����� � ��������� ������ � ������ '17.77'

# !!! ������ �������� �� �������� ������� �����, ��� � �������. ���� ���� � ������� ������ �������, ��� ������ �����,
# ��� ����� �� ������ �������� � ��� ��� �� �������.!!!

# ---------------------------------------------------------------------------------------------------------------

# ������������ �����
# ������, ��� � �����, ����� ����������. �������� �������� ����� ���������� ������������� ��� ����������.

# ���������� ��������� ����������� ���:

s1 = 'ab' + 'bc'
s2 = 'bc' + 'ab'
s3 = s1 + s2 + '!!'
print(s1)
print(s2)
print(s3)

# ����������� ���������� ������ ���� �����:
# abbc
# bcab
# abbcbcab!!

# �������� �������� ����� � ������� �� �������� �������� ����� �� �������� �������������,
# �� ����, �� ������������ ���� ���������-����� ��������� ��������!

# � ������� ������������ ����� ����� ����������� ����� ������, ������� ������ �� ������ ���������
# �������������� ��������� sep � end. ��������� ��� ������ ���� ������ ���� � ����:

print('a', 'b', 'c', sep='*', end='!')
print()  # ������� �� ����� ������
print('a' + '*' + 'b' + '*' + 'c' + '!')

# # ����������� ���������� ������ ���� �����:
# a*b*c!
# a*b*c!

# ---------------------------------------------------------------------------------------------------------------

# ��������� ������ �� �����

# � Python ��� �� ����� �������� ������ �� �����. ����� �������� ��������� ������ ��������� ���������� ���.
#
# ���������� ��������� ����������� ���:
s = 'Hi' * 4
print(s)

# ����������� ���������� ������ ���� �����:
# HiHiHiHi

# �������� ��������� ������ �� ����� (repetition) ����� ������ �� ��������. ��������, �� �����
# ����������� ������ ��������� �� 75 �������� -. �� ����� ��� ������� � ������� ����:
print('-' * 75)

# ����������� ���������� ������ ���� �����:
# ---------------------------------------------------------------------------

# !!!������ ����� �������� �� �����, �� ������ �������� �� ������.!!!

# ---------------------------------------------------------------------------------------------------------------

# ����������

# ���������� 1. ������� ������� � Python ������������ ��� �������������� (multiline) ������. ��������,

text = '''Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design 
philosophy emphasizes code readability with its notable use of significant whitespace.'''

# ���������� 2. �� ������ ������ ����� ���������� ��������, ��� ����� ������������ ��� ���������, ��� � ������� �������,
# ������ ����� ������ ��������� ����� ����� ��������� � ������ ������ �������:

s1 = '�� ����� ������������ � ��������� �������� ������� ������� "����� � ���"'
s2 = "�� ����� ������������ � ������� �������� ��������� ������� '����� � ���'"
print(s1)
print(s2)

# ����������� ���������� ������ ���� �����:
# �� ����� ������������ � ��������� �������� ������� ������� "����� � ���"
# �� ����� ������������ � ������� �������� ��������� ������� '����� � ���'

# ---------------------------------------------------------------------------------------------------------------

# �������� ���������, ������� ������� �����:
#
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."
#
# ����������. ����������� ������������ �����.

text = '''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."'''
print(text)

# ---------------------------------------------------------------------------------------------------------------

# What's Your Name?

# �������� ���������, ������� ��������� � ���������� ��� ������ � ��� � ������� ������������ � ������� �����:

# �Hello [��������� ���] [��������� �������]! You just delved into Python�.

# ������ ������� ������
# �� ���� ��������� ������� ��� ������ (��� � �������), ������ �� ��������� ������.
#
# ������ �������� ������
# ��������� ������ ������� ����� � ������������ � �������� ������.

# ����������. ����� firstname lastname �������� ������ =)

firstname = input()
lastname = input()
print(f"Hello {firstname} {lastname}! You just delved into Python")

# ---------------------------------------------------------------------------------------------------------------

# ���������� �������

# �������� ���������, ������� ��������� � ���������� �������� ���������� ������� � ������� �����:
#
# ����������� ������� [�������� ������] ����� ����� [����� �������� ������] ��������.
#
# ������ ������� ������
# �� ���� ��������� ������� ������ � �������� ���������� �������.
#
# ������ �������� ������
# ��������� ������ ������� ����� � ������������ � �������� ������.

football_team = input()
football_team_leng = len(football_team)
print(f"���������� ������� {football_team} ����� ����� {football_team_leng} ��������")

# ---------------------------------------------------------------------------------------------------------------

# ��� ������

# ���� �������� ���� �������. �������� ���������, ������� ���������� ����� �������� � ����� ������� �������� ������.

# ������ ������� ������
# �� ���� ��������� ������� �������� ���� �������, ������ �� ��������� ������.

# ������ �������� ������
# ��������� ������ ������� ����� �������� � ������� �������� ������, ������ �� ��������� ������.

# ����������. �������������, ��� ����� �������� ���� ���� ������� ��������.

town1 = input()
town2 = input()
town3 = input()
town_len1 = len(town1)
town_len2 = len(town2)
town_len3 = len(town3)
if min(town_len1, town_len2, town_len3) == town_len1:
    print(town1)
elif min(town_len1, town_len2, town_len3) == town_len2:
    print(town2)
elif min(town_len1, town_len2, town_len3) == town_len3:
    print(town3)
if max(town_len1, town_len2, town_len3) == town_len1:
    print(town1)
elif max(town_len1, town_len2, town_len3) == town_len2:
    print(town2)
elif max(town_len1, town_len2, town_len3) == town_len3:
    print(town3)



# ������ �������:

a, b, c = input(), input(), input()

if(len(a) < len(b)): b, a = a, b
if(len(c) > len(b)): c, b = b, c
if(len(c) > len(a)): c, a = a, c
if(len(b) > len(a)): b, a = a, b

print(c, a, sep='\n')
# ---------------------------------------------------------------------------------------------------------------

# �������������� ������
#
# �������� 3 ������ � ��������� �������. �������� ���������, ������� �������� ����� �� �� ���� ���� ����� ���������
# ������������ �������������� ����������.
#
# ������ ������� ������
# �� ���� ��������� �������� ��� ������, ������ �� ��������� ������.
#
# ������ �������� ������
# ��������� ������ ������� ������ �YES�, ���� �� ���� ��������� ���� ����� ��������� �������������� ����������,
# �NO� � ���� ������.

a = len(input())
b = len(input())
c = len(input())
if (2 * b - c -a) * (2 * c - b - a) * (2 * a - b - c) == 0:
    print("YES")
else:
    print("NO")

# ---------------------------------------------------------------------------------------------------------------

# �������� in
#
# � Python ���� ����������� �������� in, ������� ��������� ���������, ��� ���� ������ ��������� ������ ������.
#
# ���������� ��������� ���:

s = input()
if 'a' in s:
    print('��������� ������ �������� ������ �')
else:
    print('��������� ������ �� �������� ������ �')

# ����� ��� ���������, ���������� �� � ���������� s ������ a � ������� ��������������� �����.
#
# �� ����� ������������ �������� in ������ � ���������� ���������� not. ��������

s = input()
if '.' not in s:
    print('��������� ������ �� �������� ������� �����')


# � ������� ��������� in �� ����� ��������� ��������� ���, �����������, ��� � ���������� s ��������� ���� ��
# 5 �������� a, e, i, o, u:

if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('YES')

# �� ����:
if len(s) == 1 and s in 'aeiou':
    print('YES')

# ����������
# ����������. ���� ������ s1 ���������� � ������ s2, �� �������, ��� ������ s1 �������� ���������� ��� ������ s2.
# ������� �������, �������� in ���������� �������� �� ���� ������ ���������� ������.

# ---------------------------------------------------------------------------------------------------------------

# ���� ���������� �����
#
# �������� ���������, ������� ��������� ���� ������, ����� ���� ������� �YES�, ���� � ��������� ������ ���� ���������
# ������ � �NO� � ��������� ������.
#
# ������ ������� ������
# �� ���� ��������� �������� ���� ������.
#
# ������ �������� ������
# ��������� ������ ������� ����� � ������������ � �������� ������.

s = str(input())
if '�����' in s:
    print("YES")
else:
    print("NO")

# ---------------------------------------------------------------------------------------------------------------

# �������� ��?
#
# �������� ���������, ������� ��������� ���� ������, ����� ���� ������� �YES�, ���� � �������� ������ ���� ���������
# �������� ��� ������������, � �NO� � ��������� ������.
#
# ������ ������� ������
# �� ���� ��������� �������� ���� ������.
#
# ������ �������� ������
# ��������� ������ ������� ����� � ������������ � �������� ������.

a = input()
if '�������' in a or '�����������' in a:
    print("YES")
else:
    print("NO")

# ---------------------------------------------------------------------------------------------------------------

# ���������� email
#
# ����� ������� email ����� ����������, ���� � ��� ���� ������ ������� (@) � �����. �������� ���������
# ����������� ������������ email ������.
#
# ������ ������� ������
# �� ���� ��������� ������� ���� ������ � email �����.
#
# ������ �������� ������
# ��������� ������ ������� ������ �YES�, ���� email ����� �������� ���������� � �NO� � ���� ������.
#
# ����������. ������� �������� @ � . ������������ ��� ������������ email ������, ������ �� ���������� �������������
# ������ �� ����� �������� email.

a = input()
if '@' in a and '.' in a:
    print("YES")
else:
    print("NO")

# ---------------------------------------------------------------------------------------------------------------
