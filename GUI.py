import tkinter as tk

def toggle_frame():
    if encryption_frame.winfo_ismapped():
        decryption_frame.grid(row=0, column=0, sticky='nsew')
        encryption_frame.grid_forget()
        toggle_button.config(text="Switch to Encryption")
    else:
        encryption_frame.grid(row=0, column=0, sticky='nsew')
        decryption_frame.grid_forget()
        toggle_button.config(text="Switch to Decryption")

window = tk.Tk()
window.title('Encryption Tool')
window.geometry("500x400")

encryption_frame = tk.Frame(window)
decryption_frame = tk.Frame(window)

toggle_button = tk.Button(window, text="Switch to Decryption", command=toggle_frame)
toggle_button.grid(row=1, column=0, columnspan=2)

tk.Label(encryption_frame, text="Encryption - Statement:").grid(row=0, column=0)
encryption_entry = tk.Entry(encryption_frame, width=30)
encryption_entry.grid(row=0, column=1)
encrypt_button = tk.Button(encryption_frame, text="Encrypt")
encrypt_button.grid(row=1, column=0, columnspan=2)
encryption_result_label = tk.Label(encryption_frame, text="Encrypted Text: ")
encryption_result_label.grid(row=2, column=0, columnspan=2)

tk.Label(decryption_frame, text="Decryption - Statement:").grid(row=0, column=0)
decryption_entry = tk.Entry(decryption_frame, width=30)
decryption_entry.grid(row=0, column=1)
decrypt_button = tk.Button(decryption_frame, text="Decrypt")
decrypt_button.grid(row=1, column=0, columnspan=2)
decryption_result_label = tk.Label(decryption_frame, text="Decrypted Text: ")
decryption_result_label.grid(row=2, column=0, columnspan=2)

encryption_frame.grid(row=0, column=0, sticky='nsew')

window.mainloop()
