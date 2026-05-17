#第二題
#selection_sort practise

def selection_sort(nums):
    for i in range(len(nums)):
        min = i
        for j in range( i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums
def main():
    nums = []
    number = list(map(int , input("nums:").split()))
    print(selection_sort(number))
main()