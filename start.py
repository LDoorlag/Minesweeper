from tkinter import *
class startGui:
    '''
    startGui is a class for the start screen of the minesweeper game
    '''
    def __init__(self, window):
        '''
        initializes the startGui class and sets up the start button
        :param window: Tk
        :return: None
        '''
        self.window: Tk = window
        self.window.configure(bg="white")
        self.button: Button = Button(self.window, text="Start", command=self.start, width=80, height=80, bg="turquoise")
        self.button.pack()

        self.window.mainloop()
    def start(self):
        '''
        the start function runs the Logic class from logic.py
        :param: None
        :return: None
        '''
        self.window.destroy()
        from logic import Logic
        window: Tk = Tk()
        Logic(window)
        window.mainloop()

