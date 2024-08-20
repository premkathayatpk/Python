names=["prem","hari","sita","gita","ram"]
name=input("Enter your name: ")
if(name in names):
    print(f"{name} is present in list.")

else:
    print(f"{name} is not present in list.")