name=input("Enter the first names seperated by comma : ")
count=sum(name.lower().count('a')for name in name)
print("occurences of a and A : ",count)
