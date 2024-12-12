import math
print ("Enter quadratic equation ax^2 + bx + c  ")
a=float(input("Enter value of a : "))
b=float(input("Enter value of b : "))	
c=float(input("Enter value of c : "))
dsr=(b*b)-(4*a*c)
if(dsr==0):
	print("Possible root value = 1")
	ans=(-b)/(2*a)
	print("X = ",ans)
	
elif(dsr>0):
	print("root values are real")
	sqrtvalue=math.sqrt(dsr)
	ans1=(-b+sqrtvalue)/2*a
	ans2=(-b-sqrtvalue)/2*a
	print("X1 = ",ans1)
	print("X2 = ",ans2)
else:
	print("Complex number")
	sqrtvalue=math.sqrt(abs(dsr))/(2*a)
	print(-b/(2*a),"+i",sqrtvalue)
	print(-b/(2*a),"-i",sqrtvalue)
	
