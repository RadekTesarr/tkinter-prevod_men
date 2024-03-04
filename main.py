from tkinter import *

# Main window
root = Tk()
root.title("Převod měn")
root.minsize(200,200)
root.resizable(False, False)

# 1 eur = 25,38

# User input
amount_input = Entry(width=10, font=("Arial", 15))
amount_input.grid(row=0, column=0)

#Labels
czk_label = Label(text="CZK", font=("Arial", 15))
czk_label.grid(row=0, column=1)

# Main cycle
root.mainloop()