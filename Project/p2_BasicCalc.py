n1=float(input("Enter 1st number: "))
operator=input("Enter an operator(+, -, *, / ): ")
n2=float(input("Enter 2nd number: "))

result=0
if(operator=="+"):
    reselt=n1+n2
elif(operator=="-"):
    result=n1-n2
elif(operator=="*"):
    result=n1*n2
elif(operator=="/"):
    result=n1/n2
else:
    print("Invalid input")


print(f"{n1} {operator} {n2} = {result}")