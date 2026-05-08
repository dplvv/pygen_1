# Выбор из двух
# z1
a = input()
b = input()
if a == b:
    print("Пароль принят")
else:
    print("Пароль не принят")

# z2
a = int(input())
if a % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

# z3
a = int(input())
if a < 18:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")

# z4
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)

# z5
a = int(input())
b = int(input())
c = int(input())
d = b - a
if c - b == d:
    print("YES")
else:
    print("NO")

# z6
a = int(input())
ch1 = (a // 10 ** (4 - 1)) % 10
ch2 = (a // 10 ** (4 - 2)) % 10
ch3 = (a // 10 ** (4 - 3)) % 10
ch4 = (a // 10 ** (4 - 4)) % 10
if ch1 + ch4 == ch2 - ch3:
    print("ДА")
else:
    print("НЕТ")

# z7
a = int(input())
b = int(input())
c = int(input())
sum = 0
if a == abs(a):
    sum += a
if b == abs(b):
    sum += b
if c == abs(c):
    sum += c
print(sum)

# z8
a = int(input())
if 0 <= a <= 13:
    print("детство")
if 14 <= a <= 24:
    print("молодость")
if 25 <= a <= 59:
    print("зрелость")
if 60 <= a:
    print("старость")

# z9
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a, b, c, d))


# Логические операции
# z1
x = int(input())
if x > -1 and x < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")

# z2
x = int(input())
if x <= -3 or x >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")

# z3
x = int(input())
if x > -30 and x <= -2 or x > 7 and x <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")

# z4
a = int(input())
if 1000 <= a <= 9999 and (a % 7 == 0 or a % 17 == 0):
    print("YES")
else:
    print("NO")

# z5
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

# z6
a = int(input())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("YES")
else:
    print("NO")

# z7
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d:
    print("YES")
else:
    print("NO")

# z8
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if -1 <= (c - a) <= 1 and -1 <= (d - b) <= 1:
    print("YES")
else:
    print("NO")


# Вложенные и каскадные условия
# z1
n = int(input())
k = int(input())
if n > k:
    print("NO")
elif k > n:
    print("YES")
else:
    print("Don't know")

# z2
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")

# z3
a = int(input())
b = int(input())
c = int(input())
if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
elif b < c < a or a < c < b:
    print(c)

# z4
a = int(input())
if a == 2:
    print(28)
elif a == 4 or a == 6 or a == 9 or a == 11:
    print(30)
else:
    print(31)

# z5
a = int(input())
if a < 60:
    print("Легкий вес")
elif a < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")

# z6
a = int(input())
b = int(input())
s = input()
if s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "*":
    print(a * b)
elif s == "/":
    if b == 0:
        print("На ноль делить нельзя!")
    else:
        print(a / b)
else:
    print("Неверная операция")

# z7
a = input()
b = input()
if a == "красный" and b == "синий" or a == "синий" and b == "красный":
    print("фиолетовый")
elif a == "красный" and b == "желтый" or a == "желтый" and b == "красный":
    print("оранжевый")
elif a == "синий" and b == "желтый" or a == "желтый" and b == "синий":
    print("зеленый")
elif (a == "синий" or a == "красный" or a == "желтый") and a == b:
    print(a)
else:
    print("ошибка цвета")

# z8
a = int(input())
if a == 0:
    print("зеленый")
elif 1 <= a <= 10:
    if a % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 11 <= a <= 18:
    if a % 2 != 0:
        print("черный")
    else:
        print("красный")
elif 19 <= a <= 28:
    if a % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 29 <= a <= 36:
    if a % 2 != 0:
        print("черный")
    else:
        print("красный")
else:
    print("ошибка ввода")

# z9
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 < a1:
    a1, b1, a2, b2 = a2, b2, a1, b1
if a2 > b1:
    print("пустое множество")
elif a2 == b1:
    print(a2)
else:
    if b1 < b2:
        print(a2, b1)
    else:
        print(a2, b2)
