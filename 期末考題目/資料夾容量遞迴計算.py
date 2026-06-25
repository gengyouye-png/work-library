# 資料夾容量遞迴計算


def folder_size(folder):
    # folder[0] 是資料夾名稱，從 folder[1] 開始才是內容
    total = 0

    for item in folder[1:]:
        # base case：
        # 如果 item 是 int，代表它是檔案大小，直接加進總容量
        if isinstance(item, int):
            total = total + item

        # recursive case：
        # 如果 item 是 list，代表它是子資料夾，要繼續呼叫 folder_size
        else:
            total = total + folder_size(item)

    return total


def count_files(folder):
    count = 0

    for item in folder[1:]:
        # base case：
        # 如果 item 是 int，代表找到 1 個檔案
        if isinstance(item, int):
            count = count + 1

        # recursive case：
        # 如果 item 是 list，代表子資料夾，繼續進去計算檔案數
        else:
            count = count + count_files(item)

    return count


def max_depth(folder):
    # base case：
    # 如果資料夾底下沒有任何子資料夾，最大深度就是 1
    deepest = 1

    for item in folder[1:]:
        # 只有 list 才是子資料夾，檔案 int 不會增加資料夾深度
        if isinstance(item, list):
            # 子資料夾的深度要再 +1，代表包含目前這一層
            child_depth = 1 + max_depth(item)

            if child_depth > deepest:
                deepest = child_depth

    return deepest


# 測試資料
root = [
    "root",
    120,
    ["images", 50, 30, ["raw", 200, 180]],
    ["code", 10, ["old", 5, 8]],
    60
]

# 輸出結果
print("總容量：", folder_size(root), "MB")
print("檔案數量：", count_files(root))
print("最大深度：", max_depth(root))

# 用自己的話簡短說明其中一個遞迴停止條件
print("遞迴停止條件說明：在 folder_size 中，如果遇到 int，代表已經是檔案，不是資料夾，所以直接回傳檔案大小，不再繼續往下找。")
