import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk

def enter(val):
    global flag
    if flag == False:
        entry.delete(0, "end")
        new = str(val)
        entry.insert(0, new)
        flag = True
    else:
        current = entry.get()
        if val == '=':
            new = eval(current)
            flag = False
        else:
            new = current + str(val)
        entry.delete(0, "end")
        entry.insert(0, new)

flag = True


#Initialising window
root = tk.Tk()
icon = Image.open('Icon.jpg')
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False, photo)      
root.configure(background = 'Black')
root.title("Calculator")


#Entry field
entry = Entry(root, width=37, background='Blue', font='Arial')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


#Buttons (numbers)
#1st row
button_7 = tk.Button(root, text='7', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(7))
button_7.grid(row=1, column=0, padx = 2, pady = 2)

button_8 = tk.Button(root, text='8', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(8))
button_8.grid(row=1, column=1, padx = 2, pady = 2)

button_9 = tk.Button(root, text='9', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(9))
button_9.grid(row=1, column=2, padx = 2, pady = 2)


#2nd row
button_4 = tk.Button(root, text='4', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(4))
button_4.grid(row=2, column=0, padx = 2, pady = 2)

button_5 = tk.Button(root, text='5', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(5))
button_5.grid(row=2, column=1, padx = 2, pady = 2)

button_6 = tk.Button(root, text='6', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(6))
button_6.grid(row=2, column=2, padx = 2, pady = 2)


#3rd row
button_1 = tk.Button(root, text='1', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(1))
button_1.grid(row=3, column=0, padx = 2, pady = 2)

button_2 = tk.Button(root, text='2', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(2))
button_2.grid(row=3, column=1, padx = 2, pady = 2)

button_3 = tk.Button(root, text='3', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(3))
button_3.grid(row=3, column=2, padx = 2, pady = 2)
        

#Button 0
button_0 = tk.Button(root, text='0', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter(0))
button_0.grid(row=4, column=0, padx = 2, pady = 2)


#Buttons (functionality)
button_div = tk.Button(root, text='/', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter('/'))
button_div.grid(row=1, column=3, padx = 2, pady = 2)
        
button_mult = tk.Button(root, text='x', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter('*'))
button_mult.grid(row=2, column=3, padx = 2, pady = 2)
        
button_sub = tk.Button(root, text='-', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter('-'))        
button_sub.grid(row=3, column=3, padx = 2, pady = 2)

button_add = tk.Button(root, text='+', width=5, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter('+'))
button_add.grid(row=4, column=3, padx = 2, pady = 2)
        
button_eq = tk.Button(root, text='=', width=11, height=2, font=("Arial Black", 20), background='#2b2b2b', foreground='White', command=lambda: enter('='))
button_eq.grid(row=4, column=1, padx = 2, pady = 2, columnspan=2)
        
               
#MainLoop
root.mainloop()

