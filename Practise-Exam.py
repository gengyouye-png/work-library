all_a = 0
y = 0
b = 0
c = 0 
n  = int(input(""))
for i in range(1 , n+1):
    a = int(input(f"第{i}門成績:"))
    all_a += a #總成績
    if a < 60:
        c += 1
    else:
        b += int(input(f"第{i}門學分:"))

d = int(input("服務時數:"))

y = all_a / n
print("總學分" , b )
print("平均成績:" , y)
if c > 1:
    print("有不及成績:是")
else:
    print("有不及格成績:否")
if d < 30:
    print("服務時數:未滿")
else:
    print("服務時數:過")
reasons = []

if b < 128:
    reasons.append("總學分不足")
if y < 80:
    reasons.append("平均成績不足")
if d < 30:
    reasons.append("服務時數不足")
if c > 0:
    reasons.append("有不及格科目")

if reasons:
    print("未達成條件:")
    for i , reasons in enumerate(reasons , 1):
        print(f"{i}.{reasons}")
    print("不符合")
else:
    print("符合")
