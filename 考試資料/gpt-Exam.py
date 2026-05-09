def input_non_negative_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("輸入錯誤：不可小於 0")
            else:
                return value
        except:
            print("格式錯誤")


def check_student(data):
    rules = [
        ("總學分不足", data["total"] < 128),
        ("必修學分不足", data["required"] < 84),
        ("通識學分不足", data["elective"] < 14),
        ("服務學習時數不足", data["service"] < 20),
        ("圖書館罰款未繳清", data["fine"] != 0),
        ("尚有必修不及格科目", data["failed"] != 0),
    ]

    return [msg for msg, cond in rules if cond]


# 主程式
n = input_non_negative_number("學生人數：")                                                                                     

can_join = 0
cannot_join = 0

for i in range(n):
    print(f"\n--- 第{i+1}位 ---")
    name = input("姓名：")

    data = {
        "total": input_non_negative_number("總學分："),
        "required": input_non_negative_number("必修學分："),
        "elective": input_non_negative_number("通識學分："),
        "service": input_non_negative_number("服務時數："),
        "fine": input_non_negative_number("罰款："),
        "failed": input_non_negative_number("必修不及格數：")
    }

    reasons = check_student(data)

    print(f"\n學生：{name}")
    if not reasons:
        print("✅ 可參加")
        can_join += 1
    else:
        print("❌ 不可參加")
        for i, r in enumerate(reasons, 1):
            print(f"{i}. {r}")
        cannot_join += 1


print("\n=== 統計 ===")
print("可參加：", can_join)
print("不可參加：", cannot_join)