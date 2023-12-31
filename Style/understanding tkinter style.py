import tkinter as tk
from tkinter import ttk, font

# Window
window = tk.Tk()
window.title("Styling test")
window.geometry("400x300")
# style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use('alt')
style.configure("new.TButton", foreground="blue", background='blue', font=('kalameh', 20))
style.map('new.TButton',
          foreground=[('pressed', 'red'), ('disabled', 'green')],
          background=[('pressed', 'black'), ('disabled', 'white')]
          )
# widget
label = ttk.Label(window,
                  text=' سلام به همگی \n  من احمد شیخ زاده هستم',
                  background='red',
                  foreground='white',
                  font=('kalameh', 20),
                  justify='right',
                  )
label.pack()

button = ttk.Button(master=window, text='A button', style='new.TButton')
button.pack()

# run
window.mainloop()
