from tkinter import *

# Main window
root = Tk()
root.title("Převod měn")
root.minsize(200,200)
root.resizable(False, False)
root.config(bg="#003399")
root.iconbitmap("icon.ico")


# Function
def convert_currency():
    amount_eur = float(amount_input.get()) / 25.38
    result_label["text"] = round(amount_eur, 2)

# User input
amount_input = Entry(width=10, font=("Arial", 15))
amount_input.grid(row=0, column=0, padx=10, pady=10)

#Labels
czk_label = Label(text="CZK", font=("Arial", 15), bg="#003399", fg="white")
czk_label.grid(row=0, column=1)

result_label = Label(text="0", font=("Arial", 15), bg="#003399", fg="white")
result_label.grid(row=1, column=0)

eur_label = Label(text="EUR", font=("Arial", 15), bg="#003399", fg="white")
eur_label.grid(row=1, column=1)

# Button
count_button = Button(text="Přepočítat", font=("Arial", 15), command=convert_currency)
count_button.grid(row=0, column=2, padx=10, pady=10)

# Main cycle
root.mainloop()