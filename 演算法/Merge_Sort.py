def merge_sort(data):
    if len(data) <= 1:
        return data

    mid_i = len(data) // 2

    left_lis = data[:mid_i]
    right_lis = data[mid_i:]

    merge_sort(left_lis)
    merge_sort(right_lis)

    left_i, right_i, data_i = 0, 0, 0

    while left_i < len(left_lis) and right_i < len(right_lis):
        if left_lis[left_i] < right_lis[right_i]:
            data[data_i] = left_lis[left_i]
            left_i += 1
        else:
            data[data_i] = right_lis[right_i]
            right_i += 1

        data_i += 1

    while left_i < len(left_lis):
        data[data_i] = left_lis[left_i]
        data_i += 1
        left_i += 1

    while right_i < len(right_lis):
        data[data_i] = right_lis[right_i]
        data_i += 1
        right_i += 1

    return data


data = [9, 4, 7, 1, 6, 3, 8, 2]

sorted_data = merge_sort(data)

print(sorted_data)