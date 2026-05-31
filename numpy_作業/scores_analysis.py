import numpy as np

scores = np.array([[80, 70, 90, 85],
                   [55, 60, 58, 62],
                   [95, 88, 92, 90],
                   [40, 45, 50, 55],
                   [75, 80, 70, 65]])

student_avg = scores.mean(axis=1)
question_avg = scores.mean(axis=0)
is_pass = student_avg >= 60
pass_rate = is_pass.mean()

hardest_question = np.argmin(question_avg) + 1
need_help_students = np.where(student_avg < 60)[0] + 1
need_help_text = "、".join(need_help_students.astype(str))

print("scores.shape:", scores.shape)
print("student_avg:", student_avg)
print("question_avg:", question_avg)
print("is_pass:", is_pass)
print("pass_rate:", pass_rate)
print("hardest_question:", hardest_question)
print("need_help_students:", need_help_students)

summary = (
    f"全班及格率為 {pass_rate * 100:.1f}%，"
    f"最困難的是第 {hardest_question} 題，"
    f"需要補救的學生是第 {need_help_text} 位。"
)

print("summary:", summary)
