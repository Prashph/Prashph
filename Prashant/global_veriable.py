a = 54   #Global veriable
def fun1():
    global a
    print(f"print statement 1 :{a}")
    a = 7  #Local veriable global veriable is not used
    print(f"print statement 2 :{a}")

fun1()
print(f"print statement 3 :{a}")


