word="python"

with open("log.txt","r") as f:
    words=f.read()

    if word in words:
        print("python is contain")

    else:
        print("python is not contain")