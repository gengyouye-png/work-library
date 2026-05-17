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

#第三題
# rank_students

def rank_students(students):

    return sorted(
        students,
        key=lambda x: (-x['score'], x['name'])# tuple 多條件排序
    )


def main():

    students = [
        {'name': 'Bob', 'score': 88},
        {'name': 'Amy', 'score': 95},
        {'name': 'Carl', 'score': 95}
    ]

    ranked_students = rank_students(students)

    print(ranked_students)


main()
'''lambda 匿名函式 + tuple 多條件排序，建立一個臨時函式'''

#第三題之可輸入條件
#輸入條件
def rank_students(students):
    return sorted(
        students,
        key=lambda x: (-x['score'], x['name'])
    )
def main():
    students = []
    n = int(input("學生人數:"))
    for i in range(n):
        name = input("學生姓名:")
        score = int(input("學生分數:"))
        students.append({
            'name': name,
            'score': score
        })
    print(rank_students(students))
main()

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

#第六題
#Merge Two Sorted Arrays

def merge_sorted(a, b):

    result = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
        
    return result

def main():

    a = [1, 3, 5]
    b = [2, 3, 4, 8]

    print(merge_sorted(a, b))


main()

#第七題
#recursive_sum

def recursive_sum(n):

    if n == 0:
        return 0

    return n + recursive_sum(n - 1)


def main():

    n = int(input("n = "))

    print(recursive_sum(n))


main()

#第八題
#reverse_string


def reverse_string(s):

    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


def main():

    s = input("s = ")

    print(reverse_string(s))


main()

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

#第十題
#flatten

def flatten(data):

    if not isinstance(data, list):
        return [data]
    result = []
    for item in data:
        result += flatten(item)

    return result


def main():
    data = [1, [2, 3], [[4], 5], []]
    print(flatten(data))


main()