import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
image = tk.PhotoImage(file='icon.png')
window.title('More on the window')
window.geometry('600x400+100+200')
window.iconphoto(False,image)

#window sizes

# window.minsize(300,400)
# window.maxsize(500, 500)
# window.resizable(True,False)

#screen attributes

print(window.winfo_screenwidth())
print(window.winfo_screenheight())

#window attributes
window.attributes('-alpha',1)
# window.attributes('-topmost',True)
# window.attributes('-disable',True)
# window.attributes('-fullscreen',1)

window.bind('<Escape>',lambda event : window.quit())
window.overrideredirect(True)

grip = ttk.Sizegrip(window)
grip.place(relx=.1,rely=1,anchor='se')
window.mainloop()
