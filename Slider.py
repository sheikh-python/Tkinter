import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title('slider')
window.geometry('600x400')
scale_double = tk.DoubleVar(value=0)
scale = ttk.Scale(window ,
                  command=lambda value : progress.stop(),
                  from_=0,
                  to=25,length=300 , orient='horizontal',
                  variable=scale_double)
scale.pack()

progress = ttk.Progressbar( window  , variable=scale_double ,
                           maximum=25,
                           orient='horizontal',
                           mode='determinate',
                           length=400
                           )
progress.pack()


progress.start(1000)

#scrolled text

scrolled_text = scrolledtext.ScrolledText(window , width = 100 , height = 5)
scrolled_text.pack()
window.mainloop()