import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self , title , size):
        
        #Main setup
        super().__init__()
        self.title= title
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        
        #widget
        self.Menu = Menu(self)
        self.Main = Main(self)
        
        #run
        self.mainloop()
        

class Menu(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x=0,y=0,relwidth=.3,relheight=1) 
        
        self.creat_widget()
        
    def creat_widget(self):
        menu_button1 =ttk.Button(self , text= 'button 1')
        menu_button2 =ttk.Button(self , text= 'button 2')
        menu_button3 =ttk.Button(self , text= 'button 3')

        menu_slider1 =ttk.Scale(self , orient= 'vertical')
        menu_slider2 =ttk.Scale(self , orient= 'vertical')

        toggle_frame =ttk.Frame(self)
        menu_toggle1 =ttk.Checkbutton(toggle_frame, text= 'check1')
        menu_toggle2 =ttk.Checkbutton(toggle_frame, text= 'check2')

        entry = ttk.Entry(self)
         
        self.columnconfigure((0,1,2),weight= 1 , uniform='a')
        self.rowconfigure((0,1,2,3,4),weight= 1 , uniform='a')
        menu_button1.grid(row=0 , column=0 , sticky='nswe'  , columnspan=2)
        menu_button2.grid(row=0 , column=2 , sticky='nswe'  )
        menu_button3.grid(row=1 , column=0 , sticky='nswe'  , columnspan=3)

        menu_slider1.grid(row=2 , column=0 , rowspan=2 , sticky='nswe' , pady=20)
        menu_slider2.grid(row=2 , column=2 , rowspan=2 , sticky='nswe' , pady=20)  
        
        # toggle layout
        toggle_frame.grid(row=4 ,column=0 , columnspan=3 , sticky= 'nswe')
        menu_toggle1.pack(side='left' , expand=True)
        menu_toggle2.pack(side='left' , expand=True)
                
        #entry layout
        entry.place(relx=.5 , rely= .95 , relwidth= .9 ,anchor='center')  

class Main(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent) 
        self.place(relx=.3,y=0,relwidth=.7,relheight=1) 
        Entry(self,'ahmad','ahmad_button','blue')
        Entry(self,'ali','ali_button','red')
        

class Entry(ttk.Frame):
    def __init__(self,parent,label_text,button_text , label_background):
        super().__init__(parent)
        
        label = ttk.Label(self , text=label_text , background=label_background)      
        button = ttk.Button(self, text=button_text)
        
        label.pack(expand=True , fill="both")
        button.pack(expand=True , fill='both', pady=10 ) 
        
        self.pack(side='left', expand=True , fill= 'both', padx=20 , pady=20)
    

App('Class based app',(600,600))