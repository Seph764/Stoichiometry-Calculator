from Dataset.dataset import elementdict
from StartingValues.startingvalues import *
from ChangeItems.changestartingvalue import ChangeStartingValue
from ChangeItems.changemoleratio import ChangeMoleRatio
from ChangeItems.changelabel import ChangeLabel

def IsThisOkayNo():
    while True:
        try:
            WhatToChange = input("What would you like to change? (Starting Value/Mole Ratio/Label)")
            if WhatToChange=='Starting Value' or WhatToChange=='starting value':
                ChangeStartingValue()
            elif WhatToChange=='Mole Ratio' or WhatToChange=='mole ratio':
                ChangeMoleRatio()
            elif WhatToChange=='Label' or WhatToChange=='label':
                ChangeLabel()
            else:
                print("Oops! An error occured. Returning...")
                continue
            break
        except:
            print("Oops! An error occured. Returning...")
            continue