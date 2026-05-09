shift = int(input(""))
s = input("")

def string(s , shift):
    a = ""
    for c in s:
        if 'a' <= c <= 'z':
            new_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            a += new_c
        elif 'A' <= c <= 'Z':
            new_c = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            a += new_c
        else:
            a += c
    return a

print(string(s , shift))