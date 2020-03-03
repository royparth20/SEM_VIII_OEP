from tkinter import *
import tkinter.font as font
from TicTacToe import TicTacToe
import random
# from Tkinter import font


class Board(object):
    def __init__(self, root):
        self.root = root
        self.btnArray = []
        self.createFrame()
        self.createButtonPlane()
        x=random.randrange(0,8)
        for (_,j) in self.btnArray[0].items():
            self.textSetBtn(j, "x")
        # print("btn Array ")

    def createFrame(self):
        self.frame = Frame(self.root, height=30, width=45)
        self.frame.propagate(0)
        self.frame.pack()

    def createButtonPlane(self):
        count = 0
        self.myFont = font.Font(family="Helvetica", size=12, weight="bold")
        for i in range(3):
            for j in range(3):
                self.createButton(i, j, count)
                count -= -1

    def createButton(self, x, y, index):
        btn = Button(self.frame, bg="black", font=self.myFont, width=15,
                     height=10, borderwidth=1, command=lambda: self.clickBtn(btn, index))
        btn.grid(row=x, column=y)
        self.btnArray.append({(x, y): btn})

    def textSetBtn(self, btn, text):
        btn["text"] = text
        btn.configure(state=DISABLED)

    def clickBtn(self, btn, index):
        self.textSetBtn(btn, "o")
        board = []
        col = 0
        row = 0
        temp = []
        for x in self.btnArray:
            for (_, j) in x.items():
                temp.append(j["text"])
                if col == 2:
                    board.append(temp)
                    temp = []
                    row -= -1
                    col = -1
                col -= -1
        print(board)
        ttt = TicTacToe()
        ttt.set_board(board)
        ttt.set_player('x')
        ttt.set_opponent('o')
        if ttt.isFullBoard(board):
            score = ttt.evaluate(board)
            if score == -10:
                print("You Win")
                return
            elif score == 10:
                print("Computer Win")
                return
        try:
            score = ttt.evaluate(board)
            if score == -10:
                print("You Win")
                return
            elif score == 10:
                print("Computer Win")
                return
            i, j = ttt.findBestMove()
            for x in self.btnArray:
                for(y, button) in x.items():
                    if y == (i, j):
                        print(i, j)
                        self.textSetBtn(button, "x")

            board = []
            col = 0
            row = 0
            temp = []
            for x in self.btnArray:
                for (_, j) in x.items():
                    temp.append(j["text"])
                    if col == 2:
                        board.append(temp)
                        temp = []
                        row -= -1
                        col = -1
                    col -= -1

        except Exception :
            print("Draw")
            pass
        score = ttt.evaluate(board)
        if score == -10:
            print("You Win")
        elif score == 10:
            print("Computer Win")
        # print(i,j)

        # print("-"*25)
        # print(btn["text"],index)
