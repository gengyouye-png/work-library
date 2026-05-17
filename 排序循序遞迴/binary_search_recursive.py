#第九題
#binary_search_recursive
def binary_search_recursive(nums, target):

    def search(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return search(mid + 1, right)
        else:
            return search(left, mid - 1)

    return search(0, len(nums) - 1)


def main():

    nums = [1, 3, 5, 7, 9, 11]

    target = int(input("target = "))

    print(binary_search_recursive(nums, target))


main()