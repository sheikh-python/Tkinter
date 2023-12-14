import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

# top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame,text='First label',background='red')
label2 = ttk.Label(top_frame,text='second label',background='blue')


# middle widget
label3 = ttk.Label(window,text='3 label',background='green')

#bottom widget
bottom_frame = ttk.Frame(window)
bottom_frame2 = ttk.Frame(bottom_frame)
label4 = ttk.Label(bottom_frame,text='last label',background='orange')
button = ttk.Button(bottom_frame,text='A Button')
button2 = ttk.Button(bottom_frame,text='Another Button')
button3 = ttk.Button(bottom_frame2,text='ahmad')
button4 = ttk.Button(bottom_frame2,text='alireza')
button5 = ttk.Button(bottom_frame2,text='tofan')


#top layout
label1.pack(side='left',fill='both',expand=True)
label2.pack(side='left',fill='both',expand=True)
top_frame.pack(fill='both',expand=True)

# middle layout
label3.pack(expand=True , fill='both')

#bottom layout

label4.pack(side='left',expand=True , fill='both')
button.pack(side='left',expand=True , fill='both')
button2.pack(side='left',expand=True , fill='both')
button3.pack(expand=True,fill="both")
button4.pack(expand=True,fill="both")
button5.pack(expand=True,fill="both")
bottom_frame2.pack(side='right',expand=True,fill="both")
bottom_frame.pack(expand=True , fill='both',padx=20 , pady=20)




window.mainloop()




