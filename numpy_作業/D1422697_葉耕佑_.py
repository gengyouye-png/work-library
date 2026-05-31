import numpy as np


print("第 1 題")

arr = np.arange(1, 101)
even_arr = arr[arr % 2 == 0]
matrix = arr.reshape(10, 10)
row_mean = matrix.mean(axis=1)

print("arr.shape:", arr.shape)
print("arr.dtype:", arr.dtype)
print("even_arr.size:", even_arr.size)
print("matrix.shape:", matrix.shape)
print("row_mean:", row_mean)


print("\n第 2 題")

A = np.array([[10, 11, 12, 13],
              [20, 21, 22, 23],
              [30, 31, 32, 33],
              [40, 41, 42, 43]])

value_22 = A[1, 2]
second_column = A[:, 1]
sub_matrix = A[:2, 1:]
greater_equal_30 = A[A >= 30]

B = A.copy()
B[B % 2 == 0] = -1

print("A[1, 2]:", value_22)
print("第 2 欄:", second_column)
print("子矩陣:")
print(sub_matrix)
print(">= 30:", greater_equal_30)
print("A:")
print(A)
print("B:")
print(B)


print("\n第 3 題")

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

summary = (
    f"全班及格率為 {pass_rate * 100:.1f}%，"
    f"最困難的是第 {hardest_question} 題，"
    f"需要補救的學生是第 {need_help_text} 位。"
)

print("scores.shape:", scores.shape)
print("student_avg:", student_avg)
print("question_avg:", question_avg)
print("is_pass:", is_pass)
print("pass_rate:", pass_rate)
print("hardest_question:", hardest_question)
print("need_help_students:", need_help_students)
print("summary:", summary)


print("\n第 4 題")

raw_scores = np.array([[78, 82, 90],
                       [60, 75, 70],
                       [88, 92, 85],
                       [45, 50, 58]])

bonus = np.array([2, 0, 5])
weights = np.array([0.3, 0.3, 0.4])

adjusted_scores = raw_scores + bonus
adjusted_scores = np.clip(adjusted_scores, 0, 100)
final_scores = (adjusted_scores * weights).sum(axis=1)
is_pass = final_scores >= 60
wrong_bonus = np.array([2, 0, 5, 1])

print("raw_scores.shape:", raw_scores.shape)
print("bonus.shape:", bonus.shape)
print("weights.shape:", weights.shape)
print("adjusted_scores.shape:", adjusted_scores.shape)
print("final_scores.shape:", final_scores.shape)
print("adjusted_scores:")
print(adjusted_scores)
print("final_scores:", final_scores)
print("is_pass:", is_pass)
print("wrong_bonus.shape:", wrong_bonus.shape)


print("\n第 5 題")

rng = np.random.default_rng(seed=2026)
scores = rng.integers(0, 101, size=(300, 6)).astype(float)
missing_mask = rng.random(scores.shape) < 0.05
scores[missing_mask] = np.nan


def summarize_scores(scores):
    missing_count = np.isnan(scores).sum()
    student_avg = np.nanmean(scores, axis=1)
    question_avg = np.nanmean(scores, axis=0)
    pass_rate = (student_avg >= 60).mean()

    valid_mask = ~np.isnan(scores)
    valid_count = valid_mask.sum(axis=0)
    fail_count = ((scores < 60) & valid_mask).sum(axis=0)
    fail_rate_by_question = fail_count / valid_count

    hardest_question = np.argmin(question_avg) + 1

    return {
        "missing_count": missing_count,
        "student_avg": student_avg,
        "question_avg": question_avg,
        "pass_rate": pass_rate,
        "valid_count": valid_count,
        "fail_rate_by_question": fail_rate_by_question,
        "hardest_question": hardest_question,
    }


result = summarize_scores(scores)

print("scores.shape:", scores.shape)
print("scores.dtype:", scores.dtype)
print("missing_count:", result["missing_count"])
print("student_avg.shape:", result["student_avg"].shape)
print("question_avg:", result["question_avg"])
print("pass_rate:", result["pass_rate"])
print("valid_count:", result["valid_count"])
print("fail_rate_by_question:", result["fail_rate_by_question"])
print("hardest_question:", result["hardest_question"])

print("分析報告:")
print(f"共 {scores.shape[0]} 位學生、{scores.shape[1]} 題。")
print(f"缺考值共 {result['missing_count']} 個。")
print("平均計算已排除 np.nan。")
print(f"全班及格率為 {result['pass_rate'] * 100:.2f}%。")
print(f"每題有效作答人數為 {result['valid_count']}。")
print(f"各題不及格率為 {np.round(result['fail_rate_by_question'] * 100, 2)}%。")
print(f"平均最低的是第 {result['hardest_question']} 題。")
