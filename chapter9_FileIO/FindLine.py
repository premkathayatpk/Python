


with open("log.txt","r") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if "python" in line:
       print(f"python is present in line {lineno}")
       break
    lineno +=1
else:
    print("python is not present.")

