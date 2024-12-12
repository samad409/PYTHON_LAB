import palindrome

str=input("Enter a string : ")
con=palindrome.ispalindrome(str)
if(con==True):
	print(f"{str} is Palindrome")
else:
	print(f"{str} is not palindrome")
longest_sub=palindrome.lp_sub(str)
if longest_sub=="":
	print("There is no paindromic substring")
else:
	print(f"Longest palindromic substring is {longest_sub}")
