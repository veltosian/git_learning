#!/usr/bin/python3

import getch

class RouletteBoard():
    def __init__(self):
        self.board = []
        self.tempBoard = []
        self.token = []
        self.board = self.getAsset("Asset:gameboard")
        self.setupElements()
        self.setupNavDict()
        self.location = [0,0]
        self.getch = getch._Getch()

    def setupElements(self):
        '''
        Create dictionary of each element with indexes
        Generate indexes of the 3 rows of numbers with math
        Index includes: [start row, start column, width]
        '''
        self.betElements = {}
        
        row = [(x+1)*3 for x in range(12)]
        for i in range(len(row)):
            self.betElements[row[i]] = [1,4+3*i,2]

        row = [(x+1)*3-1 for x in range(12)]
        for i in range(len(row)):
            self.betElements[row[i]] = [3,4+3*i,2]

        row = [(x+1)*3-2 for x in range(12)]
        for i in range(len(row)):
            self.betElements[row[i]] = [5,4+3*i,2]

        self.betElements[-1] = [2,1,2]
        self.betElements[0] = [6,1,2]
        self.betElements["2to1[0]"] = [1,41,4]
        self.betElements["2to1[1]"] = [3,41,4]
        self.betElements["2to1[2]"] = [5,41,4]
        self.betElements["1st.12"]  = [7,6,6]
        self.betElements["2nd.12"]  = [7,18,6]
        self.betElements["3rd.12"]  = [7,31,6]
        self.betElements["1to18"]   = [9,4,5]
        self.betElements["EVEN"]    = [9,10,4]
        self.betElements["RED"]     = [9,16,3]
        self.betElements["BLACK"]   = [9,22,5]
        self.betElements["ODD"]     = [9,29,3]
        self.betElements["19to36"]  = [9,34,6]

    def setupNavDict(self):
        self.navDict = {0 :[-1,3,6,9,12,15,18,21,24,27,30,33,36,"2to1[0]"],
                        1 :[-1,2,5,8,11,14,17,20,23,26,29,32,35,"2to1[1]"],
                        2 :[0,1,4,7,10,13,16,19,22,25,28,31,34,"2to1[2]"],
                        3 :["1st.12", "2nd.12", "3rd.12"],
                        4 :["1to18","EVEN","RED", "BLACK", "ODD", "19to36"]
        }
        
    def replace(self,element):
        #board = self.board[:]
        #Make a copy of self.board
        board = copy(self.board)
        idx = self.betElements[element]
        row = idx[0]
        col = idx[1]
        width = idx[2]
        for i in range(width):
            board[row][col+i] = "#"
        self.tempBoard = board
        
    def getAsset(self, asset):
        board = []
        f=open("./assets/gameboard.txt", "r")
        assetLine = f.readline()
        while assetLine != "".join([asset,"\n"]):
            assetLine = f.readline()
        assetLine = f.readline()
        while assetLine != "\n":
            board.append(list(assetLine))
            del board[-1][-1]
            assetLine = f.readline()
            f.close
        return board
        
    def display(self,board):
        dispBoard = board
        for i in range(len(dispBoard)):
            print("".join(dispBoard[i]))
        
    def navigate(self):
        navIn = self.getch.__call__()
        if navIn == "w":
            if self.location[0] == 0:
                self.location[0] = 4
                # TODO: Replace location extremes with len(self.location)
                # and len(self.location[i]) where appropriate
            else:
                self.location[0] -= 1
        elif navIn == "s":
            if self.location[0] == 4:
                self.location[0] = 0
            elif self.location[0] == 2:
                self.location[0] += 1
                self.location[1] = int(self.location[1] / 4)
            else:
                self.location[0] += 1
        elif navIn == "a":
            if self.location[1] == 0:
                self.location[1] = len(self.navDict[self.location[0]])-1
            else:
                self.location[1] -= 1
        elif navIn == "d":
            if self.location[1] == len(self.navDict[self.location[0]]) -1:
                self.location[1] = 0
            else:
                self.location[1] += 1
        else:
            pass
        return self.navDict[self.location[0]][self.location[1]]
        
        # TODO Put special case in to jump twice when
        # up or down from 0 or 00
        
    def getToken(self):
        pass

def copy(original):
    board = []
    for i in range(len(original)):
        board.append([])
        for k in range(len(original[i])):
            board[i].append(original[i][k])
    return board


# Testing
rBoard = RouletteBoard()

rBoard.display(rBoard.board)

for i in range(20):
    element =rBoard.navigate()
    rBoard.replace(element)
    rBoard.display(rBoard.tempBoard)

#Where I'm at: I added the elements dictionary so that we have the
# index and width of each element on the board. We can replace
# an element with the .replace(element) function. The replace()
# function replaces with a "Z" for now.

#Need to add the ability to replace with a sprite or something.
#Maybe a sprite isn't needed
# though and we could just use some better placeholder.

#Also need to add a way to display the gameboard with the replaced
# element. I don't want to update the self.board  variable because
# then we'd lose what was originally in that place. Just want to
# display a temporary board with the marker on some element.

#Eventually it will be sweet to add the ability to move around the
# gameboard using the arrow keys with a blinking marker. 
