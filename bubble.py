#氣泡排序法
data = [7, 3, 5, 2, 9, 1]
for i in range(len(data)-1):
    for j in range(len(data)-1-i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
    print(data)
