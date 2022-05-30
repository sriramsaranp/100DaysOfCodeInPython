from cgitb import text
from itertools import count
from math import floor
from tabnanny import check
from tkinter import *
from turtle import xcor

from numpy import pad, place
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = .05
LONG_BREAK_MIN = .2
reps = 0   
timer = None 

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text = "00:00")
    my_label.config(text= "Timer" , fg= GREEN)
    checkmark.config(text= "")

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_time_sec = WORK_MIN * 60
    short_time_sec = SHORT_BREAK_MIN * 60
    long_time_sec = LONG_BREAK_MIN * 60

    value = reps % 8
    if value == 0:
        my_label.config(text="Break", fg= RED)
        count_down(long_time_sec)    
    elif reps % 2 == 0:
        my_label.config(text="Break", fg= PINK)
        count_down(short_time_sec)
    else:
        my_label.config(text="Work Time", fg= GREEN)
        count_down(work_time_sec)
 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    global timer,reps
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else :
        start_timer()
        mark = ""
        if reps % 7 == 0:
            checkmark.config(text = "")
            mark = ""
        else :
            for n in range(int(reps/2)):
                mark += "✔"
            checkmark.config(text= mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 80, pady= 40, bg= YELLOW)

my_label = Label(text= "TIMER", fg= GREEN, font= (FONT_NAME, 35, "bold") , bg= YELLOW)
my_label.grid(column= 1, row = 0)

canvas = Canvas(width= 300, height= 250, bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150,125, image = tomato_img)
timer_text = canvas.create_text(150, 150, text= "00:00", fill="white", font=(FONT_NAME, 30, 'bold'))
canvas.grid(column= 1, row= 1)

start = Button(text= "Start", command= start_timer)
start.grid(column= 0, row = 2)

end = Button(text = "Reset", command= reset_timer)
end.grid(column= 2, row = 2)

checkmark = Label(fg= GREEN, bg= YELLOW)
checkmark.grid(column= 1, row = 3)



window.mainloop()   