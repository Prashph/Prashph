import random
import math

randNumber = random.randint(1, 100)
userGuess = None

guesses = 0

print('''***Rules of the game***\n1.if player guess less than one or gretter than 100,say "OUT OF THE BOND"
2.on a player's first turn, there guess is\n*within 10 of the number,return "WORM!"
*further than a 10 awayfrom the number return,"COLD!"\n
1.On all sub sequent turns,if the guess is 
*closer to the number then then previous guess return "WORMER!"\n*further from the guess ,return "COLDER!" ''')

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    guess = []
    guess.append(userGuess)
    if(userGuess<0 or userGuess>100):
        print("OUT OF THE BOUNDS")
    elif(userGuess==randNumber):
        print("You guessed it right!")
    elif((abs(randNumber-userGuess))>10):
        print("You guessed it wrong! your responce is: COLD!")
    elif(abs(randNumber-userGuess))<10:
        print("You guessed it wrong! your responce is: WORM!")
    while True:
        if(((randNumber-userGuess[-2])<(randNumber-userGuess[-1]))):
            print("You guessed it wrong! your responce is: WORMER!")
        else:
            print("You guessed it wrong! your responce is: COLDER!")

print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
        



