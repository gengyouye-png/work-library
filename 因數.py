def count_divisors(num):
    """計算一個整數 num 有多少個正因數"""
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def main():
    try:
        user_input = input("請輸入正整數 n: ")
        if not user_input:
            return
        n = int(user_input)
        
        max_divisors = 0
        best_num = 0
        
        print("--- 各數字的因數個數 ---")
        
        for i in range(1, n + 1):
            current_count = count_divisors(i)
            
            print(f"數字 {i:2}: {current_count} 個因數")
            
            if current_count > max_divisors:
                max_divisors = current_count
                best_num = i
        
        print("-----------------------")
        print(f"結果：{best_num} {max_divisors}")
        print(f"(在 1 到 {n} 之間，{best_num} 擁有的因數最多，共 {max_divisors} 個)")
        
    except ValueError:
        print("請輸入有效的整數！")

if __name__ == "__main__":
    main()