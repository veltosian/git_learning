#!/usr/bin/python3

from random import randint

def getRoll():
    print("\nLet's roll!")
    roll = randint(-1,36)
    if roll == 0 and randint(0,1):
        roll = -1
        print("Number is... 00")
    else:
        print("Number is... {}".format(roll))
    return roll

class Wager():
    def __init__(self):
        self.bankRoll = 100
        self.betType = 0
        self.betNum = 0
        self.betColor = "black"
        self.betOddEven = "odd"
        self.doubleZero = -1
        self.colorTable = {-1: "green",
                           0: "green",
                           1: "red",
                           2: "black",
                           3: "red",
                           4: "black",
                           5: "red",
                           6: "black",
                           7: "red",
                           8: "black",
                           9: "red",
                           10: "black",
                           11: "black",
                           12: "red",
                           13: "black",
                           14: "red",
                           15: "black",
                           16: "red",
                           17: "black",
                           18: "red",
                           19: "red",
                           20: "black",
                           21: "red",
                           22: "black",
                           23: "red",
                           24: "black",
                           25: "red",
                           26: "black",
                           27: "red",
                           28: "black",
                           29: "black",
                           30: "red",
                           31: "black",
                           32: "red",
                           33: "black",
                           34: "red",
                           35: "black",
                           36: "red" }

    def getBet(self):
        # Get the bet type
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

        # Get the bet amount
        while True:
            try: #TODO Add check that disallows betting more than user has
                self.betAmt = input("How much would you like to bet? (Default 1) ")
                if self.betAmt == "":
                    self.betAmt = 1
                else:
                    self.betAmt = int(self.betAmt)
                self.bankRoll -= self.betAmt
                break
            except ValueError:
                print("Invalid input. Try again...")

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
                elif int(self.betNum) < 0 or int(self.betNum) > 36 : 
                    print("That number is out of range. Try again...")
                    continue
                else:
                    self.betNum =int(self.betNum)
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


    def checkBet(self, roll):
        if self.betType == 1:
            if self.betNum == int(roll):
                return True
            else:
                return False
        elif self.betType == 2:
            if self.betType == 2:
                if self.betColor == self.colorTable[roll]:
                    return True
                else:
                    return False
        else:
            if self.betOddEven == "even" and roll % 2 == 0:
                return True
            elif self.betOddEven == "odd" and roll % 2 == 1:
                return True
            else: 
                return False
                

    def updateBankRoll(self, roll):
        if self.checkBet(roll):
            if self.betType == 1:
                self.bankRoll += self.betAmt * 35
            else: #color and odd/Even pay the same odds so blanket else
                self.bankRoll += self.betAmt * 2


print("Welcome to roulette!")
wager = Wager()
while True:
    print("What kind of bet would you like to place?")

    wager.getBet()

    roll = getRoll()



    if wager.checkBet(roll):
        print("Congratulations you've won the bet!")
    else:
        print("Sorry, it appears that you've lost")

    wager.updateBankRoll(roll)

    print("Your bank roll is now: {}\n".format(wager.bankRoll))

#TODO:
# Add functionality for multiple bets
# Add functionality for multiple single number bets
# Add 3 text-based boxes with cursor icon in them that selects bet when user hits enter
#  - Create board of 3 boxes
#  - Add this functionality to a separate file and import it here
# Create text-based graphics with a gameboard that the user can move a cursor through
