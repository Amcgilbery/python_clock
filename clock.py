from tkinter import Tk, Label
from time import strftime

def update_time():
    current_time = strftime("%a %B %-d, %Y %H:%M")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)


# Main window
root = Tk()
root.title("Digital Clock")

# Clock label
clock_label = Label(root, font=("Comic Sans MS", 50), background="teal", foreground="black")
clock_label.pack(anchor='center', expand=True)

# Start the clock
update_time()
root.mainloop()