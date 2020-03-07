# modules
import time
import tkinter as tk
from PIL import Image, ImageTk
from Keycode import Keycode


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # load icons
        image = Image.open('images/button-pageone.png')
        button_image_pageone = ImageTk.PhotoImage(image)

        image = Image.open('images/button-pagetwo.png')
        button_image_pagetwo = ImageTk.PhotoImage(image)

        image = Image.open('images/button-a.png')
        button_image_a = ImageTk.PhotoImage(image)

        image = Image.open('images/button-b.png')
        button_image_b = ImageTk.PhotoImage(image)

        image = Image.open('images/button-c.png')
        button_image_c = ImageTk.PhotoImage(image)

        image = Image.open('images/button-d.png')
        button_image_d = ImageTk.PhotoImage(image)

        image = Image.open('images/button-e.png')
        button_image_e = ImageTk.PhotoImage(image)

        image = Image.open('images/button-f.png')
        button_image_f = ImageTk.PhotoImage(image)

        # add buttons
        page_one = tk.Button(self, compound = tk.CENTER, image = button_image_pageone, text = "Page One", command = lambda: controller.show_frame(PageOne))
        page_one.grid(row = 0, column = 0)
        page_one.image = button_image_pageone # saves the button's image from garbage collection

        page_two = tk.Button(self, compound = tk.CENTER, image = button_image_pagetwo, text = "Page Two", command = lambda: controller.show_frame(PageTwo))
        page_two.grid(row = 0, column = 1)
        page_two.image = button_image_pagetwo

        button_a = tk.Button(self, compound = tk.CENTER, image = button_image_a, text = "Button A", command = lambda: button_click('Button A'))
        button_a.grid(row = 0, column = 2)
        button_a.image = button_image_a

        button_b = tk.Button(self, compound = tk.CENTER, image = button_image_b, text = "Button B", command = lambda: button_click('Button B'))
        button_b.grid(row = 0, column = 3)
        button_b.image = button_image_b

        button_c = tk.Button(self, compound = tk.CENTER, image = button_image_c, text = "Button C", command = lambda: button_click('Button C'))
        button_c.grid(row = 1, column = 0)
        button_c.image = button_image_c

        button_d = tk.Button(self, compound = tk.CENTER, image = button_image_d, text = "Button D", command = lambda: button_click('Button D'))
        button_d.grid(row = 1, column = 1)
        button_d.image = button_image_d

        button_e = tk.Button(self, compound = tk.CENTER, image = button_image_e, text = "Button E", command = lambda: button_click('Button E'))
        button_e.grid(row = 1, column = 2)
        button_e.image = button_image_e

        button_f = tk.Button(self, compound = tk.CENTER, image = button_image_f, text = "Button F", command = lambda: button_click('Button F'))
        button_f.grid(row = 1, column = 3)
        button_f.image = button_image_f


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One")
        label.pack(padx=10, pady=10)

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page Two")
        label.pack(padx=10, pady=10)


# function to send the key data
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


# click event
def button_click(caller):
    print("Button: {} was clicked, sending keypress".format(caller))

    if "Button A" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_A))
    elif "Button B" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_B))
    elif "Button C" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_C))
    elif "Button D" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_D))
    elif "Button E" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_E))
    else:
        write_report(Keycode.KeyCombine(Keycode.KEY_F))

    # reset keypress to none
    time.sleep(0.2)
    write_report("\0\0\0\0\0\0\0\0")
