#! /user/bin/env python3
#Depreciation Calculator by kBowen

import locale
from Asset import Asset


def getDep():
    runner = 1
    while (runner !=0):
        try:
            cost = getValue("Asset Cost: ","f")
            salval = getValue("Salvage Value: ", "f")
            life = getValue("Life (years): ", "i")
            asset = Asset(cost, salval, life)
            if(asset.isValid()):
                print("Straight Line annual depreciation is: %s " %locale.currency(asset.getStraight(), grouping=True))
                print()
                dDep = question("Would you like to see the Double Declining Schedule? (Y/N): ")
                if (dDep==1):
                    print(" Year     Beg.Value   Depreciation     End.Value")
                    for i in range(1,asset.getLife()+1):
                        print("{:4}".format(i)
                        + "{:15,.2f} {:12,.2f} {:15,.2f}".format(asset.getBegBal(i), asset.getAnDep(i), asset.getEndBal(i)))
                        print()
            else:
                print("Calculator Error: " + asset.getError())
        except ValueError as e:
            print("Data Error: " + str(e))
            
        runner = question("Do you have another asset? (Y/N): ")
        
        

def getValue(prompt, vType):
    valid = False
    while not valid:
        try:
            if vType.lower() =="i":
                amt = int(input(prompt))
                valid = True
            elif vType.lower() =="f":
                amt = float(input(prompt))
                valid = True    
            else:
                print("Illegal Input: Try again")
                valid = False
        except ValueError as ex:
            print("Illegal value: " + str(ex))
            valid = False
            
    return amt
            
def question(prompt):
    functional = False
    func = -1
    while not functional:
        try:
            response = input(prompt)
            if len(response) >0 and response[0].upper()=="Y":
                func = 1
                functional = True
            elif len(response) <=0:
                print("Unknown choice.  Please try again")
                functional = False
            elif response[0].upper() == "N":
                func = 0
                functional = True
            else: 
                print("Unknown choice.  Please try again")
                func = -1
                functional = False
        except ValueError as e:
            print("Question Error: " + str(e))
            
    return func

def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')
    print("Welcome to the Depreciation Calculator")
    choice = question("Do you have an asset? (Y/N): ")
    if (choice==1):
        getDep()
    print()
    print("Thank you for using the Depreciation Calculator")

if __name__ == "__main__":
    main()
