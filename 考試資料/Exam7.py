n = int(input("請輸入正整數 n: "))
if 1 <= n <= 9:
    for i in range(1 , n+1):
        for j in range(1 ,n+1):
            print(f"{i*j: <3}" ,end =" ")
        print()