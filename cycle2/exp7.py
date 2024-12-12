list1=input("Enter colors for list 1 seperated by comma : ")
list2=input("Enter colors for list 2 seperate by comma : ")
set1=set(list1.split(','))
set2=set(list2.split(','))
diff=set1-set2
print("Difference of Set 1 and set 2 is ",diff)

