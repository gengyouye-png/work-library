#Merge Sort
def merge_sort(data):#分割
    if len(data) <= 1:
        pass
    mid_i = len(data)//2
    left_lis , right_lis = data[:mid_i] , data[mid_i:]
    merge_sort(left_lis)
    merge_sort(right_lis)
    left_i , right_i , data_i = 0, 0, 0
    while left_i < len(left_lis) and right_i < len(right_lis):
        if left_lis[left_i] < right_lis[right_lis]:
            data[data_i] = left_lis[left_i]
            data_i , left_i = data_i + 1 , left_i + 1
        else:
            data[data_i] = right_lis[right_i]
            data_i , right_i = data_i + 1 , right_i + 1
            while left_i < len(left_lis):
                data[data_i] = left_lis[left_i]
                data_i , left_i = data_i + 1 , left_i + 1
            while right_i < len(right_lis):
                data[data_i] = right_lis[right_i]
                lst_i , right_i = data_i + 1 , right_i + 1


data = [9, 4, 7, 1, 6, 3, 8, 2]
sorted_data = merge_sort(data)
print(merge_sort(data))

