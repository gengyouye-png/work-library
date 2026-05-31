def sort(nums , target , L , R ):
    if L > R :
        return -1
    mid = (L + R ) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return sort(nums , target , mid + 1 , R)
    else:
        return sort(nums , target , L , mid - 1)
def main():
    nums = [1 , 3 ,5 ,7 ,9, 11]
    target = int(input(""))
    print(sort(nums , target , 0 , len(nums) - 1))
main()