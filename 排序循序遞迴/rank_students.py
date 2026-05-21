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