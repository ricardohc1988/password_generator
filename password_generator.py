import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_var.get())
    
    # Define possible characters based on user selection
    characters = ''
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation
    
    # Check if at least one character set is selected
    if not characters:
        messagebox.showwarning("Warning", "Please select at least one character set")
        return

    # Ensure at least one character from each selected set is included
    password_chars = []
    if uppercase_var.get():
        password_chars.append(random.choice(string.ascii_uppercase))
    if lowercase_var.get():
        password_chars.append(random.choice(string.ascii_lowercase))
    if numbers_var.get():
        password_chars.append(random.choice(string.digits))
    if symbols_var.get():
        password_chars.append(random.choice(string.punctuation))
    
    # Fill the rest of the password length with random choices from the selected characters
    while len(password_chars) < password_length:
        password_chars.append(random.choice(characters))
    
    # Shuffle the password characters to ensure randomness
    random.shuffle(password_chars)
    
    # Create the final password string
    password = ''.join(password_chars)
    password_entry.delete(0, ctk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())
    messagebox.showinfo("Info", "Password copied to clipboard")

# Create the main window
window = ctk.CTk()
window.title("Password Generator")
window.geometry("400x400")
window.resizable(False, False)
ctk.set_appearance_mode("dark")

# Main frame to hold everything
main_frame = ctk.CTkFrame(window)
main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Label and entry for password length
length_frame = ctk.CTkFrame(main_frame)
length_frame.pack(pady=10)

length_label = ctk.CTkLabel(length_frame, text="Password length:")
length_label.pack(side=tk.LEFT, padx=10)

length_var = ctk.StringVar(value="8")
length_options = [str(i) for i in range(4, 21)]  # Options from 4 to 20
length_menu = ctk.CTkOptionMenu(length_frame, variable=length_var, values=length_options, width=80)
length_menu.pack(side=tk.RIGHT, padx=10)

# Frame for checkboxes
checkbox_frame = ctk.CTkFrame(main_frame)
checkbox_frame.pack(pady=10)

# Label for character set options
include_label = ctk.CTkLabel(checkbox_frame, text="Include:")
include_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky='w')

# Checkboxes for character sets
uppercase_var = ctk.BooleanVar()
uppercase_check = ctk.CTkCheckBox(checkbox_frame, text="Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, padx=10, pady=5, sticky='w')

lowercase_var = ctk.BooleanVar()
lowercase_check = ctk.CTkCheckBox(checkbox_frame, text="Lowercase Letters", variable=lowercase_var)
lowercase_check.grid(row=1, column=1, padx=10, pady=5, sticky='w')

numbers_var = ctk.BooleanVar()
numbers_check = ctk.CTkCheckBox(checkbox_frame, text="Numbers", variable=numbers_var)
numbers_check.grid(row=2, column=0, padx=10, pady=5, sticky='w')

symbols_var = ctk.BooleanVar()
symbols_check = ctk.CTkCheckBox(checkbox_frame, text="Symbols", variable=symbols_var)
symbols_check.grid(row=2, column=1, padx=10, pady=5, sticky='w')

# Entry to display the generated password
password_entry = ctk.CTkEntry(main_frame, width=200, justify="center")
password_entry.pack(pady=10, fill=tk.X, padx=20)

# Buttons
button_frame = ctk.CTkFrame(main_frame)
button_frame.pack(pady=10)

generate_button = ctk.CTkButton(button_frame, text="Generate Password", command=generate_password)
generate_button.pack(side=tk.LEFT, padx=10)

copy_button = ctk.CTkButton(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=10)

# Start the event loop
window.mainloop()
