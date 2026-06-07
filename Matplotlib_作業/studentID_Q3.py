import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Microsoft JhengHei"
plt.rcParams["axes.unicode_minus"] = False

days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
temperature = np.array([23, 25, 24, 28, 30, 29, 26])
rainfall = np.array([5, 0, 12, 3, 0, 18, 7])
fig , axes = plt.subplots(2,1,figsize = (8 , 6))#fig : 整張圖 figsize = (8 , 6)設定圖片大小

axes[0].plot(days , temperature , marker = '*' , color="k" )
axes[0].set_ylabel("溫度" )
for day, value in zip(days, temperature):
    axes[0].annotate(
        value,
        (day, value),
        xytext=(0, 6),
        textcoords="offset points",
        ha="center"
    )
bars = axes[1].bar(days , rainfall )
axes[1].bar_label(bars, padding=1)
axes[1].set_ylabel("降雨量(mm)" )
fig.suptitle("一周天氣資訊")

fig.patch.set_facecolor("#C4C1C1")
axes[0].set_facecolor("#EFE9DC")
axes[1].set_facecolor("#F6E2D9")
plt.tight_layout()
plt.savefig("q3_weather.png")
plt.show()
