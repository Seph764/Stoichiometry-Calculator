from Dataset.dataset import elementdict
from StartingValues.startingvalues import *

def IsThisOkayYes():
    while True:
        try:
            StartingIn = input("Is the starting label in mass or moles? (Mass/Moles)")
            if StartingIn=='Mass' or StartingIn=='mass':
                while True:
                    try:
                        EndingIn = input("Is the ending label in mass or moles? (Mass/Moles)")
                        if EndingIn=='Mass' or EndingIn=='mass':
                            Result = ValOfStart.ValueOfStart / sum(StartingAtomicMassList) * MolRatio.MoleRatio * sum(EndingAtomicMassList)
                            seperator = ""
                            print("The total is " + str(Result) + " grams of " + seperator.join(EndingElementList) + ".")
                            break
                        elif EndingIn=='Moles' or EndingIn=='moles':
                            Result = ValOfStart.ValueOfStart / sum(StartingAtomicMassList) * MolRatio.MoleRatio
                            seperator = ""
                            print("The total is " + str(Result) + " moles of " + seperator.join(EndingElementList) + ".")
                            break
                        else:
                            print("Oops! An error occured. Returning...")
                            continue
                    except:
                        print("Oops! An error occured. Returning...")
                        continue
            elif StartingIn=='Moles' or StartingIn=='moles':
                while True:
                    try:
                        EndingIn = input("Is the ending label in mass or moles? (Mass/Moles)")
                        if EndingIn=='Mass' or EndingIn=='mass':
                            Result = ValOfStart.ValueOfStart * MolRatio.MoleRatio * sum(EndingAtomicMassList)
                            seperator = ""
                            print("The total is " + str(Result) + " moles of " + seperator.join(EndingElementList) + ".")
                            break
                        elif EndingIn=='Moles' or EndingIn=='moles':
                            Result = ValOfStart.ValueOfStart * MolRatio.MoleRatio
                            seperator = ""
                            print("The total is " + str(Result) + " moles of " + seperator.join(EndingElementList) + ".")
                            break
                        else:
                            print("Oops! An error occured. Returning...")
                            continue
                    except:
                        print("Oops! An error occured. Returning...")
                        continue
            else:
                print("Oops! An error occured. Returning...")
                continue
            break
        except:
            print("Oops! An error occured. Returning...")
            continue