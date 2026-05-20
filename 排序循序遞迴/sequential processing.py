#第五題
# sequential processing and one-pass scan

def summarize(nums):
    tatol = 0
    min_value = nums[0]
    max_value = nums[0]
    for i in range(len(nums)):
        if nums[i] < min_value:
            min_value = nums[i]
        if nums[i] > max_value:
            max_value = nums[i]
        tatol += nums[i]
        age = tatol / len(nums)

    return tatol, min_value, max_value , age
def main():
    nums = []
    number = list(map(int, input("nums:").split()))
    summarize(number)
    print("min:",summarize(number)[1],"max:",summarize(number)[2],"sum:",summarize(number)[0],f"avg:{summarize(number)[3]:.4f}")
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