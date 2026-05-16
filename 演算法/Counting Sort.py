def counting_sort(data):
    max_num = max(data)

    count = [0] * (max_num + 1)

    for num in data:
        count[num] += 1

    print("數值:")
    for i in range(1, max_num + 1):
        print(i, end=" ")
    print()

    print("出現次數:")
    for i in range(1, max_num + 1):
        print(count[i], end=" ")
    print("\n")

    result = []

    for num in range(1, max_num + 1):
        for j in range(count[num]):
            result.append(num)

    print("依照出現次數展開後的排序結果:")
    print(result)


data = [4, 2, 2, 8, 3, 3, 1]

counting_sort(data)