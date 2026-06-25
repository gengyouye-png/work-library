# 成績資料排序與排名


def calc_total(record):
    # record 格式：[學號, 姓名, 小考, 期中考, 期末考]
    # 總分公式：小考 * 0.2 + 期中考 * 0.3 + 期末考 * 0.5
    total = record[2] * 0.2 + record[3] * 0.3 + record[4] * 0.5

    # 四捨五入到小數第 1 位
    return round(total, 1)


def compare_student(a, b):
    # 先計算兩位學生的總分
    total_a = calc_total(a)
    total_b = calc_total(b)

    # 如果 a 的總分比較高，a 應該排在 b 前面
    if total_a > total_b:
        return True

    # 如果 a 的總分比較低，a 不應該排在 b 前面
    if total_a < total_b:
        return False

    # 如果總分相同，學號比較小的排前面
    return a[0] < b[0]


def insertion_sort_students(records):
    # 複製一份資料，避免改到原本的 records
    result = records.copy()

    # 插入排序從第 2 筆資料開始處理
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        # 如果 current 應該排在 result[j] 前面，就把 result[j] 往後移
        while j >= 0 and compare_student(current, result[j]):
            result[j + 1] = result[j]
            j = j - 1

        # 找到正確位置後，把 current 放進去
        result[j + 1] = current

    return result


# 測試資料
records = [
    [1101, "Amy", 88, 76, 91],
    [1102, "Ben", 70, 82, 86],
    [1103, "Cindy", 95, 88, 84],
    [1104, "David", 88, 76, 91],
    [1105, "Eva", 60, 75, 78],
    [1106, "Frank", 95, 88, 84],
]

# 使用自己寫的插入排序來排序
sorted_records = insertion_sort_students(records)

# 輸出每位學生的名次、學號、姓名、總分
print("名次\t學號\t姓名\t總分")

rank = 1
for student in sorted_records:
    total = calc_total(student)
    print(rank, "\t", student[0], "\t", student[1], "\t", total)
    rank = rank + 1
