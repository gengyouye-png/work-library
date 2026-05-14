#插入排序法
data = [6, 2, 5, 3, 7, 4]
def inserrion_sort(data):
    for i in range(1 , len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and  data[j] > key:
            a = data[j]
            data[j] = data[j+ 1]
            data[j + 1] = a
            j -= 1
        print(data)
inserrion_sort(data)
