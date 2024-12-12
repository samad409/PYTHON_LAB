str1=input("Enter a string : ")
f_char=str1[0]
newstr=f_char+str1[1:].replace(f_char,"$")
print("Modified string : ",newstr)
