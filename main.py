from tkinter import *
from tkinter import ttk
from tkinter.font import Font

root = Tk()
root.title("Stephen Typing Test")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)

ipsum_lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore" \
              " et dolore magna aliqua. Eu feugiat pretium nibh ipsum consequat nisl vel. Nisl pretium fusce id " \
              "velit. Curabitur gravida arcu ac tortor. Sagittis nisl rhoncus mattis rhoncus urna neque. Amet nulla" \
              " facilisi morbi tempus. Ut sem nulla pharetra diam sit amet. Suscipit adipiscing bibendum est " \
              "ultricies. Ac auctor augue mauris augue neque gravida in fermentum. Ante metus dictum at tempor " \
              "commodo ullamcorper a lacus. Sit amet mauris commodo quis massa. Id faucibus nisl tincidunt" \
              " eget nullam. Augue mauris augue neque gravida in fermentum. Sem integer vitae justo eget magna " \
              "fermentum iaculis. Placerat in egestas erat imperdiet sed euismod nisi porta lorem. Est ullamcorper " \
              "eget nulla facilisi etiam dignissim diam quis enim. Faucibus ornare suspendisse sed nisi lacus sed. " \
              "In tellus integer feugiat scelerisque varius morbi enim. Morbi tempus iaculis urna id volutpat " \
              "lacus laoreet non."

# ==============Fonts=============================== #
heading_font = Font(family="Luminari", size=30, weight="bold", slant="italic", underline=1)
start_font = Font(family="Luminrari", size=20, weight="bold")
words_font = Font(family="Luminrari", size=11, weight="normal")

# ==============UI Design========================== #
app_header = ttk.Label(main_frame, text="TEST YOUR TYPING SPEED", anchor="center", font=heading_font)
app_header.grid(row=0, column=0)

start_label = ttk.Label(main_frame, text="Click >>>Here<<< To Start", anchor="center", font=start_font, padding=20)
start_label.grid(row=1, column=0)

words_label = ttk.Label(main_frame, text=ipsum_lorem, font=words_font, padding=10, relief="groove", wraplength=550)
words_label.grid(row=2, column=0)

# user_entry = ttk.Entry(main_frame, text=ipsum_lorem, font=words_font, width=70)
# user_entry.grid(row=3, column=0)

user_text = Text(main_frame, height=15, width=70)
user_text.grid(row=3, column=0)





root.mainloop()
