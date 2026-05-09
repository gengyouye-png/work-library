x , y , r = map(float, input().split())
if -10**4 <= x <= 10**4 and -10**4 <= y <= 10**4 and 0 < r <= 10**4:
    a = x**2 + y **2
    b = r**2
    if a < b:
        print("在圓內")
    elif a == b:
        print("在圓上")
    else:
        print("在圓外")
else:
    print("輸入錯誤")