#整數分類
def judbe(n):
    if -100000 <= n <= 100000:
        if n > 0:
            if n % 2 == 0:
                return "positive even"
            else:
                return "positive odd"
        elif n < 0:
            if n % 2 == 0:
                return "negative even"
            else:
                return "negative odd"
        else:
            return "zero"
    else:
        print("輸入失敗")
    
n = int(input("請輸入一個整數:"))
result = judbe(n)
print(result)

#｜三數極值
def judge(a ,b ,c):
    max = 0
    middle = 0
    min = 0
    if a > b and a > c: 
        max = a
        if b > c:
            middle = b
            min = c 
        else:
            midde = c
            min =b
    elif b > a and b > c:
        max = b
        if a > c:
            middle = a
            min = c
        else:
            middle = c
            min = a 
    else:
        max = c
        if a > b:
            middle = a
            min = b
        else:
            middle = b
            min =a
    return max , middle , min
def main():
    a , b , c = map(int , input("請輸入個數:").split())
    max , middle , min = judge(a , b ,c)
    print(max , middle , min)

main()

#座標位置判斷
def judge(x , y):
    if x > 0:
        if y > 0:
            return"Q1"
        elif y < 0:
            return "Q4"
        else:
            return "x-axis"
    elif x < 0:
        if y > 0:
            return "Q2"
        elif y < 0:
            return "Q3"
        else:
            return "x-axis"
    else:
        if y == 0:
            return "origin"
        elif y > 0:
            return "y-axis"
        else:
            return "y-axis"
def main():
    x , y = map(int , input("請輸入座標:").split())
    result = judge(x , y)
    print(result)
main()

#月份天數
def judge(year , month):
    if month in [1 , 3 , 5 , 7 , 8 , 10 , 12]:
        return 31
    elif month in [4 , 6 , 9 , 11]:
        return 30
    elif month in [2]:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return "INVALID"

def main():
    year , month = map(int , input("請輸入年和月:").split())
    if 1 <= year <= 9999 and 1 <= month <= 12:
        day = judge(year , month)
    else:
        day = "INVALID"
    print(day)
main()

#點到原點的距離_1
import math 
def calculate(x , y):
    distance = math.hypot(x, y)
    return distance
def main():
    x , y = map(float , input("請輸入座標:").split())
    if -1000 <= x <= 1000 and -1000 <= y <= 1000:
        distance = calculate(x , y)
    else:
        print("輸入超出範圍")
    print(f"距離原點地的距離為:{distance:.4f}")
main()
#點到原點的距離_2 
def calculate(x, y):
    distance = (x**2 + y**2)**0.5
    return distance

def main():
    x, y = map(float, input("請輸入座標: ").split())

    if -1000 <= x <= 1000 and -1000 <= y <= 1000:
        distance = calculate(x, y)
        print(f"距離原點的距離為: {distance:.4f}")
    else:
        print("輸入超出範圍")

main()

#會員折扣統計

def judge(level , amount):
    if level == "VIP" and "vip" and "Vip":
        if amount < 1000:
            return amount * 0.95
        elif 1000 <= amount < 5000:
            return amount * 0.8 
        else: 
            return amount * 0.7
        
    elif level == "Gold" and "gold" and "GOLD":
        if amount < 1000:
            return amount * 0.98
        elif 1000 <= amount < 5000:
            return amount * 0.85
        else:
            return amount * 0.75
    elif level == "Normal" and "NORMAL" and "normal":
        if amount < 1000:
            return amount * 1
        elif 1000 <= amount < 5000:
            return amount * 0.9
        else:
            return amount * 0.8
    else:
        return "ERROR"
    
def main():
    total = 0
    max = 0
    n = int(input("請輸入消費資料筆數:"))
    for i in range(n):
        level , amount = input("請輸入會員等級和消費金額:").split()
        judge_result = judge(level , int(amount))
        if judge_result == "ERROR":
            print(judge_result)
        else:
            print("折扣後金額" f"{judge_result:.1f}")
            total += judge_result
            if max < judge_result:
                max = judge_result
                    
    print(f"折扣後總金額{total:.1f}")
    print(f"折扣後的最高金額{max:.1f}")
main()

#五門課畢業門檻判斷
def judge(score , credit):
    if score >= 60 :
        return credit
    else:
        return 0
def main():
    credits = 0
    a , b = 0 , 0
    for i in range(2):
        score , credit = map(float , input("請輸入必修成績和學分:").split())
        if 0 <= score <= 100 and 0 < credit <= 5:
            credits += judge(score , credit)
            print(f"成績為{score} , 學分為{credit} ")
        else:
            a += 1
            print("輸入超出範圍")
    for i in range(3):
        score , credit = map(float , input("請輸入選修成績和學分:").split())
        if 0 <= score <= 100 and 0 < credit <= 5:
            credits += judge(score , credit)
            print(f"成績為{score} , 學分為{credit} ")
        else:
            b += 1
            print("輸入超出範圍")
    print(f"總學分{credits}")
    if a > 0 or b >= 2 or credits < 10:
        print("fall")
    else:
        print("pass")  

main()
#因數個數統計
def judge(num):
    count = 0 
    for i in range(1 , num + 1):
        if num % i == 0:
            count += 1
        else:
            count += 0
    return count
def main():
    count = 0 
    max = 0
    n = int(input("請輸入一正整數:"))
    for i in range(1 , n + 1):
        count = judge(i)
        print(f"數字{i}: {count}個因數")
        if max < count:
            max = count
            b = i
        
        
    print(f"在1到{n}之間，數字{b}最多因數，有{max}個")
main()

#｜函式：日期是否合法與一年中的第幾天
def is_leap(year):
    if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
def day_in_month(year , month):
    if month in [1, 3, 5, 7, 8, 10, 12 ]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if is_leap == True:
            return 29
        else:
            return 28
def day_of_year(year , month , day):
    total = 0
    for i in range(1 , month):
        total += day_in_month(year , i)
        total += day
    return total

def main():
    year , month , day = map(int , input("請輸入年月日:").split())
    if 1 <= year <= 9999 and 1 <= month <= 12 and 1 < day < day_in_month(year , month):
        total = day_of_year(year , month , day)
        print(f"今年是第{year}年的第{total}天")
main()



#函式：優秀學生資格判斷
def Credit_weights(score , credit):
    weighting_credit = score * credit
    return weighting_credit

def judge(score , credit):
    score_credits = 0
    if score >= 60:
        score_credits += credit
    
    else:
        score_credits += 0
    return score_credits
def judge_fail(score):
    failed = 0
    if score < 60:
        failed += 1
    else:
        failed += 0
    return failed
def main():
    credits = 0
    weighting_credit = 0
    score_credits = 0
    average_credit_weight = 0
    failed = 0
    n = int(input("請輸入修課門數:"))

    if 1 <= n <= 20:
        for i in range(1 , n + 1):
            score , credit = map(float , input("請輸入分數和學分:").split())
            if 0 <= score <= 100 and 1 <= credit <= 5:
                credits += credit
                weighting_credit += Credit_weights(score , credit)
            else:
                print("超過範圍:")
            score_credits += judge(score , credit)
            failed += judge_fail(score)
        service = int(input("請輸入服務時數:"))
        average_credit_weight = weighting_credit / credits  # type: ignore 計算加權平均（以學分為權重)

        if score_credits >= 15 and  average_credit_weight >= 80 and service >= 10:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    print(f"加權平均:{average_credit_weight:.2f}")
main()


