import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Menu')


#menu 
menu = tk.Menu(window)

#submenu
file_menu = tk.Menu(menu , tearoff= False)
file_menu.add_command(label='New',command=lambda:print('New File'))
file_menu.add_separator()
file_menu.add_command(label='Open',command=lambda:print('Open File'))


menu.add_cascade(label='File', menu=file_menu)

#another sub menu 
help_menu = tk.Menu(menu , tearoff=False)
help_menu.add_command(label='Help entry ' , command= lambda : print(help_chek_string.get()))

help_chek_string =tk.StringVar()
help_menu.add_checkbutton(label='Chek',onvalue='on' , offvalue='off' , variable= help_chek_string)

menu.add_cascade(label='Help', menu=help_menu)

sub_munu = tk.Menu(menu , tearoff=False)
sub_munu.add_command(label='some more stuff')
file_menu.add_cascade(label='more stuff',menu=sub_munu)


window.configure(menu=menu)


#menu button
menu_button = ttk.Menubutton(window, text='Menu button ')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button ,tearoff=False)
button_sub_menu.add_command(label='entry 1' , command= lambda : print('test'))
button_sub_menu.add_checkbutton(label='chek 1')

# menu_button.configure(menu=button_sub_menu)
menu_button['menu']=button_sub_menu

# run
window.mainloop()