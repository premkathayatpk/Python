math=float(input("Enter marks of Math: "))
science=float(input("Enter marks of science: "))
english=float(input("Enter marks of English: "))

per=float(math+science+english)/3

if(per>=40):
    if(math>=33):
        print("Pass")

    elif(science>=33):
        print("Pass")
    
    elif(english>=33):
        print("Pass")

    else:
        print("Fail")

else:
    print("Fail")
