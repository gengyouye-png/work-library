def calc_total(record):
    # 計算加權總分：第一個成績佔 20%，第二個成績佔 30%，第三個成績佔 50%
    return round(record[2] * 0.2 + record[3] * 0.3 + record[4] * 0.5, 1)


def compare_student(a, b):
    # 如果總分不同，總分較高的學生排前面
    if a[5] != b[5]:
        return a[5] > b[5]
    # 如果總分相同，學號較小的學生排前面
    return a[0] < b[0]


def insertion_sort_students(records):
    # 使用插入排序法，將學生資料依照 compare_student 的規則排序
    for i in range(1, len(records)):
        # current 是目前要插入到前面已排序區域的學生資料
        current = records[i]
        j = i - 1
        # 當 current 應該排在 records[j] 前面時，就把 records[j] 往後移
        while j >= 0 and compare_student(current, records[j]):
            records[j + 1] = records[j]
            j -= 1
        # 找到正確位置後，將 current 放進去
        records[j + 1] = current


# 每筆資料格式：[學號, 姓名, 成績1, 成績2, 成績3]
records = [
    [1101, "Amy", 88, 76, 91],
    [1102, "Ben", 70, 82, 86],
    [1103, "Cindy", 95, 88, 84],
    [1104, "David", 88, 76, 91],
    [1105, "Eva", 60, 75, 78],
    [1106, "Frank", 95, 88, 84],
]

# 將每位學生的加權總分計算出來，並加到該筆資料的最後面
for record in records:
    record.append(calc_total(record))

# 依照總分由高到低排序；若總分相同，依照學號由小到大排序
insertion_sort_students(records)

# 印出排序後的名次、學號、姓名與總分
print("名次\t學號\t姓名\t總分")
for rank, record in enumerate(records, start=1):
    # record[5] 是加權總分，:.1f 表示輸出到小數點第一位
    print(f"{rank}\t{record[0]}\t{record[1]}\t{record[5]:.1f}")
