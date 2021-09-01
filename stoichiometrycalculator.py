from Dataset.dataset import elementdict
from StartingValues.startingvalues import ValOfStart, NumOfElmntsStart, NumOfElmntsEnd, MolRatioNum, MolRatioDenom, PrintData
from ConfirmationQuestions.isthisokayyes import IsThisOkayYes
from ConfirmationQuestions.isthisokayno import IsThisOkayNo
from ChangeItems.changeanythingelse import ChangeAnythingElse

print("Stoichiometry Calculator Stable Production Release V1.0.1")
print("Built by Paul D.")
print("Copyright © 2021. All rights reserved.\n")

print("Please leave all feedback at the following email address: pvdorman764@gmail.com\n")

print("If you don't know what stoichiometry is, please consult the following Wiki article: https://en.wikipedia.org/wiki/Stoichiometry\n")

while True:
    try:
        ValOfStart()
        NumOfElmntsStart()
        NumOfElmntsEnd()
        MolRatioNum()
        MolRatioDenom()
        PrintData()
        while True:
            try:
                IsThisOkay = input("Is this okay? (Y/N)")
                if IsThisOkay=='Y' or IsThisOkay=='y':
                    IsThisOkayYes()
                elif IsThisOkay=='N' or IsThisOkay=='n':
                    while True:
                        try:
                            IsThisOkayNo()
                            try:
                                ChangeAnythingElse()
                                if ChangeAnythingElse=='Y' or ChangeAnythingElse=='y':
                                    pass
                                elif ChangeAnythingElse=='N' or ChangeAnythingElse=='n':
                                    break
                                else:
                                    print("Oops! An error occured. Returning...")
                            except:
                                print("Oops! An error occured. Returning...")
                        except:
                            print("Oops! An error occured. Returning...")
                else:
                    print("Oops! An error occured. Returning...")
                    continue
                break
            except:
                print("Oops! An error occured. Returning...")
                continue
    except:
        print("Oops! An error occured. Returning...")
    while True:
        ContinueCalculation = input("Would you like to continue calculating stoichiometry? (Y/N)")
        if ContinueCalculation=='Y' or ContinueCalculation=='y':
            break
        elif ContinueCalculation=='N' or ContinueCalculation=='n':
            break
        else:
            print("Oops! An error occured. Returning...")
            continue
    if ContinueCalculation=='Y' or ContinueCalculation=='y':
        pass
    elif ContinueCalculation=='N' or ContinueCalculation=='n':
        quit()
    else:
        print("Oops! An error occured. Returning...")
        continue