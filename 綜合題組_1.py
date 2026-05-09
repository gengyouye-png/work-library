a , b , c = 0 ,0 ,0
max = 0
def temperature_status(temp):
    global a , b , c
    global max
    if temp >= 80:
        print("danger" )
        a += 1
    elif 60 <= temp < 80:
        print("warning" )
        b += 1
    elif temp < 60:
        print("normal" )
        c += 1
    if temp > max:
        max = temp



def main ():
    x = int(input())
    for i in range(x):
        temp = int(input())
        temperature_status(temp)
    print("danger=", a , "warning=", b , "normal=", c)
    print("MAX=" , max)
main()