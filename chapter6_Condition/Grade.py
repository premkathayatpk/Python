m=float(input("Enter your marks: "))

if(m>90 and m<=100):
    print("Your Grade is Ex")

elif(m>80 and m<=90):
    print("Your Grand is A")

elif(m>70 and m<=80):
    print("Your Grand is B")

elif(m>60 and m<=70):
    print("Your Grand is C")

elif(m>=50 and m<=60):
    print("Your Grand is D")

elif(m>=0 and m<50):
    print("Your Grand is F")

else:
    print("Invalid marks(0-100)")