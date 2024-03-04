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

result_label = Label(text="0", font=("Arial", 15))
result_label.grid(row=1, column=0)

eur_label = Label(text="EUR", font=("Arial", 15))
eur_label.grid(row=1, column=1)

# Button
count_button = Button(text="Přepočítat", font=("Arial", 15))
count_button.grid(row=0, column=2)

# Main cycle
root.mainloop()