s = input("請輸入一個字串: ")
shift = int(input("請輸入移位數: "))

def shift_string(s, shift):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char

        elif 'A' <= char <= 'Z':   # ⭐ 新增這段
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char

        else:
            result += char

    return result

print(shift_string(s, shift))