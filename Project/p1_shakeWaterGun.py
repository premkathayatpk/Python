import random
'''
1 for snake
-1 for water 
0 for gun
'''
computer=random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
you = youDict[youstr]
reverseDict={1:"snake",-1:"water",0:"gun"}

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("It's a Draw")

else:
    if(computer==-1 and you==1):
        print("You win!")

    elif(computer==-1 and you==0):
        print("You lose!")

    elif(computer==1 and you==-1):
        print("You lose!")

    elif(computer==1 and you==0):
        print("You win!")

    elif(computer==0 and you==-1):
        print("You win!")

    elif(computer==0 and you==1):
        print("You lose!")

    else:
        print("Something rong")