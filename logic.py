from minesweeper import myGUI
import keyboard as kb
import time
class Logic(myGUI):
    '''
    Logic class runs all of the logic/buttons for the minesweeper game
    '''
    def __init__(self, window):
        '''
        initializes the logic class and runds the map generation function
        :param window: Tk
        :return: None
        '''
        super().__init__(window)
        self.map: list = self.GenerateMineSweeperMap()
        self.count: int = 0
        self.startTime: time = time.time()
    def click(self, row, column):
        '''
        the click function runs when a button on the grid is clicked and handles the logic of what should happen after that
        :param row: int
        :param column: int
        :return: None
        '''
        if kb.is_pressed('ctrl'):
            self.listofbuttons[row][column].config(text='F')
            self.listofbuttons[row][column].config(bg='red')
            return
        if row < 0 or row > 5 or column < 0 or column > 5:
            return
        if self.listofbuttons[row][column]['state'] == 'disabled':
            return
        print(row, column)
        if self.map[row][column] == 'x':
            self.listofbuttons[row][column].config(text='x')
            self.listofbuttons[row][column].config(state='disabled')
            self.listofbuttons[row][column].config(bg='black')
            self.gameOver()
        else:
            self.count += 1
            if self.map[row][column] ==0:
                self.listofbuttons[row][column].config(bg='yellow')
                self.listofbuttons[row][column].config(text=' ')
                self.listofbuttons[row][column].config(state='disabled')
                self.recursiveClear(row, column)
            else:
                self.listofbuttons[row][column].config(bg='yellow')
                self.listofbuttons[row][column].config(state='disabled')
                self.listofbuttons[row][column].config(text=self.map[row][column])
            if self.map[row][column] == 1:
                self.listofbuttons[row][column].config(fg='blue')
            elif self.map[row][column] == 2:
                self.listofbuttons[row][column].config(fg='green')
            elif self.map[row][column] == 3:
                self.listofbuttons[row][column].config(fg='red')
            elif self.map[row][column] == 4:
                self.listofbuttons[row][column].config(fg='purple')
            elif self.map[row][column] == 5:
                self.listofbuttons[row][column].config(fg='maroon')
            elif self.map[row][column] == 6:
                self.listofbuttons[row][column].config(fg='turquoise')
            elif self.map[row][column] == 7:
                self.listofbuttons[row][column].config(fg='black')
            elif self.map[row][column] == 8:
                self.listofbuttons[row][column].config(fg='grey')
            if self.count >= 28:
                endTime: time = time.time()
                result: time = endTime - self.startTime
                result: time = round(result, 2)
                self.gameWin(result)
    def recursiveClear(self, row, column):
        '''
        A recursive function to clear empty spaces when an empty space is clicked
        '''
        self.click(row-1, column)
        self.click(row+1, column)
        self.click(row, column-1)
        self.click(row, column+1)
        self.click(row-1, column-1)
        self.click(row-1, column+1)
        self.click(row+1, column-1)
        self.click(row+1, column+1)
        return
    def gameOver(self):
        '''
        if the game ends and is lost, this function runs allowing for either a restart or the leaderboard
        :param: None
        :return: None
        '''
        time.sleep(2)
        self.window.destroy()
        from end import endGui
        from tkinter import Tk
        window: Tk = Tk()
        window.geometry("300x400")
        window.resizable(False, False)
        endGui(window)
    def gameWin(self, time):
        '''
        if the game ends and is won, this function runs allowing for the user to enter their name and save their score
        :param time: float
        :return: None
        '''
        self.window.destroy()
        from win import winGui
        from tkinter import Tk
        window: Tk = Tk()
        window.geometry("300x400")
        window.resizable(False, False)
        winGui(window, time)
        




        

    