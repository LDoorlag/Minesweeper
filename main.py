from tkinter import *
from start import startGui
if __name__ == "__main__":
    window = Tk()
    window.title("Press Start to Play")
    window.geometry("300x200")
    window.resizable(False, False)
    startGui(window)
    window.mainloop()