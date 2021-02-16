from tkinter import *
import calendar

def showCalender():
    gui = Tk()
    gui.config(background='white')
    gui.title("Calender for the year")
    gui.geometry("600x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=0, column=0, padx=50, pady=20)
    gui.mainloop()

if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calender")
    new.geometry("350x140")
    cal = Label(new, text="Calender", bg='grey', font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field = Entry(new)
    button = Button(new, text='Show Calender', fg="Black", bg='green', command=showCalender)

    #putting widgets in position
    cal.grid(row=1, column=1, pady=4)
    year.grid(row=2, column=1, pady=4)
    year_field.grid(row=2, column=2, pady=4)
    button.grid(row=3, column=2, pady=4)
    # Exit.grid(row=6, column=1)
    new.mainloop()