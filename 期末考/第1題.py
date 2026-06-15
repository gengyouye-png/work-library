def calc_total(record):
    return round(record[2] * 0.2 + record[3] * 0.3 + record[4] * 0.5, 1)


def compare_student(a, b):
    if a[5] != b[5]:
        return a[5] > b[5]
    return a[0] < b[0]


def insertion_sort_students(records):
    for i in range(1, len(records)):
        current = records[i]
        j = i - 1
        while j >= 0 and compare_student(current, records[j]):
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = current


records = [
    [1101, "Amy", 88, 76, 91],
    [1102, "Ben", 70, 82, 86],
    [1103, "Cindy", 95, 88, 84],
    [1104, "David", 88, 76, 91],
    [1105, "Eva", 60, 75, 78],
    [1106, "Frank", 95, 88, 84],
]

for record in records:
    record.append(calc_total(record))

insertion_sort_students(records)

print("名次\t學號\t姓名\t總分")
for rank, record in enumerate(records, start=1):
    print(f"{rank}\t{record[0]}\t{record[1]}\t{record[5]:.1f}")
