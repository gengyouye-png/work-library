x , y = map(float, input().split())
if -10**4 <= x <= 10**4 and -10**4 <= y <= 10**4:
    z = (x**2 + y**2)**0.5
    print(f"{z: .4f} ")
else:
    print("輸入錯誤")  

