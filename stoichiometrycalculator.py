from Dataset.dataset import elementdict
from StartingValues.startingvalues import *
from ConfirmationQuestions.isthisokayyes import *
from ConfirmationQuestions.isthisokayno import *
from ChangeItems.changeanythingelse import *

print("Stoichiometry Calculator Beta Release v0.2.0")
print("Originally built and licensed by Paul D.")
print("This software is licensed under the GNU General Public License, Version 3.0.\n")

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
            StartingElementList.clear()
            StartingAtomicMassList.clear()
            EndingElementList.clear()
            EndingAtomicMassList.clear()
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