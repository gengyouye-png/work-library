print("第三題")
year , month  = map(int,input().split())
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31天")
if month in [4, 6, 9, 11]:
    print("30天")   
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29天")
    else:
        print("28天")