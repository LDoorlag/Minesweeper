from tkinter import *
class endGui:
    def __init__(self, window):
        '''
        initializes the endGui class and sets up the end screen
        :param window: Tk
        :return: None
        '''
        self.window: Tk = window
        self.window.configure(bg="white")
        self.label: Label = Label(self.window, text="You Lose!", bg="white")
        self.label.pack()
        self.playAgainButton: Button = Button(self.window, text="Play Again", command=self.playAgain, width=30, height=10, bg="turquoise")
        self.playAgainButton.pack()
        self.leaderBoardButton: Button = Button(self.window, text="Leaderboard", command=self.leaderBoard, width=30, height=10, bg="green")
        self.leaderBoardButton.pack()
        self.window.mainloop()
    def playAgain(self):
        '''
        playAgain function starts the startGui class from start.py
        :param: None
        :return: None
        '''
        self.window.destroy()
        from start import startGui
        window: Tk = Tk()
        window.geometry("300x200")
        startGui(window)
        window.mainloop()
    def leaderBoard(self):
        '''
        LeaderBoard function starts the leaderboard class from leaderboard.py
        :param: None
        :return: None
        '''
        self.window.destroy()
        from leaderboard import leaderboard
        leaderboard(Tk())
