def folder_size(folder):
    total = 0

    for item in folder[1:]:
        if isinstance(item, int):
            total += item
        else:
            total += folder_size(item)

    return total


def count_files(folder):
    count = 0

    for item in folder[1:]:
        if isinstance(item, int):
            count += 1
        else:
            count += count_files(item)

    return count


def max_depth(folder):
    deepest = 1

    for item in folder[1:]:
        if isinstance(item, list):
            depth = 1 + max_depth(item)
            if depth > deepest:
                deepest = depth

    return deepest


root = [
    "root",
    120,
    ["images", 50, 30, ["raw", 200, 180]],
    ["code", 10, ["old", 5, 8]],
    60,
]

print(f"總容量：{folder_size(root)} MB")
print(f"檔案數量：{count_files(root)}")
print(f"最大深度：{max_depth(root)}")
