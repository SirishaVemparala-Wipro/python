num=int(input("Enter a number: "))

flag=0

for i in range(2,num):

    if num%i==0:

        flag=1

        break

if(num<=1):

    print("Not a prime number")

elif(flag==1):

    print("Not a prime number")

else:

    print("Is a prime number")