__author__ = 'ethan'

import Tkinter as tk
import ttk
from . import vbForms


class Window1:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Window1 Title")
        self.root.wm_title("TkinterTest")

        self.style1 = ttk.Style()
        self.style1.configure('My.TLabel', foreground='red')

        self.style2 = vbForms.Style()
        self.style2.name_style('test.TLabel')
        self.style2.foreground('blue')
        # self.style2.configure('test.TLabel', foreground='blue')

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.feet = tk.StringVar()
        self.meters = tk.StringVar()

        # self.txt_in_feet = ttk.Entry(self.mainframe, width=7, textvariable=self.feet)
        # self.txt_in_feet.grid(column=2, row=1, sticky=(tk.W, tk.E))

        self.txt_in_feet = vbForms.TextInput(self.mainframe, width=7, textvariable=self.feet)
        self.txt_in_feet.grid(column=2, row=1, sticky=(tk.W, tk.E))

        self.txt_in_feet.style = 'test.TEntry'

        self.lbl_result = ttk.Label(self.mainframe, textvariable=self.meters)
        self.lbl_result.grid(column=2, row=2, sticky=(tk.W, tk.E))

        self.btn_calc = ttk.Button(self.mainframe, text="Calculate", command=self.calculate)
        self.btn_calc.grid(column=3, row=3, sticky=tk.W)

        # self.lbl_feet = ttk.Label(self.mainframe, text="feet")
        # self.lbl_feet.grid(column=3, row=1, sticky=tk.W)

        self.lbl_feet = vbForms.Label(self.mainframe, text="feet")
        self.lbl_feet.grid(column=3, row=1, sticky=tk.W)

        self.lbl_equiv = ttk.Label(self.mainframe, text="is equivalent to")
        self.lbl_equiv.grid(column=1, row=2, sticky=tk.E)

        self.lbl_meters = vbForms.Label(self.mainframe, text="meters")
        self.lbl_meters.grid(column=3, row=2, sticky=tk.W)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.txt_in_feet.focus()
        self.root.bind('<Return>', self.calculate)
        self.root.mainloop()

    def calculate(self, *args):
        try:
            value = float(self.feet.get())

            self.txt_in_feet.foreground = 'black'
            self.txt_in_feet.background = 'white'
            self.meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
            self.lbl_feet.text = "words"
            self.lbl_feet.style = 'My.TLabel'

            self.lbl_meters.style = self.style2

            if value == 7.0:
                print self.txt_in_feet.value
                self.txt_in_feet.value = 5
                print self.txt_in_feet.value
                self.lbl_feet.foreground = 'green'
                self.txt_in_feet.background = 'green'
                self.txt_in_feet.foreground = 'white'

        except ValueError:
            pass


Window1()
