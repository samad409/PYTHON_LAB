def ispalindrome(a):
	b=a[::-1]
	c=True
	d=False
	if b==a:
		return c
	else:
		return d

def lp_sub(s): 
	longest = ""
	for i in range(len(s)):
		for j in range(i + 1, len(s) + 1):
			substring = s[i:j]
			if ispalindrome(substring) and len(substring) > len(longest):
				longest = substring
	return longest
