# TODO


def main():
    counter = 0
    try:
        height= int(input("Height:"))

    except ValueError:
        print("That is not an integer between 0 and 8")
        exit()

    if (height <0 or height >8):
        print("Height must be between 0 and 8")
        exit()

    else:
        for i in range (height):
            counter+=1
            for j in range (height+2+1+i):

                if  j> (height - counter-1) and j <(height) :
                    print("#", end="")
                elif j > (height + 1) and j< (height+2+1+i) :
                    print ("#", end="")
                else:
                    print(" ",end="")
            print()





main()
