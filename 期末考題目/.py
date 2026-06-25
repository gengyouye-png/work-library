import numpy as np

scores = np.array([
    [80, 70, 90, 85],
    [55, 60, 58, 62],
    [95, 88, 92, 90],
    [40, 45, 50, 55],
    [75, 80, 70, 65]
])

student_avg = np.mean (scores , axis=1)

question_avg  = np.mean (scores , axis=0)

student_pass = student_avg >= 60

pass_rate = np.mean (student_pass)*100

x = np.argmin(question_avg) +1

y = np.where(student_avg < 60)[0] +1

print("學生成績平均:" , student_avg)
print("題目平均成績:" , question_avg)
print("學生是否及格:" , student_pass)
print("全班及格率:" , pass_rate , "%")
print("平均最低的題目: 第" , x , "題")
print("需要補救的學生編號：", y)