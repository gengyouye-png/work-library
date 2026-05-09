all_b = 0
e = 0   # 總學分
c = 0   # 不及格科目數

a = int(input("幾門課: "))

for i in range(1, a + 1):
    b = float(input(f"第{i}門成績: "))
    all_b += b
    if b < 60 :
        c += 1
    else:
        e += float(input(f"第{i}門課學分"))

x = int(input("服務學習時數: "))

y = all_b / a

print("總學分:", e)
print("平均成績:", round(y, 1))
print("有不及格科目:", "是" if c > 0 else "否")
print("服務時數達標:", "是" if x >= 30 else "否")

reasons = []

if e < 128:
    reasons.append("總學分不足")
if y < 80:
    reasons.append("平均成績不足")
if x < 30:
    reasons.append("服務時數不足")
if c > 0:
    reasons.append("有不及格科目")

if reasons:
    print("未達成條件：")
    for i, reason in enumerate(reasons, 1):
        print(f"{i}. {reason}")
    print("結果：不符合申請資格")
else:
    print("結果：符合申請資格")