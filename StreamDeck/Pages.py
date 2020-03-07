# modules
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
    else:
        return

    # reset keypress to none
    time.sleep(0.2)
    write_report("\0\0\0\0\0\0\0\0")
