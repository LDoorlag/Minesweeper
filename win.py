from tkinter import *

class winGui:
    def __init__(self, window, time):
        '''
        initializes the winGui class and sets up the win screen
        :param window: Tk
        :param time: float
        :return: None
        '''
        self.window: Tk = window
        self.window.configure(bg="white")
        self.label: Label = Label(self.window, text="You Win!", bg="white")
        self.label.pack()
        self.nameLabel: Label = Label(self.window, text="Enter your name:", bg="white")
        self.nameLabel.pack()
        self.nameEntry: Entry = Entry(self.window)
        self.nameEntry.pack()
        self.submitButton: Button = Button(self.window, text="Submit", command=lambda: self.submit(time), width=30, height=10, bg="orange")
        self.submitButton.pack()
        self.window.mainloop()
    def submit(self, time):
        '''
        submit function saves name and time to scores.txt
        :param time: float
        :return: None
        '''
        name = self.nameEntry.get()
        with open("scores.txt", "a") as file:
            file.write(f"{name.replace(' ', '')} {time}\n")
        self.window.destroy()
        from leaderboard import leaderboard
        leaderboard(Tk())
winGui(Tk(), 19)