import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import urllib.parse

# AES256 키와 IV 준비
key = b''  # 256비트 키
iv = b''  # 128비트 IV

def encrypt():
    plaintext = entry_plaintext.get()
    if not plaintext:
        messagebox.showwarning("Input Error", "Please enter text to encrypt.")
        return
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    ciphertext_encoded = base64.b64encode(ciphertext)
    ciphertext_url_encoded = urllib.parse.quote(ciphertext_encoded)
    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, ciphertext_url_encoded)

def decrypt():
    ciphertext_url_encoded = entry_ciphertext.get()
    if not ciphertext_url_encoded:
        messagebox.showwarning("Input Error", "Please enter text to decrypt.")
        return
    try:
        ciphertext_decoded = base64.b64decode(urllib.parse.unquote(ciphertext_url_encoded))
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext_decoded), AES.block_size)
        entry_plaintext.delete(0, tk.END)
        entry_plaintext.insert(0, plaintext.decode('utf-8'))
    except (ValueError, KeyError) as e:
        messagebox.showerror("Decryption Error", str(e))

# GUI 설정
root = tk.Tk()
root.title("AES256 Encrypt/Decrypt Tool")

tk.Label(root, text="Plaintext:").grid(row=0, column=0, padx=10, pady=10)
entry_plaintext = tk.Entry(root, width=100)
entry_plaintext.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Ciphertext:").grid(row=1, column=0, padx=10, pady=10)
entry_ciphertext = tk.Entry(root, width=100)
entry_ciphertext.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Encrypt", command=encrypt).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Decrypt", command=decrypt).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()