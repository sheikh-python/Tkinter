import tkinter as tk
from tkinter import ttk


def button_func():
    print('a button was pressed')


# create a window
root = tk.Tk()
root.title('first windows code')
# window.geometry('Xsize x Ysize ')
root.geometry('800x500')

# ttk label 
label = ttk.Label(master=root, text='hello world')
label.pack()

# tk.text --> for creat a text box on window
text = tk.Text(master=root)
text.pack()

# ttk entry
entry = ttk.Entry(master=root)
entry.pack()

# ttk button
button = ttk.Button(master=root, text='click me! ', command=button_func)
button.pack()

root.mainloop()
