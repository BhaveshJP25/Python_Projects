from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("370x110")
app_window.resizable(0,0)
app_window.configure(background="black")

text_font = ('digital-7', 68,)
foreground = "#FFFFFF"

label = Label(app_window, font=text_font, bg='white', fg='orange')
label.grid(row=0, column=0)

def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live, background='black')
   label.after(1000, digital_clock)

digital_clock()
app_window.mainloop()