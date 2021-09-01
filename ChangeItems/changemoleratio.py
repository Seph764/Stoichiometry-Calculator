from StartingValues.startingvalues import *

def ChangeMoleRatio():
    while True:
        try:
            WhatToChange = input("What would you like to change about the current mole ratio? (Numerator/Denominator)")
            if WhatToChange=='Numerator' or WhatToChange=='numerator':
                while True:
                    try:
                        MolRatioNum.MoleRatioNumerator = float(input("Please enter the new mole ratio numerator:"))
                        print("New mole ratio numerator saved.")
                        print("New mole ratio: " + str(MolRatio()))
                        while True:
                            try:
                                ChangeStartingNumerator = input("Would you still like to change the starting numerator? (Y/N)")
                                if ChangeStartingNumerator=='Y' or ChangeStartingNumerator=='y':
                                    break
                                elif ChangeStartingNumerator=='N' or ChangeStartingNumerator=='n':
                                    break
                                else:
                                    print("Oops! An error occured. Returning...")
                                    continue
                            except:
                                print("Oops! An error occured. Returning...")
                                continue
                        if ChangeStartingNumerator=='Y' or ChangeStartingNumerator=='y':
                            pass
                        elif ChangeStartingNumerator=='N' or ChangeStartingNumerator=='n':
                            break
                        else:
                            print("Oops! An error occured. Returning...")
                            continue
                    except:
                        print("Oops! An error occured. Returning...")
                        continue
            elif WhatToChange=='Denominator' or WhatToChange=='denominator':
                while True:
                    try:
                        MolRatioDenom.MoleRatioDenominator = float(input("Please enter the new mole ratio denominator:"))
                        print("New mole ratio denominator saved.")
                        print("New mole ratio: " + str(MolRatio()))
                        while True:
                            try:
                                ChangeStartingDenominator = input("Would you still like to change the starting denominator?")
                                if ChangeStartingDenominator=='Y' or ChangeStartingDenominator=='y':
                                    break
                                elif ChangeStartingDenominator=='N' or ChangeStartingDenominator=='n':
                                    break
                                else:
                                    print("Oops! An error occured. Returning...")
                                    continue
                            except:
                                print("Oops! An error occured. Returning...")
                                continue
                        if ChangeStartingDenominator=='Y' or ChangeStartingDenominator=='y':
                            pass
                        elif ChangeStartingDenominator=='N' or ChangeStartingDenominator=='n':
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
            try:
                while True:
                    ChangeAnythingElse = input("Would you like to change anything else about the mole ratio?")
                    if ChangeAnythingElse=='Y' or ChangeAnythingElse=='y':
                        break
                    elif ChangeAnythingElse=='N' or ChangeAnythingElse=='n':
                        break
                    else:
                        print("Oops! An error occured. Returning...")
                        continue
                if ChangeAnythingElse=='Y' or ChangeAnythingElse=='y':
                    pass
                elif ChangeAnythingElse=='N' or ChangeAnythingElse=='n':
                    break
                else:
                    print("Oops! An error occured. Returning...")
                    continue
            except:
                print("Oops! An error occured. Returning...")
                continue
        except:
            print("Oops! An error occured. Returning...")
            continue