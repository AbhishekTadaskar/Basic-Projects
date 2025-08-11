# DIGITAL CLOCK #

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="black") 

def time():
    string = strftime('%H:%M:%S %p\n%A, %d %B %Y')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(
    root, 
    font=("Helvetica", 48, "bold"), 
    background="black", 
    foreground="light green",  
    pady=20
)
label.pack(anchor="center", expand=True)

time()
root.mainloop()
