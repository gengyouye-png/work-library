def recursive_sum(n):
    if n == 0:
        return 0
    
    return n + recursive_sum(n - 1)

def main():
    n = int(input("請輸入:"))
    print("輸入:" , recursive_sum(n))
main()