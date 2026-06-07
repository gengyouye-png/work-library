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
