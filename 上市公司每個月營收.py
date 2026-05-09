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