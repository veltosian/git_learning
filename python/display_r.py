#!/usr/bin/python3

class RouletteBoard():
    def __init__(self):
        self.board = []
    f=open("./assets/gameboard.txt", "r")
        assetLine = f.readline()
        while assetLine != "":
            self.board.append(assetLine)
            assetLine = f.readline()
            f.close
    def display(self):
        print("".join(self.board))


# Testing
rBoard = RouletteBoard()

rBoard.display()
