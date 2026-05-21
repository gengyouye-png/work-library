#第六題
#Merge Two Sorted Arrays

def merge_sorted(a, b):

    result = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
        
    return result

def main():

    a = [1, 3, 5]
    b = [2, 3, 4, 8]

    print(merge_sorted(a, b))


main()

'''def merge_sorted(L, R):
    result = []
    while len(L) and len(R):
        if (L[0] <  R[0]):
            result.append(L.pop(0))
        else:
            result.append(R.pop(0))
    result = result + L if  len(L) else result + R 
    return result


def main():
    L = []
    R = []
    L = list(map(int , ("L : ").split()))
    R = list(map(int , input("R : ").split()))
    print(merge_sorted(L , R))
main()
    
    '''