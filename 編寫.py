def merge_sorted(L, R):
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
    L = list(map(int , input("L : ").split()))
    R = list(map(int , input("R : ").split()))
    print(merge_sorted(L , R))
main()
    
    