#第一題

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

#第二題

def search_by_keyword(books, keyword):
    results = []
    keyword = keyword.lower()

    for book in books:
        if keyword in book[1].lower() or keyword in book[2].lower():
            results.append(book)

    return results


def search_first_available_python(books):
    for book in books:
        if "python" in book[1].lower() and book[3] == "可借":
            return book

    return None


def print_books(books):
    if not books:
        print("查無符合資料")
        return

    print("書號\t書名\t作者\t狀態")
    for book in books:
        print(f"{book[0]}\t{book[1]}\t{book[2]}\t{book[3]}")


books = [
    ["B001", "Python Basics", "Lin", "可借"],
    ["B002", "Data Science Notes", "Wang", "借出"],
    ["B003", "Matplotlib Guide", "Chen", "可借"],
    ["B004", "Recursive Thinking", "Lin", "可借"],
    ["B005", "NumPy Practice", "Huang", "借出"],
    ["B006", "Python Project", "Tsai", "可借"],
]

for keyword in ["python", "lin"]:
    print(f'keyword = "{keyword}"')
    print_books(search_by_keyword(books, keyword))
    print()

print("第一本書名含 Python 且狀態為可借的書：")
book = search_first_available_python(books)
print_books([book] if book else [])

#第三題

def folder_size(folder):
    total = 0

    for item in folder[1:]:
        if isinstance(item, int):
            total += item
        else:
            total += folder_size(item)

    return total


def count_files(folder):
    count = 0

    for item in folder[1:]:
        if isinstance(item, int):
            count += 1
        else:
            count += count_files(item)

    return count


def max_depth(folder):
    deepest = 1

    for item in folder[1:]:
        if isinstance(item, list):
            depth = 1 + max_depth(item)
            if depth > deepest:
                deepest = depth

    return deepest


root = [
    "root",
    120,
    ["images", 50, 30, ["raw", 200, 180]],
    ["code", 10, ["old", 5, 8]],
    60,
]

print(f"總容量：{folder_size(root)} MB")
print(f"檔案數量：{count_files(root)}")
print(f"最大深度：{max_depth(root)}")

#第四題

import numpy as np


student_ids = np.array(["S1", "S2", "S3", "S4", "S5", "S6"])

scores = np.array([
    [80, 75, 90, 88],
    [60, -1, 72, 70],
    [95, 92, -1, 96],
    [70, 68, 75, -1],
    [88, 85, 84, 86],
    [-1, 78, 80, 82],
], dtype=float)

scores_with_nan = np.where(scores == -1, np.nan, scores)
quiz_averages = np.nanmean(scores_with_nan, axis=0)
filled_scores = np.where(np.isnan(scores_with_nan), quiz_averages, scores_with_nan)
student_averages = np.mean(filled_scores, axis=1)
highest_index = np.argmax(student_averages)

print("各次測驗平均：", np.round(quiz_averages, 2))
print("補值後成績：")
print(np.round(filled_scores, 2))
print("各學生補值後平均：")

for student_id, average in zip(student_ids, student_averages):
    print(f"{student_id}: {average:.2f}")

print(f"平均最高學生：{student_ids[highest_index]}")
print(f"最高平均：{student_averages[highest_index]:.2f}")

#第五題

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
products = np.array(["Notebook", "Pen", "Sticker"])
sales = np.array([
    [120, 300, 180],
    [150, 280, 210],
    [130, 350, 240],
    [170, 330, 260],
    [160, 390, 300],
    [190, 410, 320],
])

monthly_totals = np.sum(sales, axis=1)
product_totals = np.sum(sales, axis=0)
highest_month_index = np.argmax(monthly_totals)
output_dir = Path(__file__).parent

print("每月總銷售量：")
for month, total in zip(months, monthly_totals):
    print(f"{month}: {total}")

print("各產品六個月總銷售量：")
for product, total in zip(products, product_totals):
    print(f"{product}: {total}")

print(
    f"總銷售量最高月份：{months[highest_month_index]}，"
    f"銷售量：{monthly_totals[highest_month_index]}"
)

plt.figure(figsize=(8, 5))
plt.plot(months, monthly_totals, marker="o", linewidth=2, color="royalblue")
plt.title("Monthly Total Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True, linestyle="--", alpha=0.5)

for month, total in zip(months, monthly_totals):
    plt.text(month, total + 10, str(total), ha="center")

plt.tight_layout()
plt.savefig(output_dir / "q5_monthly_total.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 5))
bars = plt.bar(products, product_totals, color=["steelblue", "orange", "seagreen"])
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.grid(axis="y", linestyle="--", alpha=0.5)

for bar, total in zip(bars, product_totals):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 10,
        str(total),
        ha="center",
    )

plt.tight_layout()
plt.savefig(output_dir / "q5_product_total.png", dpi=300)
plt.close()
