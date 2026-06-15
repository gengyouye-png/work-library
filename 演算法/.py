data  = [11 , 2 , 5 , 88 , 65 , 45]
n = len(data)
while n > 1:
    for j in range (len(data) - 1):
        for i in range(len(data) - 1 - j):
            if data[i] > data[i+1]:
                data[i] , data[i+1] = data[i+1] , data[i]
        n-=1
print(data)