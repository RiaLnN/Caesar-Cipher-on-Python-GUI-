
import tkinter as tk


def encryption(text, shift):
    result = ""
    for letter in text:
        if "A" <= letter <= "Z":
            shifted = chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
            result += shifted
        elif "a" <= letter <= "z":
            shifted = chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
            result += shifted
        else:
            result += letter
    return result


def decryption(text, shift):
    return encryption(text, -shift)


def on_encrypt():
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get("1.0", "end-1c"))
        result = encryption(text, shift)
        output_text.config(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", result)
        output_text.config(state="disabled")
    except ValueError:
        output_text.config(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "Shift must be a number")
        output_text.config(state="disabled")

def on_decrypt():
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get("1.0", "end-1c"))
        result = decryption(text, shift)
        output_text.config(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", result)
        output_text.config(state="disabled")
    except ValueError:
        output_text.config(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "Shift must be a number")
        output_text.config(state="disabled")



root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x300")


tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack()
input_text = tk.Text(root, height=3, font=("Arial", 12))
input_text.pack()


tk.Label(root, text="Enter Shift:", font=("Arial", 12)).pack()
shift_entry = tk.Text(root, height=1, font=("Arial", 12))
shift_entry.pack()


tk.Button(root, text="Encrypt", command=on_encrypt, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Decrypt", command=on_decrypt, font=("Arial", 12)).pack(pady=5)


tk.Label(root, text="Result:", font=("Arial", 12)).pack()
output_text = tk.Text(root, height=3, font=("Arial", 12))
output_text.pack()

root.mainloop()

