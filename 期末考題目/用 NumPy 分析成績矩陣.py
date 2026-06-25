import numpy as np

# 建立成績矩陣
# 每一列代表一位學生
# 每一欄代表一題
scores = np.array([
    [80, 70, 90, 85],
    [55, 60, 58, 62],
    [95, 88, 92, 90],
    [40, 45, 50, 55],
    [75, 80, 70, 65]
])

# 1. 計算每位學生平均
# axis=1 表示橫向計算，也就是每一列各自算平均
student_avg = np.mean(scores, axis=1)

# 2. 計算每一題平均
# axis=0 表示直向計算，也就是每一欄各自算平均
question_avg = np.mean(scores, axis=0)

# 3. 判斷每位學生是否及格
# 平均分數大於或等於 60 分，就是及格
student_pass = student_avg >= 60

# 4. 計算全班及格率
# True 會被當成 1，False 會被當成 0
pass_rate = np.mean(student_pass) * 100

# 5. 找出平均最低的題目
# np.argmin 會找出最小值的位置
# 題號要從 1 開始，所以要 +1
hardest_question = np.argmin(question_avg) + 1

# 6. 找出需要補救的學生
# 條件是學生平均分數小於 60
# 學生編號要從 1 開始，所以要 +1
need_help_students = np.where(student_avg < 60)[0] + 1

# 7. 輸出結果
print("每位學生平均：", student_avg)
print("每一題平均：", question_avg)
print("每位學生是否及格：", student_pass)
print("全班及格率為：", pass_rate, "%")
print("平均最低的題目是第", hardest_question, "題")
print("需要補救的學生編號：", need_help_students)

# 最後整理輸出一段摘要文字
print("全班及格率為", pass_rate, "%，最困難的是第", hardest_question, "題。")
