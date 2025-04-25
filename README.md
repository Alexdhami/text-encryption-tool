# text-encryption-tool

This is a simple Python program that allows users to **encrypt** and **decrypt** messages using an extended Caesar cipher method. Unlike traditional Caesar ciphers that only handle letters, this tool works with **all visible ASCII characters** (from space `32` to tilde `126`), making it more versatile and fun!

---

## ✨ Features

- Encrypt and decrypt full sentences with symbols, numbers, and spaces
- Handles invalid input gracefully
- Uses modular code with a class structure
- Loop-based interaction lets you encrypt/decrypt as many times as you like

---

## 🚀 How It Works

The cipher shifts the ASCII value of each character by a number (`shift`), wrapping around if it goes past the end of the visible character range.

- Input: Any string (letters, symbols, numbers, etc.)
- Output: Cipher text (scrambled based on your shift)

---

## 🛠 Usage

1. **Run the script**:
   ```bash
   python filename.py
