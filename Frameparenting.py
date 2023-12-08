import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')

frame = ttk.Frame(window ,width=200 ,
                  height=200 , borderwidth=10 ,
                  relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')
label = ttk.Label(frame, text='label in frame')
label.pack()
button = ttk.Button(frame,text='button in a frame')
button.pack()

label2 = ttk.Label(window,text='a label in a main window')
label2.pack(side='left')

# run
window.mainloop()