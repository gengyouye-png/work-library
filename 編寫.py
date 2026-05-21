def sort_numbers(nums):
    n = len(nums)
    while n > 1:
        for i in range(n - 1):
            if nums[i] > nums[i +1]:
                nums[i] , nums[i + 1] = nums[i + 1],nums[i]
        n -= 1
    return nums
def main():
    nums = []
    nums = list(map(int , input("輸入:").split()))
    print(sort_numbers(nums))
main()