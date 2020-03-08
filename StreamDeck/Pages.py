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

        # load icons
        image = Image.open('images/button-back.png')
        button_image_back = ImageTk.PhotoImage(image)

        image = Image.open('images/button-g.png')
        button_image_g = ImageTk.PhotoImage(image)

        image = Image.open('images/button-h.png')
        button_image_h = ImageTk.PhotoImage(image)

        image = Image.open('images/button-i.png')
        button_image_i = ImageTk.PhotoImage(image)

        image = Image.open('images/button-j.png')
        button_image_j = ImageTk.PhotoImage(image)

        image = Image.open('images/button-k.png')
        button_image_k = ImageTk.PhotoImage(image)

        image = Image.open('images/button-l.png')
        button_image_l = ImageTk.PhotoImage(image)

        image = Image.open('images/button-m.png')
        button_image_m = ImageTk.PhotoImage(image)

        # add buttons
        start_page = tk.Button(self, compound = tk.CENTER, image = button_image_back, text = "Back", command = lambda: controller.show_frame(StartPage))
        start_page.grid(row = 0, column = 0)
        start_page.image = button_image_back

        button_g = tk.Button(self, compound = tk.CENTER, image = button_image_g, text = "Button G", command = lambda: button_click('Button G'))
        button_g.grid(row = 0, column = 1)
        button_g.image = button_image_g

        button_h = tk.Button(self, compound = tk.CENTER, image = button_image_h, text = "Button H", command = lambda: button_click('Button H'))
        button_h.grid(row = 0, column = 2)
        button_h.image = button_image_h

        button_i = tk.Button(self, compound = tk.CENTER, image = button_image_i, text = "Button I", command = lambda: button_click('Button I'))
        button_i.grid(row = 0, column = 3)
        button_i.image = button_image_i

        button_j = tk.Button(self, compound = tk.CENTER, image = button_image_j, text = "Button J", command = lambda: button_click('Button J'))
        button_j.grid(row = 1, column = 0)
        button_j.image = button_image_j

        button_k = tk.Button(self, compound = tk.CENTER, image = button_image_k, text = "Button K", command = lambda: button_click('Button K'))
        button_k.grid(row = 1, column = 1)
        button_k.image = button_image_k

        button_l = tk.Button(self, compound = tk.CENTER, image = button_image_l, text = "Button L", command = lambda: button_click('Button L'))
        button_l.grid(row = 1, column = 2)
        button_l.image = button_image_l

        button_m = tk.Button(self, compound = tk.CENTER, image = button_image_m, text = "Button M", command = lambda: button_click('Button M'))
        button_m.grid(row = 1, column = 3)
        button_m.image = button_image_m

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # load icons
        image = Image.open('images/button-back.png')
        button_image_back = ImageTk.PhotoImage(image)

        image = Image.open('images/button-n.png')
        button_image_n = ImageTk.PhotoImage(image)

        image = Image.open('images/button-o.png')
        button_image_o = ImageTk.PhotoImage(image)

        image = Image.open('images/button-p.png')
        button_image_p = ImageTk.PhotoImage(image)

        image = Image.open('images/button-q.png')
        button_image_q = ImageTk.PhotoImage(image)

        image = Image.open('images/button-r.png')
        button_image_r = ImageTk.PhotoImage(image)

        image = Image.open('images/button-s.png')
        button_image_s = ImageTk.PhotoImage(image)

        image = Image.open('images/button-t.png')
        button_image_t = ImageTk.PhotoImage(image)

        # add buttons
        start_page = tk.Button(self, compound = tk.CENTER, image = button_image_back, text = "Back", command = lambda: controller.show_frame(StartPage))
        start_page.grid(row = 0, column = 0)
        start_page.image = button_image_back

        button_n = tk.Button(self, compound = tk.CENTER, image = button_image_n, text = "Button N", command = lambda: button_click('Button N'))
        button_n.grid(row = 0, column = 1)
        button_n.image = button_image_n

        button_o = tk.Button(self, compound = tk.CENTER, image = button_image_o, text = "Button O", command = lambda: button_click('Button O'))
        button_o.grid(row = 0, column = 2)
        button_o.image = button_image_o

        button_p = tk.Button(self, compound = tk.CENTER, image = button_image_p, text = "Button P", command = lambda: button_click('Button P'))
        button_p.grid(row = 0, column = 3)
        button_p.image = button_image_p

        button_q = tk.Button(self, compound = tk.CENTER, image = button_image_q, text = "Button Q", command = lambda: button_click('Button Q'))
        button_q.grid(row = 1, column = 0)
        button_q.image = button_image_q

        button_r = tk.Button(self, compound = tk.CENTER, image = button_image_r, text = "Button R", command = lambda: button_click('Button R'))
        button_r.grid(row = 1, column = 1)
        button_r.image = button_image_r

        button_s = tk.Button(self, compound = tk.CENTER, image = button_image_s, text = "Button S", command = lambda: button_click('Button S'))
        button_s.grid(row = 1, column = 2)
        button_s.image = button_image_s

        button_t = tk.Button(self, compound = tk.CENTER, image = button_image_t, text = "Button T", command = lambda: button_click('Button T'))
        button_t.grid(row = 1, column = 3)
        button_t.image = button_image_t


# function to send the key data
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


# click event
def button_click(caller):
    print("Button: {} was clicked, sending keypress".format(caller))

    if "Button A" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_MOD_LSHIFT, Keycode.KEY_A))
    elif "Button B" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_B, Keycode.KEY_C))
    elif "Button C" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_C))
    elif "Button D" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_D))
    elif "Button E" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_E))
    elif "Button F" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_F))
    elif "Button G" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_G))
    elif "Button H" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_H))
    elif "Button I" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_I))
    elif "Button J" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_J))
    elif "Button K" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_K))
    elif "Button L" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_L))
    elif "Button M" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_M))
    elif "Button N" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_N))
    elif "Button O" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_O))
    elif "Button P" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_P))
    elif "Button Q" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_Q))
    elif "Button R" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_R))
    elif "Button S" == caller:
        write_report(Keycode.KeyCombine(Keycode.KEY_S))
    else:
        write_report(Keycode.KeyCombine(Keycode.KEY_T))

    # reset keypress to none
    time.sleep(0.2)
    write_report("\0\0\0\0\0\0\0\0")
