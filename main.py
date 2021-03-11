from tkinter import *
from tkinter import font
import ctypes
root = Tk()
root.geometry("400x215")
root.title("Currency Converter")

defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(size=11)


# Deletes text in entry field
def clear():
    usdEntry.delete(0, "end")
    poundLabel.configure(text="Pounds: 0")
    francLabel.configure(text="Francs:0")
    lireLabel.configure(text="Lire:   0")
    markLabel.configure(text="Marks: 0")
    pesetaLabel.configure(text="Pesetas:0")
    usdLabel.configure(text="USD:   0")


# Gets info from entry field, converts it into other currencies
def get_usd():
    usd = usdEntry.get()
    try:
        usd = float(usd)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(0, u"Invalid Input", u"Error", 0)
    francs = round(usd * 6.1, 2)
    pounds = round(usd * 0.64, 2)
    lire = round(usd * 1793.62, 2)
    mark = round(usd * 1.811, 2)
    pesetas = round(usd * 154.076, 2)

    poundLabel.configure(text=f"Pounds: {pounds}")
    francLabel.configure(text=f"Francs:{francs}")
    lireLabel.configure(text=f"Lire:   {lire}")
    markLabel.configure(text=f"Marks: {mark}")
    pesetaLabel.configure(text=f"Pesetas:{pesetas}")
    usdLabel.configure(text=f"USD:   {usd}")


# Where Labels are defined
poundLabel = Label(text="Pounds: 0", font="TkFixedFont")
francLabel = Label(text="Francs:0", font="TkFixedFont")
lireLabel = Label(text="Lire:   0", font="TkFixedFont")
markLabel = Label(text="Marks: 0", font="TkFixedFont")
pesetaLabel = Label(text="Pesetas:0", font="TkFixedFont")
usdLabel = Label(text="USD:   0", font="TkFixedFont")

# Creates entry field and puts some text in it.
usdEntry = Entry(font="TkFixedFont")
usdEntry.insert(0, "   Enter USD Here")

# Where the buttons are defined
clearEntry = Button(text="Clear", command=clear, width=9, font="TkFixedFont")
quitButton = Button(text="Quit", command=quit, width=9, font="TkFixedFont")
getMoney = Button(text="Calculate", command=get_usd, width=9, font="TkFixedFont")

# Places the buttons
clearEntry.place(x=151, y=25)
quitButton.place(x=151, y=95)
getMoney.place(x=151, y=60)

# Places the entry field
usdEntry.place(x=110, y=0)

# Places the labels
usdLabel.place(x=95, y=133)
poundLabel.place(x=214, y=133)

markLabel.place(x=95, y=153)
pesetaLabel.place(x=214, y=153)

francLabel.place(x=95, y=173)
lireLabel.place(x=214, y=173)

# Keeps window open
root.mainloop()
