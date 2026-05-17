def flatten(data):

    if not isinstance(data, list):
        return [data]

    result = []

    for item in data:
        result += flatten(item)

    return result


def main():

    data = eval(input("data = "))

    print(flatten(data))


main()