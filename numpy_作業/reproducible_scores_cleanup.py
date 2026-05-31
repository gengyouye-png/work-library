import numpy as np

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
