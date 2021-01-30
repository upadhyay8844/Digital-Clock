import time
from tkinter import Label, Tk

# Tkinter function for the application window
app_window = Tk()
app_window.title("My Digital Time")
app_window.geometry("420x150")
app_window.resizable(0, 0)

# Designing the label
text_font = ("Boulder", 68, 'bold')
background = "#242221"
foreground = "#fc4103"
border_width = 25

# combining both
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)


# Digital Clock Function
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(300, digital_clock)


digital_clock()
app_window.mainloop()
