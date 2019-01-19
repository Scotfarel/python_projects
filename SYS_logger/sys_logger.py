import time
from tkinter import Tk, Label
 
 
class WindowLog(object):
 
    def __init__(self, master):
        self.master = master
        self.master.title("You started at:")
        self.master.config(bg="#420")
        self.master.resizable(0, 0)
 
 
if __name__ == "__main__":
    init_time = time.asctime()
    app = Tk()
 
    window = WindowLog(app)
    Label(app, text=init_time).grid(row=0, column=0)
    app.mainloop()
    