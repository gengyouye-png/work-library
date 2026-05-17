#第八題
#reverse_string


def reverse_string(s):

    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


def main():

    s = input("s = ")

    print(reverse_string(s))


main()