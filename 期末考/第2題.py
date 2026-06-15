def search_by_keyword(books, keyword):
    results = []
    keyword = keyword.lower()

    for book in books:
        if keyword in book[1].lower() or keyword in book[2].lower():
            results.append(book)

    return results


def search_first_available_python(books):
    for book in books:
        if "python" in book[1].lower() and book[3] == "可借":
            return book

    return None


def print_books(books):
    if not books:
        print("查無符合資料")
        return

    print("書號\t書名\t作者\t狀態")
    for book in books:
        print(f"{book[0]}\t{book[1]}\t{book[2]}\t{book[3]}")


books = [
    ["B001", "Python Basics", "Lin", "可借"],
    ["B002", "Data Science Notes", "Wang", "借出"],
    ["B003", "Matplotlib Guide", "Chen", "可借"],
    ["B004", "Recursive Thinking", "Lin", "可借"],
    ["B005", "NumPy Practice", "Huang", "借出"],
    ["B006", "Python Project", "Tsai", "可借"],
]

for keyword in ["python", "lin"]:
    print(f'keyword = "{keyword}"')
    print_books(search_by_keyword(books, keyword))
    print()

print("第一本書名含 Python 且狀態為可借的書：")
book = search_first_available_python(books)
print_books([book] if book else [])
