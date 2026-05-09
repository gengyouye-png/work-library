a = 0
b = 0
n = int(input("請輸入n的值: "))
for i in range(1 , n+1):
    a += i
    if i % 3 == 0 and i % 5 !=0:
        b += 1
print(a)
print(b)