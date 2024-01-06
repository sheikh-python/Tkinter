import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='journal')
window.title('ttk bootstrap intro')
window.geometry('400x300')

label = ttk.Label(window, text='Label')
label.pack(pady=10)

button1 = ttk.Button(window, text='red', bootstyle='danger-outline')
button1.pack(pady=10)

button2 = ttk.Button(window, text='warning ', bootstyle='warning-outline')
button2.pack(pady=10)

button3 = ttk.Button(window, text='blue', bootstyle='SUCCESS-outline')
button3.pack(pady=10)
# run
window.mainloop()
