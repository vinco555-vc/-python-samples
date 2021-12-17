

rows = int(input("How many rows"))
colums = int(input("How many colums"))
symbol = input("Enter Symbol")

for i in range(rows):
    for o in range(colums):
        print(symbol, end="")
    print()