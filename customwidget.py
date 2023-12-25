import tkinter as tk
from tkinter import ttk

def creat_segment(parent,label_text, label_button):
    frame = ttk.Frame(master=parent)
    # grid layout
    frame.rowconfigure(0,weight=1)
    frame.columnconfigure((0,1,2),weight=1 , uniform='a')
    # widget
    ttk.Label(frame, text=label_text).grid(row=0 , column=0 , sticky='nsew')
    ttk.Button(frame, text=label_button).grid(row=0 , column=1 , sticky='nsew')
    
    return frame

class Segment(ttk.Frame):
    def __init__(self,parent,label_text, label_button , text_part2):
        super().__init__(master=parent)
        
        # grid layout
        self.rowconfigure(0,weight=1)
        self.columnconfigure((0,1,2),weight=1 , uniform='a')
        
        #widget
        ttk.Label(self, text=label_text).grid(row=0 , column=0 , sticky='nsew')
        ttk.Button(self, text=label_button).grid(row=0 , column=1 , sticky='nsew')
        self.creat_part2(text_part2).grid(row=0 , column=2 , sticky='nsew')
        self.pack(expand=True , fill='both' , padx=10 , pady=10 )
        
    def creat_part2(self,text):
        frame = ttk.Frame(master=self)
        entry = ttk.Entry(frame).pack(expand=True , fill='both')
        button = ttk.Button(frame , text=text).pack(expand=True , fill='both')
        
        return frame

#window
window = tk.Tk()
window.title('widgets and return')
window.geometry('400x600')

# creat_segment(window , 'label' , 'button').pack(expand=True , fill='both' , padx=10 , pady=10 )
# creat_segment(window , 'test' , 'bench').pack(expand=True , fill='both' , padx=10 , pady=10 )
# creat_segment(window , 'ahmad' , 'ali').pack(expand=True , fill='both' , padx=10 , pady=10 )
# creat_segment(window , 'sara' , 'click').pack(expand=True , fill='both' , padx=10 , pady=10 )
# creat_segment(window , 'hashem' , 'text').pack(expand=True , fill='both' , padx=10 , pady=10 )


Segment(window , 'label' , 'button','part1')
Segment(window , 'test' , 'bench','part2')
Segment(window , 'ahmad' , 'ali','part3')
Segment(window , 'sara' , 'click','part4')
Segment(window , 'hashem' , 'text','part5')


#run
window.mainloop()