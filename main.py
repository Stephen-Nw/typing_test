import random
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from wpm_functions import wpm_calculation
from samples_and_report import samples, result_analysis, instructions

root = Tk()
root.title("Stephen Typing Test")
main_frame = ttk.Frame(root, padding=10, width=950, height=350)
main_frame.grid(row=0, column=0)
counter_frame = ttk.Frame(root, padding=5, width=950, height=350)
counter_frame.grid(row=1, column=0)

counter = 0
phrase_to_type = random.choice(samples)
instruction = instructions()


# ============================FUNCTIONS==================================#
def countdown_time():
    """timer that increments every second"""
    global counter
    timer_label.config(text=f"Time: {counter} secs")
    timer_label.after(1000, countdown_time)
    counter += 1
    return counter


def start_typing():
    """Creates initial label containing text for user to type and entry where user types"""
    def words_per_minute(event):
        """Calculates user wpm while typing"""
        word_length = len(user_text.get("1.0", "end-2c"))
        word_per_min = wpm_calculation(word_length, counter)
        wpm_label.config(text=f"WPM: {word_per_min}")

    def final_word_per_min_calculation(event):
        """Calculate final wpm after user hits Return. Destroys other widgets and creates a new result
        widget with user summary"""
        final_word_length = len(user_text.get("1.0", "end-2c"))  # end-2c removes 2 xters at end of text
        final_word_per_min = wpm_calculation(final_word_length, counter)

        words_label.destroy()
        user_text.destroy()
        timer_label.destroy()
        wpm_label.destroy()

        results = result_analysis(counter, final_word_length, final_word_per_min)
        results_label = ttk.Label(counter_frame, text=results, padding=10, relief="solid", width=75, justify="left")
        results_label.grid(row=0, column=0)

    global counter
    start_button.destroy()
    instruction_label.destroy()
    countdown_time()

    secondary_frame = ttk.Frame(root, padding=10, width=950, height=350)
    secondary_frame.grid(row=3, column=0)

    words_label = ttk.Label(main_frame, text=phrase_to_type, font=words_font, padding=5, relief="solid",
                            wraplength=550)
    words_label.grid(row=2, column=0, columnspan=4)

    user_text = Text(secondary_frame, height=10, width=70, relief="solid")
    user_text.grid(row=0, column=0, columnspan=4)
    user_text.focus()  # Set cursor in entry field

    user_text.bind_all('<Key-Return>', final_word_per_min_calculation)
    user_text.bind_all('<KeyPress-a>', words_per_minute)
    user_text.bind_all('<KeyPress-o>', words_per_minute)
    user_text.bind_all('<KeyPress-i>', words_per_minute)
    user_text.bind_all('<KeyPress-u>', words_per_minute)
    user_text.bind_all('<KeyPress-f>', words_per_minute)


# ==============FONTS=============================== #
heading_font = Font(family="Helvetica", size=25, weight="bold", slant="italic", underline=1)
start_font = Font(family="Helvetica", size=20, weight="bold")
words_font = Font(family="Helvetica", size=11, weight="normal")

# ==============UI DESIGN========================== #
app_header = ttk.Label(main_frame, text="TEST YOUR TYPING SPEED", anchor="center", font=heading_font, padding=5)
app_header.grid(row=0, column=0, columnspan=4)

instruction_label = ttk.Label(main_frame, text=instruction, anchor="ne", font=words_font, padding=5,
                              wraplength=550, relief="solid")
instruction_label.grid(row=1, column=0, columnspan=4, pady=10)

start_button = ttk.Button(main_frame, text=">>>Click To Start<<<", command=start_typing)
start_button.grid(row=2, column=1)

timer_label = ttk.Label(counter_frame, text="Timer: ", anchor="nw", width=70)
timer_label.grid(row=1, column=0)

wpm_label = ttk.Label(counter_frame, text="wpm: ", anchor="nw")
wpm_label.grid(row=1, column=2)


root.mainloop()
