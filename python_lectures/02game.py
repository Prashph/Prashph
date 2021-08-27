def game():
     return 128

score = game()
with open("another.txt","r") as f:
    highscore = int(f.read())

if highscore<score:
    with open("another.txt", "w") as f:
        f.write(str(score))




