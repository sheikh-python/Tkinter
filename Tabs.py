import tkinter as tk
from tkinter import ttk
 
window = tk.Tk()
window.geometry('600x400')
window.title("Tab Widget")

#Notebook widget

notebook = ttk.Notebook(window)
tab1=ttk.Frame(notebook)
label = ttk.Label(tab1 , text='Text in tab 1')
label.pack()
button1 = ttk. Button(tab1 , text='button in tab 1')
button1.pack()

tab2=ttk.Frame(notebook)
label2 = ttk.Label(tab2, text=('text in tab 2'))
label2.pack()
entry = ttk.Entry(tab2)
entry.pack()

notebook.add(tab1, text='tab 1')
notebook.add(tab2, text='tab 2')
notebook.pack()

# run 
window.mainloop()  