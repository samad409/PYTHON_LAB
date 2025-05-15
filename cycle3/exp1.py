#factorial

n = int(input("Enter the number : "))
fact = 1
if n==0:
	print("Factorial = 1")
else:
	for i in range(1, n + 1):
    		fact = fact * i
	print("Factorial : ", fact)

