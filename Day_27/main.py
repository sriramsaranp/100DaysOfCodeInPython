from tkinter import *

window = Tk()
window.title("Mile to Km Conerter")
window.minsize(width="250" , height= "150")
window.config(padx= 20, pady = 20)


input = Entry()
input.grid(column= 1, row= 0)

my_label = Label(text= "Miles", font= ("Arial", 15))
my_label.grid(column=2, row = 0)

new_label = Label(text="is equal to", font=("Arial",15))
new_label.grid(column= 0, row = 2)

my_label = Label(text= "Km", font= ("Arial", 15))
my_label.grid(column=2, row = 1)

answer = Label()
answer.grid(column= 1, row = 1)

def button_clicked():
    miles = input.get()
    km = int(miles)*1.609
    answer.config(text= f"{int(km)}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row= 2)




window.mainloop()