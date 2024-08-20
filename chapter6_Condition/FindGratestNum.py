print("Enter 4 numbers: ")
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())

if(n1>n2 and n1>n3 and n1>n4):
    print(f"{n1}is grater")
elif(n2>n1 and n2>n3 and n2>n4):
    print(f"{n2}is grater")
elif(n3>n1 and n3>n2 and n3>n4):
    print(f"{n3}is grater")
else:
     print(f"{n4} is grater")