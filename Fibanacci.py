import sys
import re

def FibanacciCalc(n):
    calculationlist = [0, 1, 1]
    for i in range(3,n):
        sum = calculationlist[i-2] + calculationlist[i-1]
        calculationlist.append(sum)
    return calculationlist


if __name__ == "__main__":
    argumentlist = sys.argv
    if len(argumentlist) == 1:
        print("no arguments")
    elif len(argumentlist) == 2:
        if re.fullmatch(r"\d+", argumentlist[1]) == None:
            print("positive integer needed")
        else:
            print(FibanacciCalc(int(argumentlist[1])))

    else:
        print("too many arguments")

        
