#第五題
# sequential processing and one-pass scan

def summarize(nums):
    total = 0
    min_index = nums[0]
    max_index = nums[0]
    for i in range(len(nums)):
        if max_index < nums[i]:
            max_index = nums[i]
        elif min_index >nums[i]:
            min_index = nums[i]
        total += nums[i]
        agv = total / len(nums)

    return (min_index , max_index , total , agv )

def main():
    nums = []
    nums = list(map(int , input("輸入:").split()))
    min , max , sum , agv = summarize(nums)
    print("min",min ,"max",max , "sum",sum , f"agv:{agv:.4f}")

main()


'''def summarize(nums):
    total = 0

    min_num = nums[0]
    max_num = nums[0]

    for i in range(len(nums)):
        total += nums[i]

        if nums[i] < min_num:
            min_num = nums[i]

        if nums[i] > max_num:
            max_num = nums[i]

    avg = total / len(nums)

    return total, min_num, max_num, avg


def main():
    nums = list(map(int, input("nums: ").split()))

    result = summarize(nums)

    print(
        "min:", result[1],
        "max:", result[2],
        "sum:", result[0],
        f"avg:{result[3]:.4f}"
    )


main()'''