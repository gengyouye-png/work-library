#Python Matplotlib
#月銷售量折線圖 (Line Plot)
import matplotlib.pyplot as plt 
import numpy as np 

plt.rcParams["font.family"] = "Microsoft JhengHei"
plt.rcParams["axes.unicode_minus"] = False
x = np.array(["1月", "2月", "3月", "4月", "5月", "6月" ])
y = np.array([42, 55, 49, 63, 72, 85])
plt.plot(x, y, lw=0.5, color='k', marker='*', ms=15, label="銷售額")
plt.title("月銷售量趨勢")
plt.xlabel("月份")
plt.ylabel("銷售量" , rotation= 0)
plt.grid(True, linestyle="-", linewidth=2.0, alpha=0.5)
plt.gca().set_facecolor("#FFF3CD")
plt.legend()
plt.show()  
plt.savefig("q1_sales.png")

#科目平均分數長條圖 (Bar Chart)
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

#溫度與降雨量多子圖 (Subplots)
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
