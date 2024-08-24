import random
def game():
    print("You are playing a game...")
    score= random.randint(1,100)
    print(f"Your score: {score}")
    #featch the hiscore
    with open("HiScore.txt","r") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    if(score>hiscore):
        #write the hiscore
        print(f"You got high score: {score}")
        with open("HiScore.txt","w") as f:
            f=f.write(str(score))
    return score

game()

