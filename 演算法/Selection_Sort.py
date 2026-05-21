def sort(nums):
    for i in range(len(nums) - 1):
        min = i
        for j in range(1 + i ,len(nums)):
            if nums[min] > nums[j]:
                min = j
        nums[min], nums[j] = nums[j] , nums[min]
    return nums
def main():
    nums = []
    nums = list(map(int , input("nums:").split()))
    print(sort(nums))
main()