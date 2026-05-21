def reverse_sting(s):
    if len(s) <= 1:
        return s
    return reverse_sting (s[1:] )+ s[0]
def main():

    s = input("輸入:")
    print(reverse_sting(s))
main()