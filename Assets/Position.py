import tkinter as tk

# The library is now installed from the name code files!
import pyautogui

def update_position_label():
    mouse_position = pyautogui.position()
    position_label.config(text=f"{mouse_position.x}, {mouse_position.y}")
def copy_to_clipboard():
    mouse_position = pyautogui.position()
    root.clipboard_clear()
    root.clipboard_append(f"{mouse_position.x}, {mouse_position.y}")
    root.update()

root = tk.Tk()
root.title("Mouse Position Tracker")
position_label = tk.Label(root, text="", font=("Helvetica", 16))
position_label.pack(pady=10)
update_position_label() 
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)
def update_position():
    update_position_label()
    root.after(100, update_position)

root.after(100, update_position)
root.mainloop()