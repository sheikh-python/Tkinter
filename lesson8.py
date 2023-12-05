import tkinter as tk
from tkinter import ttk


# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

#canvas 
canvas = tk.Canvas(window , bg='white')
canvas.pack()
#(left , top , right , bottom)
# canvas.create_rectangle(50,20,100,200,
#                         fill='green',width=5 ,
#                         dash=(200,150,1,1),
#                         outline='red')
# canvas.create_oval((200,5,300,100),
#                    fill='red',
#                    width=2,
#                 )
# canvas.create_arc((200,5,300,100),fill='green',start = 45 ,
#                   extent = 87 ,outline='green',width=5,
#                   style =tk.CHORD )

# canvas.create_line((0,0, 100 , 150 ),fill='blue',width=10)
# canvas.create_polygon((20,20 , 100 , 200 , 150 ,150 ),fill='gray')
# canvas.create_text((100,200),text='this is some text')
# canvas.create_window((150,100),window=ttk.Button(window,text='this is text in a canvas'))

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x-brush_size/2 , y- brush_size/2 , x+brush_size/2 , y+brush_size/2),fill='black')
def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size+=4
    else:
        brush_size -=4
        
    brush_size = max(0,min(brush_size, 50))
    print(event)
brush_size = 2
canvas.bind('<Motion>',draw_on_canvas)
canvas.bind('<MouseWheel>',brush_size_adjust)


window.mainloop()