elements = input("Enter elements separated by spaces: ").split()

elements = list(map(int, elements))

product = list(map(lambda x: x * 3, elements))

print("The values * 3 are : ", product)

