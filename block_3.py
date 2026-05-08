# Числовые типы данных: int, float
# z1
a = float(input())
b = float(input())
print(0.5 * a * b)

# z2
S = float(input())
V1 = float(input())
V2 = float(input())
print(S / (V1 + V2))

# z3
a = float(input())
if a == 0:
    print("Обратного числа не существует")
else:
    print(a ** (-1))

# z4
a = float(input())
print((5 / 9) * (a - 32))

# z5
a = int(input())
if a <= 2:
    print(float(a * 10.5))
else:
    print(float(2 * 10.5 + (a - 2) * 4))

# z6
a = float(input())
print(int(10 * a % 10))

# z7
a = float(input())
print(a % int(a))

# z8
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print("Наименьшее число =", min(a, b, c, d, e))
print("Наибольшее число =", max(a, b, c, d, e))

# z9
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

# z10
a = int(input())
ch1 = (a // 10 ** (3 - 1)) % 10
ch2 = (a // 10 ** (3 - 2)) % 10
ch3 = (a // 10 ** (3 - 3)) % 10
mx = max(ch1, ch2, ch3)
mn = min(ch1, ch2, ch3)
sum = ch1 + ch2 + ch3
sr = sum - mx - mn
if sr == mx - mn:
    print("Число интересное")
else:
    print("Число неинтересное")

# z11
a = int(input())
b = int(input())
c = int(input())
mx = max(a, b, c)
mn = min(a, b, c)
print(mx)
print((a + b + c) - (mx + mn))
print(mn)

# z12
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
print(abs(p1 - q1) + abs(p2 - q2))


# Строковый тип данных
# z1
print(
    '"Python is a great language!", said Fred. "I don'
    + "'t ever remember having this much fun before."
    + '"'
)

# z2
a = input()
b = input()
print("Hello" + " " + a + " " + b + "! You have just delved into Python")

# z3
a = input()
print("Футбольная команда" + " " + a + " " + "имеет длину", len(a), "символов")

# z4
a = input()
b = input()
c = input()
la = len(a)
lb = len(b)
lc = len(c)
mn = min(la, lb, lc)
mx = max(la, lb, lc)
if mn == la:
    print(a)
elif mn == lb:
    print(b)
elif mn == lc:
    print(c)
if mx == la:
    print(a)
elif mx == lb:
    print(b)
elif mx == lc:
    print(c)

# z5
a = input()
b = input()
c = input()
la = len(a)
lb = len(b)
lc = len(c)
mn = min(la, lb, lc)
mx = max(la, lb, lc)
sr = (la + lb + lc) - (mx + mn)
if sr - mn == mx - sr:
    print("YES")
else:
    print("NO")

# z6
a = input()
if "синий" in a:
    print("YES")
else:
    print("NO")

# z7
a = input()
if "суббота" in a or "воскресенье" in a:
    print("YES")
else:
    print("NO")

# z8
a = input()
if "@" in a and "." in a:
    print("YES")
else:
    print("NO")


# Модуль math
# z1
from math import *

R = float(input())
print(pi * pow(R, 2))
print(2 * pi * R)

# z2
from math import *

x = float(input())
print(ceil(x) + floor(x))

# z3
from math import *

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2)))

# z4
from math import *

x = float(input())
x = radians(x)
print(sin(x) + cos(x) + pow(tan(x), 2))

# z5
from math import *

n = int(input())
a = float(input())
print((n * pow(a, 2)) / (4 * tan(pi / n)))

# z6
from math import *

a = float(input())
b = float(input())
print((a + b) / 2)
print(sqrt(a * b))
print((2 * a * b) / (a + b))
print(sqrt((pow(a, 2) + pow(b, 2)) / 2))

# z7
from math import *

a = float(input())
b = float(input())
c = float(input())
D = pow(b, 2) - 4 * a * c
if D == 0:
    print(-b / (2 * a))
elif D > 0:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
else:
    print("Нет корней")
