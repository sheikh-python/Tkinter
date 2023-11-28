import tkinter as tk
from tkinter import ttk

def button_func():
    print('a basic button')
    print(radio_var.get())
    
#setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

#button
button_string = tk.StringVar(value='a button with stringvar')
button = ttk.Button (window , text='a simple button' ,
                     command= button_func , 
                     textvariable=button_string)
button.pack()

#checkbutton
check_var = tk.IntVar(value=10)
check1 = ttk.Checkbutton(window , text='checkbox1' ,
                         command= lambda : print(check_var.get()) , 
                         variable= check_var ,
                         onvalue=10 , 
                         offvalue= 5)

check1.pack()

check2 = ttk.Checkbutton(window, text='checkbox 2',
                         command=lambda : check_var.set(5))
check2.pack()
#radiobutton
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window,text='radio button 1 ' ,
                         value=1 , command=lambda : print(radio_var.get()) ,
                         variable= radio_var)
radio1.pack()

radio2 = ttk.Radiobutton(window,text='radio button 2 ' , value='radion2' ,
                         variable=radio_var , command=lambda : print(radio_var.get()))
radio2.pack()

#run
window.mainloop()