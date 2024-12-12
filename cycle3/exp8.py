upper_limit = int(input("Enter the upper limit : "))
for i in range(1, upper_limit):
        temp = i
        sum = 0
        while temp > 0:
                digit = temp % 10
                temp = temp // 10
                sum = sum + digit
        flag = 0
        if sum <= 1:
                continue
        for j in range(2, sum):
                if sum % j == 0:
                        flag = 1
        if flag == 0:
                print("sum of ", i , " = ",sum)

