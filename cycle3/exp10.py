n = int(input("Enter a number : "))
print("Factors of ", n ," = ", end = " ")
count = 1
while count <= n:
        if n % count == 0:
                print(count, end = " ")
        count = count + 1
print()

