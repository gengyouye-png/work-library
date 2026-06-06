import matplotlib.pyplot as plt
import numpy as np 

plt.rcParams["font.family"] = "Microsoft JhengHei"
plt.rcParams["axes.unicode_minus"] = False
x = np.array(["國文", "英文", "數學", "程式設計"])
y = np.array([76, 68, 59, 82])
plt.title = ("科目平均分數比較")

bars = plt.bar(x, y)
plt.bar_label(
    bars,
    labels=y,
    padding=3
)
plt.axhline(
    y = 60,
    color = "red",
    linestyle = ':',
    label = "及格線"
)
plt.legend()
plt.show()
plt.savefig("q2_scores.png")