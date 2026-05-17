#第四題_1
#linear search 搜尋字元

def linear_search(nums , target):
    for i in range(len(nums)):
        if nums[i] == target:
            return 1
        
    return -1
        
def main():
    nums = ['a', 'b', 'c', 'b']
    targrt = input("target:")
    print(linear_search(nums , targrt))
main()

#第四題_2
#搜尋數字
def linear_search(nums , target):
    for i in range(len(nums)):
        if nums[i] == target:
            return 1
        
    return -1
def main():
    nums = [10, 20, 30]
    targrt = int(input("target:"))
    print(linear_search(nums , targrt))
main()