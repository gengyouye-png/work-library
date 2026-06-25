import numpy as np
import matplotlib.pyplot as plt

# 月份資料
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])

# 商品名稱
products = np.array(["Notebook", "Pen", "Sticker"])

# 銷售資料
# 每一列代表一個月份
# 每一欄代表一種商品
sales = np.array([
    [120, 300, 180],
    [150, 280, 210],
    [130, 350, 240],
    [170, 330, 260],
    [160, 390, 300],
    [190, 410, 320]
])

# 1. 計算每個月份的總銷售量
# axis=1 表示橫向相加，也就是每一個月份三種商品的總和
monthly_total = np.sum(sales, axis=1)

# 2. 計算每個商品 6 個月內的總銷售量
# axis=0 表示直向相加，也就是每一種商品六個月份的總和
product_total = np.sum(sales, axis=0)

# 3. 找出總銷售量最高的月份
max_month_index = np.argmax(monthly_total)
max_month = months[max_month_index]
max_month_sales = monthly_total[max_month_index]

# 輸出基本統計結果
print("每月總銷售量：", monthly_total)
print("每個商品總銷售量：", product_total)
print("總銷售量最高的月份：", max_month)
print("該月份銷售量：", max_month_sales)

# 4. 畫折線圖：每個月份的總銷售量
plt.figure()
plt.plot(months, monthly_total, marker="o")
plt.title("Monthly Total Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)

# 標記最高銷售月份
plt.scatter(max_month, max_month_sales, color="red")
plt.text(max_month, max_month_sales, str(max_month_sales))

# 儲存折線圖
plt.savefig("期末考題目/q5_monthly_total.png")
plt.close()

# 5. 畫長條圖：每個商品 6 個月總銷售量
plt.figure()
plt.bar(products, product_total)
plt.title("Product Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

# 在每個長條上方標記數值
for i in range(len(products)):
    plt.text(products[i], product_total[i], str(product_total[i]), ha="center")

# 儲存長條圖
plt.savefig("期末考題目/q5_product_total.png")
plt.close()
