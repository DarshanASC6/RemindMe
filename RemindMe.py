import time
import ctypes  # An included library with Python install.   

tasks = input("Remind me to: ")
# Asks the user what they want to be reminded to do later on

x = tasks.split(", ")
# variable that splits up the string into multiple inputs

duration = float(input("How many minutes until I remind you? "))
# Asks the user how frequently they want to be reminded to do their task

if duration < 1:
    print("Reminding you to", x[0], "in", duration, "minutes")
# Basic grammer stuff because I'm picky. States both the reminder and how long until the reminder.

elif duration > 1:
    print("Reminding you to", x[0], "in", duration, "minutes")
# Basic grammer stuff because I'm picky. States both the reminder and how long until the reminder.

else:
    print("Reminding you to", x[0], "in", duration, "minutes")
# Basic grammer stuff because I'm picky. States both the reminder and how long until the reminder.


duration = duration * 60
# This converts duration from seconds to minutes

counter = 0
# Variable that counts the number of reminders printed

while 1 == 1:
    time.sleep(duration)
    # Waits for the user input amount of time
    
    ctypes.windll.user32.MessageBoxW(0, x[0], "RemindMe.py Reminder", 0)
    # Creates a popup message that won't go away until the user acknowledges it
    
    counter = counter + 1
    # Increases the number of reminders
    
    print("Reminders given to", x[0], ": ", counter)
    # Shows how many reminders have been given