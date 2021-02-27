from tkinter import *
from tkmacosx import Button
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FBDCE2"
RED = "#EE6352"
GREEN = "#9CD08F"
PURPLE = "#685155"
FONT_NAME = "Futura"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# starting from count input
# counts down by 1 every second (1000ms)
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # change timer using canvas itemconfig method
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

# create window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)


# setup canvas
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=PURPLE, bg=PINK, font=(FONT_NAME, 45, "normal"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", borderless=1, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", borderless=1)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=PURPLE, bg=PINK, font=(FONT_NAME, 20, "normal"))
check_marks.grid(column=1, row=3)

window.mainloop()