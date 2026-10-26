# QR Code Generator

A simple Tkinter app that converts text or a URL into a QR code and saves it as a PNG image.

## Install dependency
```bash
python -m pip install "qrcode[pil]"
```

## Run
```bash
python qr_code_generator.py
```

## How it works
1. The user enters text or a URL.
2. `qrcode.make()` creates the QR image.
3. A save dialog lets the user choose where to save the PNG file.

## Files
- `qr_code_generator.py` — application code.
