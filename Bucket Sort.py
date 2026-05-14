def bucket_sort(data):
    buckets = [[] for _ in range(5)]

    for num in data:
        if 0.0 <= num < 0.2:
            buckets[0].append(num)
        elif 0.2 <= num < 0.4:
            buckets[1].append(num)
        elif 0.4 <= num < 0.6:
            buckets[2].append(num)
        elif 0.6 <= num < 0.8:
            buckets[3].append(num)
        elif 0.8 <= num <= 1.0:
            buckets[4].append(num)

    ranges = [
        "[0.0,0.2)",
        "[0.2,0.4)",
        "[0.4,0.6)",
        "[0.6,0.8)",
        "[0.8,1.0]"
    ]

    result = []

    for i in range(5):
        print(f"B{i}")
        print("區間:", ranges[i])
        print("放入的資料:", buckets[i])

        buckets[i].sort()

        print("桶內排序後:", buckets[i])
        print()

        result.extend(buckets[i])

    print("串接後的最終結果:")
    print(result)


data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12]

bucket_sort(data)