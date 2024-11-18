import tkinter as tk
from crypto import *

def toggle_frame():
    if encryption_frame.winfo_ismapped():
        decryption_frame.grid(row=0, column=0, sticky='nsew')
        encryption_frame.grid_forget()
        toggle_button.config(text="Switch to Encryption")
    else:
        encryption_frame.grid(row=0, column=0, sticky='nsew')
        decryption_frame.grid_forget()
        toggle_button.config(text="Switch to Decryption")

#triggers when the encrypt button is pressed
def encrypt_button_pressed():
    password = recipient_public_key_entry.get()
    data = encryption_entry.get()
    encrypted_text = encrypt(data, password)
    encrypted_text_entry.delete(0, tk.END)
    encrypted_text_entry.insert(0, encrypted_text)

#triggers when the decrypt button is pressed
def decrypt_button_pressed():
    password = private_key_entry.get()
    token = decryption_entry.get()
    decrypted_text = decrypt(token, password)
    decrypted_text_entry.delete(0, tk.END)
    decrypted_text_entry.insert(0, decrypted_text)
    

window = tk.Tk()
window.title('Encryption Tool')
window.geometry("500x400")

encryption_frame = tk.Frame(window)
decryption_frame = tk.Frame(window)

toggle_button = tk.Button(window, text="Switch to Decryption", command=toggle_frame)
toggle_button.grid(row=1, column=0, columnspan=2)

# Encryption Frame
tk.Label(encryption_frame, text="Password: ").grid(row=1, column=0)
recipient_public_key_entry = tk.Entry(encryption_frame, width=30)
recipient_public_key_entry.grid(row=1, column=1)

tk.Label(encryption_frame, text="Message to Encrypt: ").grid(row=2, column=0)
encryption_entry = tk.Entry(encryption_frame, width=30)
encryption_entry.grid(row=2, column=1)

encrypt_button = tk.Button(encryption_frame, text="Encrypt", command=encrypt_button_pressed)
encrypt_button.grid(row=3, column=0, columnspan=2)
encryption_result_label = tk.Label(encryption_frame, text="Encrypted Text:")
encryption_result_label.grid(row=4, column=0, sticky='e')
encrypted_text_entry = tk.Entry(encryption_frame, width=30)
encrypted_text_entry.grid(row=4, column=1, sticky='w')


# Decryption Frame
tk.Label(decryption_frame, text="Password: ").grid(row=0, column=0)
private_key_entry = tk.Entry(decryption_frame, width=30)
private_key_entry.grid(row=0, column=1)

tk.Label(decryption_frame, text="Encrypted Message: ").grid(row=1, column=0)
decryption_entry = tk.Entry(decryption_frame, width=30)
decryption_entry.grid(row=1, column=1)

decrypt_button = tk.Button(decryption_frame, text="Decrypt", command=decrypt_button_pressed)
decrypt_button.grid(row=2, column=0, columnspan=2)
decryption_result_label = tk.Label(decryption_frame, text="Decrypted Text: ")
decryption_result_label.grid(row=4, column=0, sticky='e')
decrypted_text_entry = tk.Entry(decryption_frame, width=30)
decrypted_text_entry.grid(row=4, column=1, sticky='w')

# Initially display the encryption frame
encryption_frame.grid(row=0, column=0, sticky='nsew')


