import customtkinter as ctk


# window
window = ctk.CTk()
window.title('customtkinter app')
window.geometry('600x400')

# widget
label = ctk.CTkLabel(window,
                     text='A ctk label',
                     fg_color=('blue', 'red'),
                     text_color='white',
                     corner_radius=10)
label.pack()

button = ctk.CTkButton(window,
                       text='A ctk button',
                       fg_color='#FF0',
                       text_color='#000',
                       hover_color='#AA0',
                       command=lambda: ctk.set_appearance_mode('light'))

button.pack()

frame = ctk.CTkFrame(window)
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx=20, pady=20)

# run
window.mainloop()
