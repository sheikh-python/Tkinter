import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')

#combobox

items = ('ahmad','reza', 'ali','mamad')
food_var = tk.StringVar(value=items[0])
combo = ttk.Combobox(window , textvariable=food_var)
combo['values'] = items

# combo.config(values=items)
combo.pack()

combo_label = ttk.Label(window, text='name')
combo_label.pack()

#events
#combo.bind('event',function)
combo.bind('<<ComboboxSelected>>',
           lambda event : combo_label.config(text=f'selected value : {food_var.get()}') ) 


#spinbox
spin_int = tk.IntVar(value=[])
spin = ttk.Spinbox(window , 
                #    from_=8 , 
                #    to=50 , increment= 5 ,
                   command=lambda : print(spin_int.get()) ,
                   textvariable=spin_int)

spin.bind('<<Increment>>' , lambda event : print('up'))
spin.bind('<<Decrement>>' , lambda event : print('down'))

letter = ('a', 'b' , 'c' , 'd')
spin['values']=letter
# spin['values']=(1,2,3,4,5,6)
spin.pack()


# run
window.mainloop()
