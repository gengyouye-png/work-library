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