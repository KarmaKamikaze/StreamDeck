# keyboard report format:
# Byte 0: Keyboard modifier bits (SHIFT, ALT, CTRL etc)
# Byte 1: reserved
# Byte 2-7: Up to six keyboard usage indexes representing the keys that are 
#           currently "pressed". 
#           Order is not important, a key is either pressed (present in the 
#           buffer) or not pressed.

# modules
import time
import tkinter as tk
from PIL import Image, ImageTk
from Keycode import Keycode


# initialize tk
root = tk.Tk()


# function to send the key data
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


# click event
def button_click(caller):
    print("Button: {} was clicked, sending keypress".format(caller))

    if "MuteAudio" == caller:
        write_report(Keycode.Pause)

    elif "BardSpells" == caller:
        MuteAudio.grid_forget()
        BardSpells.grid_forget()

        Back = tk.Button(root, compound = tk.CENTER, image = photoBack, text = "Back", command = lambda: button_click('Back'))
        Back.grid(row = 0, column = 0)

        ViciousMockery = tk.Button(root, compound = tk.CENTER, image = photoViciousMockery, text = "ViciousMockery", command = lambda: button_click('ViciousMockery'))
        ViciousMockery.grid(row = 0, column = 1)
    else:
        return


# load icons
image = Image.open("MuteAudio.png")
photoMuteAudio = ImageTk.PhotoImage(image)

image = Image.open("BardSpells.png")
photoBardSpells = ImageTk.PhotoImage(image)

image = Image.open("ViciousMockery.jpg")
photoViciousMockery = ImageTk.PhotoImage(image)

image = Image.open("Back.jpg")
photoBack = ImageTk.PhotoImage(image)


# add buttons
MuteAudio = tk.Button(root, compound = tk.CENTER, image = photoMuteAudio, text = "Mute Mic", command = lambda: button_click('MuteAudio'))
MuteAudio.grid(row = 0, column = 0)

BardSpells = tk.Button(root, compound = tk.CENTER, image = photoBardSpells, text = "Bard Spells", command = lambda: button_click('BardSpells'))
BardSpells.grid(row = 0, column = 1)


# start the event loop
root.mainloop()