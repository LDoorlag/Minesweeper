from tkinter import *

class leaderboard():
    def __init__(self, window):
        '''
        initializes and builds the leaderboard by taking and sorting the data from the csv
        :param window: Tk
        :return: None
        '''
        self.window: Tk = window
        self.window.title("Leaderboard")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.configure(bg="black")
        with open("scores.txt", "r") as file:
            data: str = file.read()
            list: str = data.split("\n")
            result: tuple = []
            for i in list:
                if i == "":
                    continue
                print(i)
                score = i.split()
                time: str = score[1]
                name: str = score[0]
                result.append((name, time))
            result.sort(key=lambda x: x[1])
            for i in range(12):
                if i >= len(result):
                    break
                name, time = result[i]
                label: Label = Label(self.window, text=f"{i+1}.  {name} - {time}", bg="black", fg="white", font=("Arial", 20))
                label.pack()
        self.playAgainButton: Button = Button(self.window, text="Play Again", command=self.playAgain, width=30, height=10, bg="red")
        self.playAgainButton.pack()
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
