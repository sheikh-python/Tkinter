import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Grid')
window.geometry('600x400')

# widgets 
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
label4 = ttk.Label(window, text = 'Label 4', background = 'yellow')
button1 = ttk.Button(window, text = 'Button 1')
button2 = ttk.Button(window, text = 'Button 2')
entry = ttk.Entry(window)

# define a grid

window.columnconfigure((0,1,2),weight=1,uniform='a')
window.columnconfigure(3,weight=10,uniform='a')
window.rowconfigure((0,1,2),weight=1,uniform='a')
window.rowconfigure(3,weight=4,uniform='a')


#place a widget

label1.grid(row=0 , column= 0 , sticky='nsew' )
label2.grid(row=0 , column= 2 ,rowspan=1 , sticky='nsew' )
label3.grid(row=2 , column= 2 ,columnspan=1, sticky='nsew' )
label4.grid(row=3 , column= 3 , sticky='nsew' )


# run
window.mainloop()