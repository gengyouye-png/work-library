#第七題
#recursive_sum

def recursive_sum(n):

    if n == 0:
        return 0

    return n + recursive_sum(n - 1)


def main():

    n = int(input("n = "))

    print(recursive_sum(n))


main()