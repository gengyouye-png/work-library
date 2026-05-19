#第十題
#flatten

def flatten(data):

    if not isinstance(data, list):
        return [data]
    result = []
    for item in data:
        result += flatten(item)

    return result


def main():
    data = [1, [2, 3], [[4], 5], []]
    print(flatten(data))


main()