from tkinter import *
import random
class myGUI:
    def __init__(self, window):
        '''
        initializes the GUI and makes the buttons to represent the minesweeper grid
        :param window: Tk
        :return: None
        '''
        self.window: Tk = window
        self.window.title("Minesweeper")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.configure(bg="white")
        self.listofbuttons: list = []
        for row in range(6):
            self.listofbuttons.append([])
            for column in range(6):
                print(row, column)
                button = Button(self.window, width=10, height=5, bg="white", command=lambda row=row, column=column: self.click(row, column))
                button.grid(row=row, column=column)
                self.listofbuttons[row].append(button)
    def GenerateMineSweeperMap(self):
        '''
        creates the minesweeper map
        :param: None
        :return: list
        '''
        n: int = 6
        NumberOfMines: int = 8
        arr: list = [[0 for row in range(n)] for column in range(n)]
        CoordList: list = []
        while NumberOfMines > 0:
            x: int = random.randint(0,n-1)
            y: int = random.randint(0,n-1)
            tempvar: list = x, y
            if tempvar in CoordList:
                continue
            else:
                arr[y][x] = 'x'
                CoordList.append(tempvar)
                NumberOfMines -= 1
        
            if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
                if arr[y][x+1] != 'x':
                    arr[y][x+1] += 1
            if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
                if arr[y][x-1] != 'x':
                    arr[y][x-1] += 1
            if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
                if arr[y-1][x-1] != 'x':
                    arr[y-1][x-1] += 1
 
            if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
                if arr[y-1][x+1] != 'x':
                    arr[y-1][x+1] += 1
            if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
                if arr[y-1][x] != 'x':
                    arr[y-1][x] += 1
 
            if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
                if arr[y+1][x+1] != 'x':
                    arr[y+1][x+1] += 1
            if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
                if arr[y+1][x-1] != 'x':
                    arr[y+1][x-1] += 1
            if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
                if arr[y+1][x] != 'x':
                    arr[y+1][x] += 1
        return arr