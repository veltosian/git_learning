#!/usr/bin/python3

from random import randint

def getRoll():
    print("\nLet's roll!")
    roll = randint(0,1)
    if roll == 0 and randint(0,1):
        roll = -1
        print("Number is... 00")
    else:
        print("Number is... {}".format(roll))
    return roll

class Wager():
    def __init__(self):
        self.betType = 0
        self.betNum = 0
        self.betColor = "black"
        self.betOddEven = "odd"
        self.doubleZero = -1
#        self.colorTable = {}

        

    def getBet(self):
        while True:
            try:
                usrInput = int(input("1: Single Number, 2: Red or Black, 3: Odd or Even "))
                if usrInput < 1 or usrInput > 3:
                    continue
                else:
                    break
            except ValueError:
                print("Looks like you didn't enter a number holmes")
                print("Try again...")
        self.betType = usrInput

        if self.betType == 1:
            self.getBetNum()
        elif self.betType == 2:
            self.getBetColor()
        else:
            self.getBetOddEven()


    def getBetColor(self):
        while True:
            try:
                self.betColor = input("Which color would you like to bet on? ")
                if self.betColor not in ["red", "black", "Red", "Black", "RED", "BLACK"]:
                    print("That is an invalid color. Try again...")
                    continue
                else:
                    if self.betColor in ["red", "Red", "RED"]:
                        self.betColor = "red"
                    else:
                        self.betColor = "black"
                    break
            except ValueError:
                print("Invalid input. Try again...")

    def getBetNum(self):
        while True:
            try:
                self.betNum = input("Which number would you like to bet on? ")
                if self.betNum == "00":
                    self.betNum = self.doubleZero
                    break
                elif int(self.betNum) < 0 or int(self.betNum) > 29 : 
                    print("That number is out of range. Try again...")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input. Try again...")

    def getBetOddEven(self):

        while True:
            try:
                self.betOddEven = input("Would you like to bet on odd or even? ")
                if self.betOddEven not in ["odd", "even", "Odd", "Even", "ODD", "EVEN"]:
                    print("Sorry that is neither 'odd' nor 'even'. Try again...")
                else:
                    if self.betOddEven in ["odd", "Odd", "ODD"]:
                        self.betOddEven = "odd"
                    else:
                        self.betOddEven = "even"
                    break
            except ValueError:
                print("Invalid input. Try again...")


#    def setBetVars(self):
#        if betType == 2:
#            self.betColor = 


print("Welcome to roulette!")
print("What kind of bet would you like to place?")
#usrBet = input("(1: Single Number, 2: Red or Black, 3: Odd or Even)")
wager = Wager()
wager.getBet()



roll = getRoll()


#Testing






#Notes Zach: 
# Check bank balance and pay credit card
# Check when pigout at the park is
# Check when we stay at the davenport
