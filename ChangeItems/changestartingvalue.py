from StartingValues.startingvalues import *

def ChangeStartingValue():
    while True:
        try:
            ValueOfStart = float(input("Please enter the new starting value:"))
            print("New starting value saved.")
            ChangeStartingValue = input("Would you still like to change the starting value? (Y/N)")
            if ChangeStartingValue=='Y' or ChangeStartingValue=='y':
                pass
            elif ChangeStartingValue=='N' or ChangeStartingValue=='n':
                break
            else:
                print("Oops! An error occured. Returning...")
                continue
        except:
            print("Oops! An error occured. Returning...")
            continue