import random

def Roll_Dice():
    ### randint(start,stop) is from start to stop (including)
    side = random.randint(1,6)
    print("You've got a " + str(side))

### keep_on should be a boolean
keep_on = True
while(keep_on):

    Roll_Dice()
    ### how to make the cursor on the next line???
    answer =raw_input("Do you want to try again? (Y or N)")
    if answer=="Y" or answer == "y":
        continue
    elif answer == "N" or answer =="n":
        keep_on = False
    else:
        print("You entered a wrong answer, enter again")
