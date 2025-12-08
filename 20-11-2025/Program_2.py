book = {"Title": "A Tale of Two Cities",
        "Author": "Charles Dickens",
        "Price": 147,
        "No_of_pages": 400}

# Add
book["Publisher"] = "Penguin Classics"

# Search
key = input("Enter a key to search: ")
if key in book:
    print(f"Found: {key} : {book[key]}")
else:
    print("Key not found")

# display
print(book)
