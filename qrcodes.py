import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

def on_generate_button_click():
    url = url_entry.get()
    generate_qr_code(url)
    show_qr_code()

def show_qr_code():
    img = Image.open("qrcode.png")
    img.thumbnail((200, 200))
    img_tk = ImageTk.PhotoImage(img)

    qr_code_label.config(image=img_tk)
    qr_code_label.image = img_tk


root = tk.Tk()
root.title("URL to QR Code Converter")

url_label = ttk.Label(root, text="Enter URL:")
url_entry = ttk.Entry(root, width=30)
generate_button = ttk.Button(root, text="Generate QR Code", command=on_generate_button_click)
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
qr_code_label = ttk.Label(root)

url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
url_entry.grid(row=0, column=1, padx=10, pady=5)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)
quit_button.grid(row=4, column=0,columnspan=2, pady=10)
qr_code_label.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()
