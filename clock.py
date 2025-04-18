from tkinter import Tk, Label, Canvas
from time import strftime
from tkinter.font import Font

def update_time():
    current_time = strftime("%a %B %-d, %Y %H:%M")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

def resize_elements(event):
    # Calculate optimal font size based on current window
    width = event.width
    height = event.height

    new_size = min(width // 20, height // 6)
    new_size = max(new_size, 10)
    if font['size'] != new_size:
        font.configure(size=new_size)

# Main window
root = Tk()
root.title("Anthony's Clock")
root.geometry("800x400")
root.minsize(300, 150)
root.resizable(True, True)

# Create a canvas as background
canvas = Canvas(root, bg="grey", highlightthickness=0)
canvas.pack(fill='both', expand=True)

# Set up resizable font
font = Font(family="Helvetica", size=50)

# Clock label centered
clock_label = Label(canvas, font=font, background="teal", foreground="black")
clock_label.place(relx=0.5, rely=0.5, anchor='center')

# Bind resize event
canvas.bind("<Configure>", resize_elements)

# Start the clock
update_time()
root.mainloop()
