def ChangeAnythingElse():
    while True:
        try:
            ChangeAnythingElse = input("Would you like to change anything else? (Y/N)")
            if ChangeAnythingElse=='Y' or ChangeAnythingElse=='y':
                break
            elif ChangeAnythingElse=='N' or ChangeAnythingElse=='n':
                break
            else:
                print("Oops! An error occured. Returning...")
                continue
        except:
            print("Oops! An error occured. Returning...")
            continue