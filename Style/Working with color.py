import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('colors')
window.geometry('400x300')

# widgets
ttk.Label(window, background="#00787f").pack(expand=True, fill='both')
ttk.Label(window, background="#c208b8").pack(expand=True, fill='both')
ttk.Label(window, background="#c208b8").pack(expand=True, fill='both')

# run
window.mainloop()
