books = [
    "Python Crash Course",
    "Nihongo Renshuu",
    "Clean Code",
    "Rich Dad Poor Dad"
]
count = 0
while True:

    search = input("Enter book name to search (or 'exit' to quit): ").lower()
    if(search == "exit"):
        break

    i = 0
    flag = 0

    while i < len(books):
        if(search == books[i].lower()):
            count += 1
            flag = 1
        i += 1

    if flag:
        print("Book found!")
    else:
        print("Book not available.")

print(f"Total search made: {count}")