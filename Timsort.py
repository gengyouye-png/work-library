def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge(a, b):
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result += a[i:]
    result += b[j:]

    return result


runs = [
    [3, 4, 5],
    [1, 2, 9],
    [8, 7, 6],
    [10, 11, 12]
]

for i in range(4):
    print(f"Run {i+1}")
    print("原始:", runs[i])

    runs[i] = insertion_sort(runs[i])

    print("排序後:", runs[i])
    print()

a = merge(runs[0], runs[1])
b = merge(runs[2], runs[3])

print("第一輪合併A:", a)
print("第一輪合併B:", b)
print()

final = merge(a, b)

print("最後結果:", final)