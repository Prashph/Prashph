import random

def game(you,player1):
    if player1 == you:
        return None
    elif player1 == 's':
        if  you =='w':
            return False
        elif you == 'g':
            return True
    elif player1 == 'w':
        if you =='g':
            return False
        elif you == 's':
             return True
    elif player1 == 'g':
        if you =='s':
            return False
        elif you == 'w':
             return True


print("comp turn: gun(g) water(w) or snake(s)?")

randNo =random.randint(1, 3)

if randNo == 1:
   player1 ="s"
elif randNo == 2:
   player1 ="w"
elif randNo ==3:
   player1 ="g"

you = input("your turn: gun(g) water(w) or snake(s)?")
a =game(player1,you)

print(f"computer chose {player1}")
print(f"you chose {you}")

if a == None:
    print("the game is tie")
elif a:
    print("you win!")
else:
  print("you lose!")

