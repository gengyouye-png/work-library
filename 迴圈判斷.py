# Ex1  

x = float(input("請輸入x座標: "))
y = float(input("請輸入y座標: "))
r = float(input("請輸入半徑r: "))

a = x**2 + y**2
b = r**2

if a < b:
    print("在圆内")
elif a == b:
    print("在圆上")
else:
    print("在圆外")

# Ex2
a = int(input("請輸入第一個數字: "))
b = int(input("請輸入第二個數字: "))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

result = gcd(a, b)
print(f"{a} 和 {b} 的最大公因數是: {result}")

# 作業1
credits = 0
passed_elective = 0
passed_required = 0

required_scores = [float(input(f"請輸入必修第 {i} 科成績: ")) for i in range(1, 6)]
for score in required_scores:
    if score >= 60:
        passed_required += 1
        credits += 20

elective_scores = [float(input(f"請輸入選修第 {i} 科成績: ")) for i in range(1, 4)]
for score in elective_scores:
    if score >= 60:
        credits += 20
        passed_elective += 1

print("總學分:", credits)
if passed_required >= 5:
    print("必修全部及格:是")
else:    print("必修全部及格:否")
if passed_elective >= 3:
    print("體育及格門數: 3 ")
else:
    print(f"體育及格門數: {passed_elective} ")

if credits >= 132:
    print("總學分: 已符合畢業門檻")
else:
    print("總學分: 未符合畢業門檻")

# 作業2
credits = 0
scores = 0
a = 0
b = 0
c = 0
serve = 0



scores = input("請輸入修課總門數: ")
for i in range(int(scores)):
    c= float(input(f"請輸入第 {i+1} 門課程成績: "))
    a += c
    if c < 60:
        b += 1
    elif c >= 60:
        credits += float(input(f"請輸入第 {i+1} 門課程學分: "))

serve = input("請輸入服務學習時數: ")
print("總學分:", credits)
print("平均成績:", a / int(scores))
if b > 0:
    print("有不及格科目:是")
elif b == 0:
    print("有不及格科目:否")
print("未達成條件:")
if credits < 128:
    print("總學分不足")
if a / int(scores) < 80:
    print("平均成績不足")
if int(serve) < 30:
    print("服務時數不足")
if b > 0:
    print("有不及格科目")
if credits < 128 or a / int(scores) < 80 or int(serve) < 30 or b > 0:
    print("結果: 不符合申請資格")
else:    
    print("條件全部達成")
    print("結果: 符合申請資格")

# 作業3
def input_non_negative_number(prompt, is_int=True):
    while True:
        try:
            value = input(prompt)

            if is_int:
                value = int(value)
            else:
                value = float(value)

            if value < 0:
                print("輸入錯誤：所有數值皆不得小於 0，請重新輸入。")
            else:
                return value
        except ValueError:
            print("輸入格式錯誤，請重新輸入。")


def check_student(total, required, elective, service, fine, failed_required):
    reasons = []

    if total < 128:
        reasons.append("總學分不足")
    if required < 84:
        reasons.append("必修學分不足")
    if elective < 14:
        reasons.append("通識學分不足")
    if service < 20:
        reasons.append("服務學習時數不足")
    if fine != 0:
        reasons.append("圖書館罰款未繳清")
    if failed_required != 0:
        reasons.append("尚有必修不及格科目")

    return reasons


# 主程式
n = input_non_negative_number("請輸入學生人數：", is_int=True)

can_join_count = 0
cannot_join_count = 0
for i in range(1, n+1):
    print(f"\n===== 輸入第 {i} 位學生資料 =====")
    name = input("姓名：")

    total = input_non_negative_number("總學分：", is_int=True)
    required = input_non_negative_number("必修學分：", is_int=True)
    elective = input_non_negative_number("通識學分：", is_int=True)
    service = input_non_negative_number("服務學習時數：", is_int=True)
    fine = input_non_negative_number("圖書館罰款金額：", is_int=True)
    failed_required = input_non_negative_number("必修不及格科目數：", is_int=True)

    reasons = check_student(total, required, elective, service, fine, failed_required)

    print(f"\n學生：{name}")
    if len(reasons) == 0:
        print("結果：可參加畢業榮譽典禮")
        can_join_count += 1
    else:
        print("結果：不可參加畢業榮譽典禮")
        print("未達成條件：")
        for idx, reason in enumerate(reasons, start=1):
            print(f"{idx}. {reason}")
        cannot_join_count += 1

print("\n===== 統計結果 =====")
print(f"可參加畢業榮譽典禮人數：{can_join_count}")
print(f"不可參加畢業榮譽典禮人數：{cannot_join_count}")