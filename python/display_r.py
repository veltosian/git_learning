#!/usr/bin/python3

class RouletteBoard():
    def __init__(self):
        self.board = []
        self.token = []
        f=open("./assets/gameboard.txt", "r")
        assetLine = f.readline()
        while assetLine != "Asset:gameboard\n":
            assetLine = f.readline()
        assetLine = f.readline()
        while assetLine != "\n":
            self.board.append(assetLine)
            assetLine = f.readline()
            f.close
        self.board[-1] = self.board[-1].strip()
        
    def display(self):
        dispBoard = self.board
        
        print("".join(dispBoard))

    def getToken(self):
        pass
        
# Testing
rBoard = RouletteBoard()

rBoard.display()
