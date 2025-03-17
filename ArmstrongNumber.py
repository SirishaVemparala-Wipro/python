import math

num=int(input("Enter a number: "))

value = [int(d) for d in str(num)]

result = 0

for i in range(0, len(value)):

    result = result + math.pow(value[i], len(value))

if result==num:

    print("Armstrong number")

else:

    print("Not an armstrong number")