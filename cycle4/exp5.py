elements = input("Enter elements separated by spaces: ").split()
elements = list(map(int, elements))
squares = list(map(lambda x: 2 ** x, elements))
print("The squares are:", squares)

