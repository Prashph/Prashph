# f = open("this.txt","w")
# f.write("this is nice")
# f.close()
# ----------------------------
# with open('another.txt','w') as f:
#     a = f.write("prashant is good boy")
#     print(a)

def game():
     return 665

score = game()
with open("highscore.txt","r") as f:
    highScorestr = f.read()
if highScorestr =='':
    with open("highscore.txt", "w") as f:
        f.write(str(score))  
if int(highScorestr)<score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))
        

