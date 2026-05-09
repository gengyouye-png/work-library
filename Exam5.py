import math
a = 0
b = 0
while True:
    n = int(input("請輸入n的值: "))
    if n % 2 == 0 and n > 0:
        a += n
    elif n > 0 and n % 2 != 0:
        b += n
    if n == 0:
        break
print(a)
print(b)
