word="Donkey"

with open("replaceWord.txt","r") as f:
    content=f.read()

contentNew =content.replace(word,"######")

with open("replaceWord.txt","w") as f:
    f.write(contentNew)