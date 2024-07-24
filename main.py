import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
rep = 1
second_waiter = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global rep
    window.after_cancel(second_waiter)
    canvas.itemconfig(countdown_text, text=f"00:00")
    rep = 1
    timer_label.config(text="TIMER", fg=GREEN)
    checkboxes_label["text"] = ""




# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_work_timer():
    global rep
    if rep % 8 == 0:
        time = LONG_BREAK_MIN * 60
        timer_label.config(text="Break", fg=RED)

    elif rep % 2 == 0:
        time = SHORT_BREAK_MIN * 60
        timer_label.config(text="Break", fg=PINK)
    else:
        time = WORK_MIN * 60
        timer_label.config(text="Work", fg=GREEN)

    countdown(time)
    rep += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global rep
    global second_waiter
    mins = math.floor(count / 60)
    secs = count - (mins * 60)
    if secs < 10:
        secs = f"0{secs}"

    if count >= 0:

        second_waiter = window.after(1000, countdown, count - 1)
        canvas.itemconfig(countdown_text, text=f"{mins}:{secs}")
    else:
        start_work_timer()
        if rep % 2 != 0:
            checkboxes_label["text"] = checkboxes_label["text"] + "✓"


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
canvas = tkinter.Canvas(width=400, height=448, bg=YELLOW, highlightthickness=0)

tomato_img = tkinter.PhotoImage(file="clock.png")
canvas.create_image(200, 224, image=tomato_img)
countdown_text = canvas.create_text(200, 224, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="TIMER", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_work_timer)
start_button.grid(column=1, row=3)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=3, row=3)

checkboxes_label = tkinter.Label(text="", font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
checkboxes_label.grid(column=2, row=4)

window.mainloop()
