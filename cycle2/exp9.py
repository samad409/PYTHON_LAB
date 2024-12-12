num=input("Enter integers seperateed by commas : ").split(',')
result=[]
for i in num:
	if int(i)>100:
		result.append('over')
	else:
		result.append(int(i))
print(result)
