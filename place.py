import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Place')
window.geometry('400x600')

# widgets 
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
button = ttk.Button(window, text = 'Button')

#layout

label1.place(x=300,y=100,width=100,height=200)
label2.place(relx= .2 , rely=.1 , relwidth=.4 , relheight=.5)
label3.place(x= 80 , y=60 , width=160 , height=300)
button.place(relx=1 , rely=1 ,anchor='center')

#frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text='frame label ',background='yellow')
frame_button = ttk.Button( frame, text='frame button')

#frame_layout
frame.place(relx= 0 , rely=0 , relwidth=.3 , relheight=1)
frame_label.place(relx=0, rely=0 , relwidth=1 , relheight=.5)
frame_button.place(relx=0, rely=.5 , relwidth=1 , relheight=.5)

# run
window.mainloop()
