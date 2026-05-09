def analyze_batch(total, defect):
    yield_rate = (total - defect) / total * 100
    ratio = defect / total
    
    if defect == 0:
        grade = "A"
    elif ratio <= 0.02:
        grade = "B"
    elif ratio <= 0.05:
        grade = "C"
    else:
        grade = "REJECT"
    
    return yield_rate, grade


N = int(input("請輸入批次數量:"))

accept = 0
reject = 0

worst_ratio = -1
worst_batch = 0

for i in range(1, N + 1):
    total, defect = map(int, input(f"請輸入批次{i}的總數和缺陷數:").split())
    yield_rate, grade = analyze_batch(total, defect)
    print(f"batch {i}: {yield_rate:.1f} {grade}")
    if grade in ["A", "B", "C"]:
        accept += 1
    else:
        reject += 1
    
    ratio = defect / total
    if ratio > worst_ratio:
        worst_ratio = ratio
        worst_batch = i

# 最後輸出
print(f"accept={accept}")
print(f"reject={reject}")
print(f"worst_batch={worst_batch}")