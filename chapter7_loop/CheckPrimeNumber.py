num =int(input("Enter a number: "))

if(num<=1):
    print("Not prime number.")

for i in range(2,num):
    if((num%i)==0):
        print(f"{num} is not prime number")
        break

else:
    print("prime")