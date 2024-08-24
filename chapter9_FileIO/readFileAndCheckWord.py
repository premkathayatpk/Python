with open("poems.txt","r") as f:
    content=f.read()
    print(content)

if("twinkle" in content):
    print("\nThe word 'twinkle' is present in Poems")

else:
    print("\nThe word 'twinkle' is not present in Poems")
