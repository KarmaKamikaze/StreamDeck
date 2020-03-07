# modules
import os
from tkinter import *
from Pages import StartPage, PageOne, PageTwo


class TkinterWindow(Tk):
    def __init__(self, *args, **kwargs):
        # initialize tkinter
        Tk.__init__(self, *args, **kwargs)
        
        # Setup frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


# start the event loop
window = TkinterWindow()
window.title("PiDeck") # sets title for tkinter windows
if "nt" == os.name: # checks and sets applicatoin icon depending on Windows or Linux
    window.iconbitmap(r'images/PiDeck_icon.ico')
else:
    window.iconbitmap(r'@images/PiDeck_icon.xbm')
window.mainloop()
