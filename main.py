from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20

repetitions = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text="Timer", fg= GREEN)
    check_label.config(text="")
    global repetitions
    repetitions = 0
    start_button.config(state="normal")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetitions
    repetitions +=1
    #tweaks
    start_button.config(state="disabled")
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

    short_break_min = SHORT_BREAK_MIN*60
    work_min = WORK_MIN*60
    long_break_min = LONG_BREAK_MIN*60

    if repetitions % 8 == 0:
        count_down(long_break_min)
        title_label.config(text="Break", fg=RED)
        window.bell()
    elif repetitions % 2 == 0:
        count_down(short_break_min)
        title_label.config(text="Break", fg=PINK)
        window.bell()
    else:
        count_down(work_min)
        title_label.config(text="Work", fg=GREEN)
        window.bell()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(repetitions/2)
        for _ in range (work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas
canvas = Canvas(width=205, height=230, highlightthickness=0, bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103,115, image=tomato_image)
timer_text = canvas.create_text(103,130,text="00:00",font= (FONT_NAME, 35, "bold"), fill= "white")
canvas.config()
canvas.grid(column=1, row=1)


#Labels

title_label=Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg= YELLOW)
title_label.grid(column=1, row=0)
check_label = Label(text=" ", fg= GREEN, bg=YELLOW, font=(FONT_NAME, 10))
check_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", font=(FONT_NAME,10),highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", font=(FONT_NAME,10),highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)



window.mainloop()