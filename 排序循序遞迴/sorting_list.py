#第一題
#sorting and list practise
#bubble_sort_practice

def sort_numbers(nums):
    n = len(nums)
    while n > 1:
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        n -= 1
    return nums
def main():
    nums = list(map(int, input("輸入：").split()))
    print("輸入:",sort_numbers(nums))
main()
