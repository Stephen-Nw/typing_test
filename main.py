from tkinter import *
from tkinter import ttk
from tkinter.font import Font

root = Tk()
root.title("Stephen Typing Test")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

heading_font = Font(family="Luminari", size=35, weight="bold", slant="italic", underline=1)

# ==============UI Design========================== #

app_header = ttk.Label(main_frame, text="TEST YOUR TYPING SPEED", anchor="center", font=heading_font)
app_header.grid(row=1, column=1)




root.mainloop()
