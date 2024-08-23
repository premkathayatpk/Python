def rem(l,word):
    for item in l:
        l.remove(word)
        return l



l=["Hari","Ram","Prem","Sita"]
word =input("Enter a word do you want to delete: ") 
print(rem(l,word))   