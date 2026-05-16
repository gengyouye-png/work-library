def radix_sort(data):
    print("第0趟")
    print("原始序列")
    print(data)
    print()

    exp = 1
    digit_name = ["個位數", "十位數", "百位數"]

    for step in range(3):
        buckets = [[] for _ in range(10)]

        for num in data:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        data = []

        for bucket in buckets:
            data.extend(bucket)

        print(f"第{step + 1}趟")
        print(digit_name[step])
        print(data)
        print()

        exp *= 10


data = [170, 45, 75, 90, 802, 24, 2, 66]

radix_sort(data)