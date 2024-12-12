str1=input("Enter first string : ")
str2=input("Enter second string : ")
swap_str1=str1[0]+str2[1]+str1[2:]
swap_str2=str2[0]+str1[1]+str2[2:]
str3=swap_str1+" "+swap_str2
print(str3)
