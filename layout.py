import tkinter as tk
from tkinter import ttk

#window 
window = tk.Tk()
window.title('Layout basic')
window.geometry('600x400')

#hex color picker
#widgets
labal1 = ttk.Label(window,text='label 1',background='#34d8eb')
labal2 = ttk.Label(window,text='label 2',background='#e534eb')

# #pack
# labal1.pack(side='left',expand= True , fill='both')
# labal2.pack(side='left',expand=True , fill='both')

#grid 
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)


# labal1.grid(row=0 , column= 1 , sticky='nsew' )
# labal2.grid(row=1 , column= 1 ,columnspan=2, sticky='nsew' )

#place
labal1.place(x=100 , y =200 , width= 200 , height=100)
labal2.place(relx=.5 , rely=0.5 ,relwidth=1 , anchor='center')

#run
window.mainloop()