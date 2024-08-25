
with open("log.txt","r") as f:
    f1=f.read()

with open("copyFile.txt","r") as f:
    f2=f.read()

if(f1==f2):
    print("Both file content are match")

else:
    print("This files content are not match")
