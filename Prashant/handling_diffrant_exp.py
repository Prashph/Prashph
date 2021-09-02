try:
    a = int(input("Enter a Number: "))
    c = 1/a
    print(c)

except ValueError as e:
    print("Please enter a valid value")

except ZeroDivisionError as e:
    print("make sure you are not deviding by zero")

print("Thanks for using this code!")
