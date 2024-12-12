num=input("Enter integers sepereted by comma : ").split(',')
result=[]
for i in num:
	number=int(i)
	if number%2!=0:
		result.append(number)
print(result)
