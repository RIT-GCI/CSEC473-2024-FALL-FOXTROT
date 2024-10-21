#!/bin/bash
#Arianna Schwartz

# Trap SIGINT (Ctrl+C) and disable it
trap '' SIGINT

# Ghost ASCII art
ghost='
        .-.
   ..   `.
   :g g   :
   : o    `.
  :         ``.
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:.
       :              `.
        `.              `.     
          `.`.`.`---..,___`;.-*
'

# Function to print the ghost at a specific position in the given terminal
print_ghost() {
  local padding=$1
  local tty=$2  # tty is passed as an argument

  # Move the cursor to the top-left and clear the screen
  echo -e "\033[H\033[2J" > "$tty"

  # Move the cursor down to the desired padding
  for ((i = 0; i < padding; i++)); do
    echo "" > "$tty"
  done

  # Print the ghost
  echo "$ghost" > "$tty"
}

# Animation loop: Ghost flies up and down in each terminal
padding=0
direction=1
loops=0
max_padding=10  # Maximum movement range

while [[ $loops -lt 20 ]]; do
  # Loop through all open terminal ttys
  for tty in /dev/pts/*; do
    # Print the ghost with variable padding in each terminal
    print_ghost "$padding" "$tty"
  done

  # Control the "floating" motion by changing padding
  if [[ $padding -ge $max_padding ]]; then
    direction=-1
  elif [[ $padding -le 0 ]]; then
    direction=1
  fi

  padding=$((padding + direction))
  
  # Wait to make the animation visible
  sleep 0.2

  # Increment the number of loops
  ((loops++))
done

# Ghost speaks before closing the terminal
for tty in /dev/pts/*; do
  echo -e "\033[H\033[2J" > "$tty"  # Fully clear the terminal
  echo "$ghost" > "$tty"
  echo "" > "$tty"
  echo "Watch me make this terminal...disappear" > "$tty"
done

# Wait a few seconds to read the message
sleep 1.5

# Close the terminals by killing their processes (for each tty)
for tty in /dev/pts/*; do
  PARENT_PID=$(ps -t "$tty" -o ppid= | head -n 1)  # Get the parent process ID for each tty
  if [[ ! -z "$PARENT_PID" ]]; then
    kill -9 "$PARENT_PID"  # Kill the terminal process
  fi
done
