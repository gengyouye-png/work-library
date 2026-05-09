def power_fee(kwh):
    if kwh <= 100:
        return kwh * 5
    elif 100 < kwh <= 200:
        return 100 * 5 + (kwh - 100) * 7
    elif kwh > 200:
        return 100 * 5 + 100 * 7 + (kwh - 200) * 9

def main():
    total = 0
    over_budget_count = 0
    over_budget = 1000
    sever = int(input("請輸入伺服器數量："))
    for i in range(sever):
        kwh = float(input("請輸入第{}台用電量:" .format(i + 1)))
        fee = power_fee(kwh)
        total += fee # type: ignore
        if fee > over_budget:
            over_budget_count += 1
        print("第{}台電費為: {}" .format(i + 1 , fee))
    print("總電費為: {}".format(total))
    print("超過預算的伺服器數量:{}".format(over_budget_count))
main()