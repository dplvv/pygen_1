# z1
a = int(input())
ch3 = (a // 10 ** (4 - 3)) % 10
ch4 = (a // 10 ** (4 - 4)) % 10
if ch3 == 0 and ch4 == 0:
    print("YES")
else:
    print("NO")

# z2
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a + b + c + d) % 2 == 0:
    print("YES")
else:
    print("NO")

# z3
age = int(input())
sex = input()
if 10 <= age <= 15 and sex == "f":
    print("YES")
else:
    print("NO")

# z4
a = int(input())
if a == 1:
    print("I")
elif a == 2:
    print("II")
elif a == 3:
    print("III")
elif a == 4:
    print("IV")
elif a == 5:
    print("V")
elif a == 6:
    print("VI")
elif a == 7:
    print("VII")
elif a == 8:
    print("VIII")
elif a == 9:
    print("IX")
elif a == 10:
    print("X")
else:
    print("ошибка")

# z5
a = int(input())
if a % 2 != 0:
    print("YES")
elif a % 2 == 0 and 2 <= a <= 5:
    print("NO")
elif a % 2 == 0 and 6 <= a <= 20:
    print("YES")
else:
    print("NO")

# z6
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) == abs(b - d):
    print("YES")
else:
    print("NO")

# z7
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs((a - c) * (b - d)) == 2:
    print("YES")
else:
    print("NO")

# z8
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) == abs(b - d) or a == c or b == d:
    print("YES")
else:
    print("NO")
