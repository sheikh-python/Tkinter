import tkinter as tk
from tkinter import ttk
def button_func():
    #get the content of the entry 
    entry_text = entry.get()
    # print(entry_text)
    # label.config(text='a new text')
    label['text']=entry_text
    # entry['state']='enable'
    print(label.configure())
    
    
# window
window = tk.Tk()
window.title('Getting and setting widget')

#widget
label = ttk.Label(master=window , text='some text')
label.pack()

entry=ttk.Entry(master=window)
entry.pack()

button=ttk.Button(master=window , text='click' ,command=button_func ) 
button.pack()

#run
window.mainloop()