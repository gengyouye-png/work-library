import numpy as np

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
print("說明: wrong_bonus 無法對齊 raw_scores 的最後一維 3。")

print("broadcasting: bonus.shape (3,) 可對齊 raw_scores.shape (4, 3) 的最後一維。")
