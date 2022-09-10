from re import X
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Radio Button Test')

frame = tk.LabelFrame(root, text='Please select topping:', padx=10, pady=10)
frame.grid(row=0, column=0, padx=20, pady=20)

# Functionality of 'Confirm' button; remove button and display choice to user.
def confirm():
    global x
    if x.get() == 0:
        return
    confirm_button.grid_forget()
    message = tk.Label(frame, text=f"Thanks. You've ordered a {options[x.get()]}.")    
    message.grid(row=5, column=0, sticky='W')

# Dictionary pairing numerical options with name of topping choice
options = {1: 'Margherita',
           2: 'Meat Feast',
           3: 'Hawaiian',
           4: 'Vegi Volcano'}

# Generating radio buttons for each topping choice
x = tk.IntVar() # variable to store user choice (default 0 for premature pressing of confirmation button)
for option in options.keys():
    button = tk.Radiobutton(frame, text=options[option], variable=x, value=option)
    button.grid(row=option, column=0, sticky='W')

confirm_button = tk.Button(frame, text='Confirm', command=confirm)
confirm_button.grid(row=5, column=0, sticky='W')

root.mainloop()