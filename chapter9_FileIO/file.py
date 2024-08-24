import os

#create file
if os.path.exists("myfile.txt"):
    print("Alread exit")
else:
    f=open("myfile.txt","x") 

#open and write the filein file
f = open("myfile.txt", "w") #f=open("myfile.txt","a")  #for appending
f.write("I am prem")
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())

#f = open("java.jpg", "rb")   #for read bianry mode(image)
print(f.read())

#delete file
if os.path.exists("file1.txt"):
    os.remove("file1.txt") 
else:
    print("The file doesnot exit")