for row in range(6):
    for colume in range(7):
        if (row==0 and colume%3!=0) or (row==1 and colume%3==0) or (row-colume==2) or (row+colume==8):
                print("*",end="")
        else:
            print(" ",end="")
    print()

