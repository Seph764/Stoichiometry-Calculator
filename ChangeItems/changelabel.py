from Dataset.dataset import elementdict
from StartingValues.startingvalues import *

def ChangeLabel():
    while True:
        try:
            WhatToChange = input("What would you like to change about the current label? (Starting/Ending)")
            if WhatToChange=='Starting' or WhatToChange=='starting':
                while True:
                    try:
                        StartingLabelAddOrDelete = input("How would you like to change it? (Add/Remove)")
                        if StartingLabelAddOrDelete=='Add' or StartingLabelAddOrDelete=='add':
                            while True:
                                try:
                                    HowManyToAdd = int(input("How many elements would you like to add?"))
                                    for i in range(0, HowManyToAdd):
                                        elmnt = input("Enter Element #{}:".format(i+1))
                                        atomicmass = elementdict.get("{}".format(elmnt))
                                        StartingElementList.append(elmnt)
                                        StartingAtomicMassList.append(atomicmass)
                                        print(elmnt + " has been added.")
                                    print("Here is the new list: " + str(StartingElementList))
                                    while True:
                                        try:
                                            AddAnyMore = input("Would you like to add any more elements? (Y/N)")
                                            if AddAnyMore=='Y' or AddAnyMore=='y':
                                                break
                                            elif AddAnyMore=='N' or AddAnyMore=='n':
                                                break
                                            else:
                                                print("Oops! An error occured. Returning...")
                                                continue
                                        except:
                                            print("Oops! An error occured. Returning...")
                                            continue
                                    while True:
                                        if AddAnyMore=='Y' or AddAnyMore=='y':
                                            break
                                        elif AddAnyMore=='N' or AddAnyMore=='n':
                                            break
                                        else:
                                            print("Oops! An error occured. Returning...")
                                            continue
                                    if AddAnyMore=='Y' or AddAnyMore=='y':
                                        pass
                                    elif AddAnyMore=='N' or AddAnyMore=='n':
                                        break
                                    else:
                                        print("Oops! An error occured. Returning...")
                                        continue
                                except:
                                    print("Oops! An error occured. Returning...")
                                    continue
                            break
                        elif StartingLabelAddOrDelete=='Remove' or StartingLabelAddOrDelete=='remove':
                            while True:
                                try:
                                    HowManyToRemove = int(input("How many inputs would you like to remove?"))
                                    for i in range(0, HowManyToRemove):
                                        print(StartingElementList)
                                        elmntdel = int(input("Which number entry would you like to remove?"))
                                        del StartingElementList[elmntdel - 1]
                                        del StartingAtomicMassList[elmntdel - 1]
                                        print("Entry has been removed.")
                                    print("Here is the new list: " + str(EndingElementList))
                                    while True:
                                        try:
                                            RemoveAnyMore = input("Would you like to remove any more elements? (Y/N)")
                                            if RemoveAnyMore=='Y' or RemoveAnyMore=='y':
                                                break
                                            elif RemoveAnyMore=='N' or RemoveAnyMore=='n':
                                                break
                                            else:
                                                print("Oops! An error occured. Returning...")
                                                continue
                                        except:
                                            print("Oops! An error occured. Returning...")
                                            continue
                                    while True:
                                        if RemoveAnyMore=='Y' or RemoveAnyMore=='y':
                                            break
                                        elif RemoveAnyMore=='N' or RemoveAnyMore=='n':
                                            break
                                        else:
                                            print("Oops! An error occured. Returning...")
                                            continue
                                    if RemoveAnyMore=='Y' or RemoveAnyMore=='y':
                                        pass
                                    elif RemoveAnyMore=='N' or RemoveAnyMore=='n':
                                        break
                                    else:
                                        print("Oops! An error occured. Returning...")
                                        continue
                                except:
                                    print("Oops! An error occured. Returning...")
                                    continue
                            break
                        else:
                            print("Oops! An error occured. Returning...")
                            continue
                    except:
                        print("Oops! An error occured. Returning...")
                        continue
            elif WhatToChange=='Ending' or WhatToChange=='ending':
                while True:
                    try:
                        EndingLabelAddOrDelete = input("How would you like to change it? (Add/Remove)")
                        if EndingLabelAddOrDelete=='Add' or EndingLabelAddOrDelete=='add':
                            while True:
                                HowManyToAdd = int(input("How many elements would you like to add?"))
                                for i in range(0, HowManyToAdd):
                                    elmnt = input("Enter Element #{}:".format(i+1))
                                    atomicmass = elementdict.get("{}".format(elmnt))
                                    EndingElementList.append(elmnt)
                                    EndingAtomicMassList.append(atomicmass)
                                    print(elmnt + " has been added.")
                                print("Here is the new list: " + str(EndingElementList))
                                while True:
                                    AddAnyMore = input("Would you like to add any more elements? (Y/N)")
                                    if AddAnyMore=='Y' or AddAnyMore=='y':
                                        break
                                    elif AddAnyMore=='N' or AddAnyMore=='n':
                                        break
                                    else:
                                        print("Oops! An error occured. Returning...")
                                        continue
                                if AddAnyMore=='Y' or AddAnyMore=='y':
                                    pass
                                elif AddAnyMore=='N' or AddAnyMore=='n':
                                    break
                                else:
                                    print("Oops! An error occured. Returning...")
                                    continue
                            break
                        elif EndingLabelAddOrDelete=='Remove' or EndingLabelAddOrDelete=='remove':
                            while True:
                                HowManyToRemove = int(input("How many inputs would you like to remove?"))
                                for i in range(0, HowManyToRemove):
                                    print(EndingElementList)
                                    elmntdel = int(input("Which number in the entry order would you like to remove?"))
                                    del EndingElementList[elmntdel - 1]
                                    del EndingAtomicMassList[elmntdel - 1]
                                    print("Entry has been removed.")
                                while True:
                                    RemoveAnyMore = input("Would you like to remove any more elements? (Y/N)")
                                    if RemoveAnyMore=='Y' or RemoveAnyMore=='y':
                                        break
                                    elif RemoveAnyMore=='N' or RemoveAnyMore=='n':
                                        break
                                    else:
                                        print("Oops! An error occured. Returning...")
                                        continue
                                if RemoveAnyMore=='Y' or RemoveAnyMore=='y':
                                    pass
                                elif RemoveAnyMore=='N' or RemoveAnyMore=='n':
                                    break
                                else:
                                    print("Oops! An error occured. Returning...")
                                    continue
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
                    ChangeAnythingElse = input("Would you like to change anything else about the label?")
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