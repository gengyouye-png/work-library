def quick_sort(data, level=0):
    print("    " * level + f"子序列: {data}")

    if len(data) <= 1:
        print("    " * level + f"排序結果: {data}")
        return data

    pivot = data[0]

    less = []
    equal = []
    greater = []

    for num in data:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    print("    " * level + f"pivot = {pivot}")
    print("    " * level + f"小於 pivot: {less}")
    print("    " * level + f"等於 pivot: {equal}")
    print("    " * level + f"大於 pivot: {greater}")
    print()

    left = quick_sort(less, level + 1)
    right = quick_sort(greater, level + 1)

    result = left + equal + right

    print("    " * level + f"本子序列排序結果: {result}")
    print()

    return result


data = [5, 1, 8, 3, 7, 2, 6, 4]

sorted_data = quick_sort(data)

print("最後排序結果:", sorted_data)