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