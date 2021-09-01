from Dataset.dataset import elementdict

StartingElementList = []
StartingAtomicMassList = []
EndingElementList = []
EndingAtomicMassList = []

def ValOfStart():
    while True:
        try:
            ValOfStart.ValueOfStart = float(input("What is the starting value?"))
            break
        except:
            print("Oops! An error occured. Returning...")

def NumOfElmntsStart():
    while True:
        try:
            i = 0
            NumOfElmntsStart.NumberOfElementsStart = int(input("How many elements form the starting label?"))
            while i < NumOfElmntsStart.NumberOfElementsStart:
                try:
                    elmnt = input("Enter Element #{}:".format(i + 1))
                    if elmnt in elementdict:
                        atomicmass = elementdict.get("{}".format(elmnt))
                        StartingElementList.append(elmnt)
                        StartingAtomicMassList.append(atomicmass)
                        print(elmnt + " has been added.")
                        i += 1
                    else:
                        print("Oops! An error occured. Returning...")
                        continue
                except:
                    print("Oops! An error occured. Returning...")
                    continue
        except:
            print("Oops! An error occured. Returning...")
            continue
        break

def NumOfElmntsEnd():
    while True:
        try:
            i = 0
            NumOfElmntsEnd.NumberOfElementsEnd = int(input("How many elements form the ending label?"))
            while i < NumOfElmntsEnd.NumberOfElementsEnd:
                try:
                    elmnt = input("Enter Element #{}:".format(i + 1))
                    if elmnt in elementdict:
                        atomicmass = elementdict.get("{}".format(elmnt))
                        EndingElementList.append(elmnt)
                        EndingAtomicMassList.append(atomicmass)
                        print(elmnt + " has been added.")
                        i += 1
                    else:
                        print("Oops! An error occured. Returning...")
                        continue
                except:
                    print("Oops! An error occured. Returning...")
                    continue
        except:
            print("Oops! An error occured. Returning...")
            continue
        break

def MolRatioNum():
    while True:
        try:
            MolRatioNum.MoleRatioNumerator = float(input("What is the numerator of the mole ratio?"))
            print("Mole ratio numerator added.")
            break
        except:
            print("Oops! An error occured. Returning...")
            continue

def MolRatioDenom():
    while True:
        try:
            MolRatioDenom.MoleRatioDenominator = float(input("What is the denominator of the mole ratio?"))
            print("Mole ratio denominator added.")
            break
        except:
            print("Oops! An error occured. Returning...")
            continue

def MolRatio():
    MolRatio.MoleRatio = float(MolRatioNum.MoleRatioNumerator) / float(MolRatioDenom.MoleRatioDenominator)
    return MolRatio.MoleRatio

def PrintData():
    print("Starting value entered: " + str(ValOfStart.ValueOfStart))
    print("List of elements added to the beginning label's list: " + str(StartingElementList))
    print("List of elements added to the ending label's list: " + str(EndingElementList))
    print("Mole ratio numerator entered: " + str(MolRatioNum.MoleRatioNumerator))
    print("Mole ratio denominator entered: " + str(MolRatioDenom.MoleRatioDenominator))
    print("Resulting mole ratio entered: " + str(MolRatio()))