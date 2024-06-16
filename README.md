# URL to QR Code Converter

This is a simple application built with Python using tkinter and qrcode libraries to generate QR codes from URLs.

## Features

- **Generate QR Code**: Converts a user-provided URL into a QR code.
- **Display QR Code**: Shows the generated QR code within the application window.
- **Save QR Code**: Automatically saves the generated QR code as `qrcode.png` in the current directory.

## Installation

To run this application, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

Install the required Python libraries using pip:
`pip install qrcode[pil] tk`


### Usage
1. Run the Application:
  - Execute the script `qr_code_generator.py` using Python.
    
2. Generate QR Code:
  - Enter a URL into the provided text entry box.  
  - Click on the "Generate QR Code" button to create the QR code.

    
3. Display QR Code:
  - The generated QR code will be displayed in the application window.
  - It is automatically saved as qrcode.png in the current directory.

This QR code will never expire, in contrast to the many sites on the web whose codes expire after a few days and ask for payment in order to extend. Which was the initial motivation to create this project.
