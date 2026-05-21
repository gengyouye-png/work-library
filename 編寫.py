def binary_search_recursive(nums , traget , left , right):
    if left > right :
        return -1
    mid = (left + right) // 2
    if nums[mid] == traget:
        return mid
    elif nums[mid] < traget:
        return binary_search_recursive(nums , traget , mid + 1 , right)
    else:
        return binary_search_recursive(nums , right , left , mid -1)
def main():
    nums = [1, 3, 5, 7, 9, 11]
    target = int(input("輸入:"))
    print(binary_search_recursive(nums, target, 0, len(nums) - 1))
main()
