from tkinter import *
from tkinter import ttk
from tkinter.font import Font

root = Tk()
root.title("Stephen Typing Test")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)
secondary_frame = ttk.Frame(root, padding=10, width=950, height=350)
secondary_frame.grid(row=2, column=0)
tertiary_frame = ttk.Frame(root, padding=10, width=950, height=350)
tertiary_frame.grid(row=3, column=0)


def start_typing():
    pass


results = "Well done!! Your typing speed is ____ words per minute!! \n\n" \
          "You made ___ mistakes in your typing\n\n" \
          "The mistakes you made are: "

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
app_header = ttk.Label(main_frame, text="TEST YOUR TYPING SPEED", anchor="center", font=heading_font, padding=15)
app_header.grid(row=0, column=0, columnspan=4)

# start_label = ttk.Label(main_frame, text="Click", anchor="center", font=start_font, padding=10)
# start_label.grid(row=1, column=0)

start_button = ttk.Button(main_frame, text=">>>Click To Start<<<", command=start_typing)
start_button.grid(row=1, column=1)

words_label = ttk.Label(main_frame, text=ipsum_lorem, font=words_font, padding=10, relief="solid", wraplength=550)
words_label.grid(row=2, column=0, columnspan=4)

user_text = Text(secondary_frame, height=10, width=70, relief="solid")
user_text.grid(row=0, column=0, columnspan=4)

timer_label = ttk.Label(secondary_frame, text="timer: placeholder", anchor="nw", width=60, padding=(0, 10))
timer_label.grid(row=1, column=0)

wpm_label = ttk.Label(secondary_frame, text="wpm: placeholder", anchor="nw")
wpm_label.grid(row=1, column=2)

results_label = ttk.Label(tertiary_frame, text=results, padding=10, relief="solid", width=75, justify="left")
results_label.grid(row=0, column=0)

root.mainloop()
