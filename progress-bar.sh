#!/bin/bash

# Array of spinner characters
spinner=("|" "/" "-" "\\")

# Function to display the spinner
spin() {
  while true; do
    for i in "${spinner[@]}"; do
      echo -ne "\r$i" # Print the spinner character and stay on the same line
      sleep 0.1       # Wait for 0.1 second
    done
  done
}

# Start the spinner in the background
spin &

# Capture the spinner process ID (PID)
spinner_pid=$!

# Move cursor to the line below the spinner

# Example: simulate some work with a sleep command
sleep 5

# Kill the spinner process once done
kill $spinner_pid

# Move the cursor to a new line after the spinner stops
echo -ne "\rTask completed!\n"
