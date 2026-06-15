from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
products = np.array(["Notebook", "Pen", "Sticker"])
sales = np.array([
    [120, 300, 180],
    [150, 280, 210],
    [130, 350, 240],
    [170, 330, 260],
    [160, 390, 300],
    [190, 410, 320],
])

monthly_totals = np.sum(sales, axis=1)
product_totals = np.sum(sales, axis=0)
highest_month_index = np.argmax(monthly_totals)
output_dir = Path(__file__).parent

print("每月總銷售量：")
for month, total in zip(months, monthly_totals):
    print(f"{month}: {total}")

print("各產品六個月總銷售量：")
for product, total in zip(products, product_totals):
    print(f"{product}: {total}")

print(
    f"總銷售量最高月份：{months[highest_month_index]}，"
    f"銷售量：{monthly_totals[highest_month_index]}"
)

plt.figure(figsize=(8, 5))
plt.plot(months, monthly_totals, marker="o", linewidth=2, color="royalblue")
plt.title("Monthly Total Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True, linestyle="--", alpha=0.5)

for month, total in zip(months, monthly_totals):
    plt.text(month, total + 10, str(total), ha="center")

plt.tight_layout()
plt.savefig(output_dir / "q5_monthly_total.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 5))
bars = plt.bar(products, product_totals, color=["steelblue", "orange", "seagreen"])
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.grid(axis="y", linestyle="--", alpha=0.5)

for bar, total in zip(bars, product_totals):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 10,
        str(total),
        ha="center",
    )

plt.tight_layout()
plt.savefig(output_dir / "q5_product_total.png", dpi=300)
plt.close()
