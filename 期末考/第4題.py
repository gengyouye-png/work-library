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
