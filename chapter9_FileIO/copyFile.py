
with open("log.txt","r") as f:
    content=f.read()

with open("copyFile.txt","w") as f:
    f.write(content)