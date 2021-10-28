# IMPORT
import thinker
from tkinter import *

# CURRANCYCALCULATOR
class Currancy_Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Currancy Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()

        self.total_label_text.set(self.total)

        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.usd_button = Button(master, text="USD", command=lambda: self.update("USD"))
        self.cny_button = Button(master, text="CNY", command=lambda: self.update("CNY"))
        self.gbp_button = Button(master, text="GBP", command=lambda: self.update("GBP"))
        self.eur_button = Button(master, text="EUR", command=lambda: self.update("EUR"))
        self.dkk_button = Button(master, text="DKK", command=lambda: self.update("DKK"))
        self.skk_button = Button(master, text="SKK", command=lambda: self.update("SKK"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=8, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=8, sticky=W+E)

        self.usd_button.grid(row=2, column=0)
        self.cny_button.grid(row=2, column=1)
        self.gbp_button.grid(row=2, column=2)
        self.eur_button.grid(row=2, column=3)
        self.dkk_button.grid(row=2, column=4)
        self.skk_button.grid(row=2, column=5)

    def validate(self, new_text):
        if not new_text: # clearing
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "USD":
            self.total = ((self.entered_number) * (0.12))

        elif method == "CNY":
            self.total = ((self.entered_number) * (0.78))

        elif method == "GBP":
            self.total = ((self.entered_number) * (0.086))

        elif method == "EUR":
            self.total = ((self.entered_number) * (0.100))

        elif method == "DKK":
            self.total = ((self.entered_number) * (0.74))

        elif method == "SKK":
            self.total = ((self.entered_number) * (2.02))

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Currancy_Calculator(root)
root.mainloop()