# Команды print() и input(), переменные
# z1
print("Здравствуй, мир!")

# z2
print("4", "8", "15", "16", "23", "42")

# z3
print("4")
print("8")
print("15")
print("16")
print("23")
print("42")

# z4
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")

# z5
name = input()
print("Привет,", name)

# z6
team = input()
print(team, "-", "чемпион!")

# z7
a = input()
b = input()
c = input()
print(a)
print(b)
print(c)

# z8
a = input()
b = input()
c = input()
print(c)
print(b)
print(a)


# Параметры sep и end, PEP8
# z1
a = "***"
print("I", "like", "Python", sep=a)

# z2
name = input()
print("Привет,", name, end="!")

# z3
a = input()
b = input()
c = input()
d = input()
print(b, c, d, sep=a)


# Целочисленная арифметика. Часть 1
# z1
a = int(input())
print(a)
print(a + 1)
print(a + 2)

# z2
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

# z3
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = a + b + c + d
print(e * 3)

# z4
a = int(input())
b = int(input())
c = 3 * (a + b) ** 3 + 275 * b**2 - 127 * a - 41
print(c)

# z5
a = int(input())
print("Следующее за числом", a, "число:", a + 1)
print("Для числа", a, "предыдущее число:", a - 1)

# z6
a = int(input())
V = a**3
S = 6 * a**2
print("Объем =", V)
print("Площадь полной поверхности =", S)

# z7
a = int(input())
b = int(input())
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)

# z8
a = int(input())
d = int(input())
n = int(input())
print(a + d * (n - 1))

# z9
a = int(input())
print(a, a * 2, a * 3, a * 4, a * 5, sep="---")


# Целочисленная арифметика. Часть 2
# z1
b = int(input())
q = int(input())
n = int(input())
res = b * q ** (n - 1)
print(res)

# z2
a = int(input())
print(a // 100)

# z3
a = int(input())
b = int(input())
print(b // a)
print(b % a)

# z4
n = int(input())
if n % 2 == 1:
    print(n // 2 + 1)
if n % 2 == 0:
    print(n // 2)

# z5
a = int(input())
print(a, "мин - это", a // 60, "час", a % 60, "минут.")

# z6
a = int(input())
print((a - 1) // 4 + 1)

# z7
a = int(input())
ch1 = a // 100
ch2 = a % 100 // 10
ch3 = a % 10
summ = ch1 + ch2 + ch3
pr = ch1 * ch2 * ch3
print("Сумма цифр =", summ)
print("Произведение цифр =", pr)

# z8
a = int(input())
ch1 = a // 100
ch2 = a % 100 // 10
ch3 = a % 10
print(ch1, ch2, ch3, sep="")
print(ch1, ch3, ch2, sep="")
print(ch2, ch1, ch3, sep="")
print(ch2, ch3, ch1, sep="")
print(ch3, ch1, ch2, sep="")
print(ch3, ch2, ch1, sep="")

# z9
a = int(input())
ch1 = (a // 10 ** (4 - 1)) % 10
ch2 = (a // 10 ** (4 - 2)) % 10
ch3 = (a // 10 ** (4 - 3)) % 10
ch4 = (a // 10 ** (4 - 4)) % 10
print("Цифра в позиции тысяч равна", ch1)
print("Цифра в позиции сотен равна", ch2)
print("Цифра в позиции десятков равна", ch3)
print("Цифра в позиции единиц равна", ch4)
