while(True):
    print("press q to quit")
    a = input("Enter a Number")
    if a == 'q':
        break
    try:
        a = int(a)
        if a>6:
         print("You entered a number gretter then 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game")

