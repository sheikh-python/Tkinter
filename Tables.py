import tkinter as tk
from tkinter import ttk
from random import choice


# window
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# data 
first_names = ['ahmad', 'ali', 'reza', 'mina', 'zahra', 'sadra', 'farshad', 'Anna', 'sara']
last_names = ['Sheikhzadeh', 'mohammadi', 'shiran zadeh', 'fatemi', 'alipour', 'rahmati', 'fadaei', 'bagheri']

#treeview
table = ttk.Treeview(window,columns=('first','last','email'),show='headings')
table.heading('first',text='Firstname')
table.heading('last',text='Lastname')
table.heading('email',text='Email')
table.pack(fill='both',expand=True)

#table.insert(parent='',index=0,values=('ahmad','sheikh','ahmadsheikh@gmail.com'))

for i in range(100):
    first=choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@gmail.com'
    data = (first,last,email)
    table.insert(parent='',index=0,values=data)

table.insert(parent='',index=tk.END,values=('rrrrrr','ttttttttttt','jjjjjjjjjjj'))

#events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    print('Delete')
    # table.delete(table.selection())
    for i in table.selection():
        table.delete(i)


table.bind('<<TreeviewSelect>>' ,  item_select)
table.bind('<Delete>' , delete_items)
# run 
window.mainloop()