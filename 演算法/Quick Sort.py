def quick_sort(data):
    if len(data) <= 1:
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

    left = quick_sort(less)
    right = quick_sort(greater)

    result = left + equal + right

    print(result)

    return result


data = [5, 1, 8, 3, 7, 2, 6, 4]

sorted_data = quick_sort(data)