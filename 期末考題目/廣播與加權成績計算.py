import numpy as np

# 原始成績矩陣
# 每一列代表一位學生
# 每一欄代表一個成績項目
raw_scores = np.array([
    [78, 82, 90],
    [60, 75, 70],
    [88, 92, 85],
    [45, 50, 58]
])

# bonus 有 3 個數字，剛好對應到每一列的 3 個成績項目
bonus = np.array([2, 0, 5])

# weights 是三個成績項目的權重
weights = np.array([0.3, 0.3, 0.4])

# 1. 印出 shape
# raw_scores 是 4 位學生、3 個成績，所以 shape 是 (4, 3)
# bonus 和 weights 都有 3 個數字，所以 shape 是 (3,)
print("raw_scores.shape：", raw_scores.shape)
print("bonus.shape：", bonus.shape)
print("weights.shape：", weights.shape)

# 2. 使用廣播 broadcasting，將 bonus 加到 raw_scores 的每一列
# NumPy 會自動把 bonus 套用到每位學生的三個成績項目
adjusted_scores = raw_scores + bonus

# 3. 使用 np.clip 將分數限制在 0 到 100 之間
# 如果加分後超過 100，就會變成 100
adjusted_scores = np.clip(adjusted_scores, 0, 100)

# 4. 使用 weights 計算每位學生的加權總分
# adjusted_scores * weights 會先讓每個成績乘上對應權重
# sum(axis=1) 表示每一列相加，得到每位學生的總分
final_scores = (adjusted_scores * weights).sum(axis=1)

# 5. 判斷每位學生是否及格
# 加權總分大於或等於 60 分就是及格
passed = final_scores >= 60

# 6. 錯誤示範：wrong_bonus 的 shape 是 (4,)
# raw_scores 的 shape 是 (4, 3)
# NumPy 會想要從最後一個維度開始對齊：
#     raw_scores 最後一個維度是 3
#     wrong_bonus 最後一個維度是 4
# 3 和 4 不相等，也沒有其中一個是 1，所以不能 broadcasting
wrong_bonus = np.array([2, 0, 5, 1])

# 這行如果真的執行會錯誤：
# wrong_scores = raw_scores + wrong_bonus

# 7. 輸出結果與說明
print("加分後成績：")
print(adjusted_scores)

print("加權總分：", final_scores)
print("是否及格：", passed)

print("wrong_bonus.shape：", wrong_bonus.shape)
print("wrong_bonus 不能直接加到 raw_scores，因為 (4, 3) 和 (4,) 的最後一個維度 3、4 無法對齊。")
print("broadcasting 是從 shape 的最後面開始比對，數字相同或其中一個是 1 才能自動擴展。")
