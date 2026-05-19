def bubble(num):
    for i in range(len(num)-1):
        for j in range(len(num) -1 -i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1] , num[j]
        print(num)
        return num
    
def main():
    data = list(map(int , input("num:").split()))
    print(bubble(data))
main()