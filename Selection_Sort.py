data =  [8, 4, 6, 2, 7, 3]
def selection_sort(data):
    for i in range(len(data) - 1):
        min = i 
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
        swap(data , i , min)
        print(data)
def swap(data , i , min):
    data[i] , data[min] = data[min] , data[i]
selection_sort(data)