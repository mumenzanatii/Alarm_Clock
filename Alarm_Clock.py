import time
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
from playsound import playsound
import pygame


def set_alarm():
    hour = hour_var.get()
    minute = minute_var.get()
    second = second_var.get()
    alarm_time = f"{hour:02}:{minute:02}:{second:02}"
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            playsound('/Users/macbookpro/Desktop/Sync Internship/Task1/alarm.wav')
            messagebox.showinfo(title="Alarm", message="Time's up!")
            break


app = tk.Tk()
app.title("Alarm Clock")

# Set window size and position
app.geometry("350x300+500+200")
app.configure(bg="#2f2f2f")

# Set fonts
title_font = Font(family="Helvetica", size=24, weight="bold")
label_font = Font(family="Helvetica", size=16)
entry_font = Font(family="Helvetica", size=20)
button_font = Font(family="Helvetica", size=16)

# Create title label
title_label = tk.Label(app, text="Alarm Clock",
                       font=title_font, fg="#ffffff", bg="#2f2f2f")
title_label.pack(pady=10)

# Create label for input fields
label = tk.Label(app, text="Set Alarm Time:",
                 font=label_font, fg="#ffffff", bg="#2f2f2f")
label.pack()

# Create dropdown menu for hours
hour_var = tk.StringVar(value="00")
hour_style = ttk.Style()
hour_style.configure("TMenubutton", font=entry_font, relief="flat")
hour_menu = ttk.OptionMenu(
    app, hour_var, *[f"{i:02}" for i in range(24)], style="TMenubutton")
hour_menu.pack(pady=10)

# Create dropdown menu for minutes
minute_var = tk.StringVar(value="00")
minute_style = ttk.Style()
minute_style.configure("TMenubutton", font=entry_font, relief="flat")
minute_menu = ttk.OptionMenu(
    app, minute_var, *[f"{i:02}" for i in range(60)], style="TMenubutton")
minute_menu.pack(pady=10)

# Create dropdown menu for seconds
second_var = tk.StringVar(value="00")
second_style = ttk.Style()
second_style.configure("TMenubutton", font=entry_font, relief="flat")
second_menu = ttk.OptionMenu(
    app, second_var, *[f"{i:02}" for i in range(60)], style="TMenubutton")
second_menu.pack(pady=10)

# Create button to set the alarm
input_frame = ttk.Frame(app, padding=(20, 40), style="My.TFrame")
input_frame.pack(fill="both", expand=True)

button = ttk.Button(app, text="Set Alarm", style="My.TButton",
                    command=set_alarm)
button.pack(pady=10)

app.mainloop()
