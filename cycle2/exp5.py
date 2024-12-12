str1=input("Enter a string : ")
if str1[-3:]=="ing":
	print(str1[:-3]+"ly")
else:
	print(str1+"ing")
