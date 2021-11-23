from tkinter import *
import random
from tkinter import messagebox
# from pynput import keyboard
import keyboard
import pyautogui
import lights
from playsound import playsound

class Test:
    def __init__(self, master):
        self.root = Toplevel(master)
        self.root.title("lol")
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.photo = PhotoImage(file='johnpython.png')
        self.win_dim = f"{self.photo.width()}x{self.photo.height()}+"

        self.root.geometry(self.win_dim + "100+100")

        label = Label(self.root, image=self.photo)
        label.place(x=10, y=10)
        self.dim = pyautogui.size()

        self.move_me()


    def move_me(self):
        x, y = str(random.randrange(self.dim[0])), str(random.randrange(self.dim[0]))
        loc = self.win_dim + x + '+' + y
        self.root.geometry(loc)
        self.checker()
        self.root.after(500, self.move_me)

    def on_exit(self): #prevents users from being able to terminate windows
        Test(tk)
        lights.showing()
        playsound('music/christmas.mp3', block=False)
        messagebox.showinfo(title="HOHOHOHO", message="Enjoy these gifts!")

    def checker(self):
        if keyboard.is_pressed('q'):
            Test(tk)
            lights.showing()
            playsound('music/christmas.mp3', block=False)



def main():
    tk = Tk()
    tk.withdraw()
    Test(tk)
    lights.showing()
    playsound('music/christmas.mp3', block = False)

    tk.mainloop()

if __name__ == '__main__':
    main()
