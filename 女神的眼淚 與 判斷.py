print("女神的眼淚與判斷")
#公式 h = 1/2*g *t**2
h = input("請輸入身高：")
print(h)
g = 10 #重力加速度
t = float(h)*2 / g
t = t**0.5
t = round(t, 2)
v = float(h) / t
v = round(v, 2)
print("落第時間" ,t)
print("落第速度", v)

#作業1
print("第一題")
print("請輸入學生分數")
score = input()
score = int(score)

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif  score >= 70:
    print("C")
elif  score >= 60:
    print("D")
elif  score < 60:
    print("不及格")
#作業2
# 會員等級陣列
print("第二題")
levels = ["VIP", "Gold", "Normal"]
amount = float(input("請輸入購物金額: "))
level = input("請輸入會員等級(VIP, Gold, Normal): ")

if level not in levels:
    print("等級錯誤")

else:

    if amount < 1000:
        if level == "VIP":
            discount = 0.95
            print ("discount", discount)
        elif level == "Gold":
            discount = 0.98
            print ("discount", discount)
        else:
            discount = 1

    elif amount < 5000:
        if level == "VIP":
            discount = 0.8
            print ("discount", discount)
        elif level == "Gold":
            discount = 0.85
            print ("discount", discount)
        else:
            discount = 0.9

    else:
        if level == "VIP":
            discount = 0.7
            print ("discount", discount)
        elif level == "Gold":
            discount = 0.75
            print ("discount", discount)
        else:
            discount = 0.8
            print ("discount", discount)

    total = amount * discount
    print("折扣後金額:", total)

#作業3
print("第三題")
year = int(input("請輸入年分: "))
month = int(input("請輸入月份: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31天")
if month in [4, 6, 9, 11]:
    print("30天")   
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29天")
    else:
        print("28天")

print("Thank you for using this program!")

