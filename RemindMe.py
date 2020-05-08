import time
import ctypes  # An included library with Python install.   

tasks = input("Remind me to: ")
# Asks the user what they want to be reminded to do later on

x = tasks.split(", ")
# variable that splits up the string into multiple inputs

num_tasks = int(len(x) - 1)
# variable that counts the number of tasks

for i in x:
    duration = float(input("How many minutes until I remind you? "))
    # Asks the user how frequently they want to be reminded to do their task

    if duration < 1:
        print("Reminding you to", x[num_tasks], "in", duration, "minutes")
    # Basic grammer stuff because I'm picky. States both the reminder and how long until the reminder.

    elif duration > 1:
        print("Reminding you to", x[num_tasks], "in", duration, "minutes")
    # Basic grammer stuff because I'm picky. States both the reminder and how long until the reminder.

    else:
        print("Reminding you to", x[num_tasks], "in", duration, "minute")
    # Basic grammer stuff because I'm picky. States both the reminder and how long until the reminder.

    num_tasks = num_tasks - 1

duration = duration * 60
# This converts duration from seconds to minutes

counter = 0
# Variable that counts the number of reminders printed

for p in x:
    num_tasks = int(len(x) - 1)
    
    time.sleep(duration)
    # Waits for the user input amount of time
    
    ctypes.windll.user32.MessageBoxW(0, x[num_tasks], "RemindMe.py Reminder", 0)
    # Creates a popup message that won't go away until the user acknowledges it
    
    counter = counter + 1
    # Increases the number of reminders
    
    print("Reminders given to", x[num_tasks], ":", counter)
    # Shows how many reminders have been given
    num_tasks = num_tasks - 1
    if num_tasks == 0:
        num_tasks = int(len(x) - 1)