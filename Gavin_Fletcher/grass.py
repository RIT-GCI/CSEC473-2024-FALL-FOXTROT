#!/usr/bin/python
import subprocess
import time
import threading
import random
import os 
os.environ["DISPLAY"] = ":0"
def install_pynput():
    try:
        import pynput  
    except ModuleNotFoundError:
        subprocess.run(["apt", "install", "python3-pynput", "-y"])

install_pynput()

from pynput.keyboard import Key, Controller
from pynput import keyboard

def open_terminal_with_text(text):
    screen_width = 1920
    screen_height = 1080

    # Generate random coordinates for the terminal position
    random_x = random.randint(0, screen_width - 400)
    random_y = random.randint(0, screen_height - 300) 
    geometry = f"450x300+{random_x}+{random_y}"
    # Using a shell command that maintains the terminal open
    command = f'bash -c "echo \'{text}\'; read -p \'keep calm, touch some grass :)\'"'
    subprocess.Popen(['x-terminal-emulator', '-geometry', geometry, '-e', command])


def grass():
    ascii_grass = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣇⠀⣀⠀⠀⢀⣠⡶⢟⣩⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⢤⣤⣄⡀⠀⢀⡿⣿⣼⣻⢁⣴⠟⢥⣿⠟⠁⠀⠀⠀⠀⠀⠀⣄⠀⢠⣾⡏⢀⣠⣾⠆⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠻⣝⠳⣾⡇⣿⠃⣯⠞⠁⣰⡟⠁⠀⠀⠀⠀⠀⠀⢠⠀⢿⢧⣺⠉⣿⠞⣹⣏⣤⣶⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢷⠀⠁⠈⠐⠏⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡾⠌⠳⠀⠈⠀⠙⠁⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⣷⠀⠀⠀⠀⡄⠀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣾⡿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⡿⠀⢹⠀⢀⣴⡾⢻⡆⠀⢸⡿⣆⠀⠀⢀⣠⢀⣴⠞⣩⡾⣁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⢦⣄⢸⡇⠀⢸⣶⢿⡿⠀⡌⠳⠀⣼⠇⣿⢠⡼⣿⣿⡟⠁⢠⣟⣥⣼⡿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢶⣦⣌⣷⠙⢿⡇⠀⢸⠇⣿⣠⡾⠻⡕⣴⡏⠀⣽⠏⠀⣿⠋⠀⠀⣿⡟⢩⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠙⡇⠀⠀⠀⠈⠀⠹⠏⠀⠀⠙⠟⠀⠀⠀⠀⠀⠉⠀⠀⠀⠸⠷⣾⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣴⣄⠀⢰⡏⣸⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⢠⣧⠀⠀⢀⣀⠀⠀
⠀⢠⣿⠙⣦⡟⢠⣿⣿⢏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣶⣀⠀⠀⣿⢿⡄⣸⡿⣿⣤⡶⣿⠏⠀⠀
⣐⣟⢹⡆⠘⡇⢸⠟⣿⡼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡏⠛⢦⡏⠀⢻⠏⠀⣽⠛⢱⣿⣴⣷⠄
⠉⢻⡟⠓⠀⡇⠃⢸⡟⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣬⣧⡀⠀⠃⠀⠀⠀⠀⠁⠀⠀⠟⠿⠃⠀
⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠷⠶⠶⣬⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    open_terminal_with_text(ascii_grass)  # Open a terminal to show the grass message
    
def alert():
    # Alert for telling blue team to take a break
    print("Time to take a break!")
    
def on_press(key):
    if key == keyboard.Key.enter:
        grass()
        grass()
def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keep the listener running
    grass()
    
if __name__ == "__main__":
    main()
