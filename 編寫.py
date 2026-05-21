def sort(students):
    
    return sorted(
        students,
        key = lambda x : (-x['score'] , x['name'])
    )
def main():
    students = []
    n = int(input("學生人數:"))
    for i in range(n):
        name = input("name:")
        score = int(input("score:"))
        students.append({
            'name':name,
            'score':score
        })
    print(sort(students))
main()
