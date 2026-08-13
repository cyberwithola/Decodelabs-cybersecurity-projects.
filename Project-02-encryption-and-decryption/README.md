# Caesar Cipher — Encryption & Decryption 🔐

A Python command-line tool that encrypts and decrypts text using the classic Caesar cipher. This project was built as **Project 2** of the DecodeLabs Cybersecurity Internship (2026 Batch).

## Overview

This tool takes a message and a shift key from the user, then encrypts or decrypts the text by shifting each letter along the alphabet. It's a hands-on introduction to the fundamentals of data confidentiality, transforming readable plaintext into unreadable ciphertext, and reversing the process with the correct key.

## Features

* ✅ Encrypts any message using a user-defined shift key
* ✅ Decrypts messages back to their original text using the same key
* ✅ Handles both uppercase and lowercase letters
* ✅ Leaves spaces, numbers, and punctuation unchanged
* ✅ Accepts negative shift values as well as positive ones
* ✅ Validates shift key input, rejecting non-numeric entries
* ✅ Interactive menu allows multiple encrypt/decrypt operations in one session
* ✅ Decryption is implemented as the inverse of encryption, avoiding duplicate logic

## How It Works

The checker transforms each letter using modular arithmetic:

| Step    | Description                                                     |
| ------- | ---------------------------------------------------------------- |
| Convert | Each letter is converted to its A–Z / a–z position                |
| Shift   | Position is shifted by the chosen key                             |
| Wrap    | Result is wrapped using % 26 so it loops around the alphabet      |
| Rebuild | Shifted position is converted back into a letter                  |

```
E(x) = (x + shift) % 26      → Encryption
D(x) = (x - shift) % 26      → Decryption
```

Since the same key both locks and unlocks the message, this is a symmetric cipher.

## Getting Started

### Prerequisites

* Python 3.7 or higher

### Run the Program

From the project directory, run:

```
python 01-caesar_cipher.py
```

The program will show a menu to encrypt, decrypt, or quit.

## Example

```
=========================
    Caesar Cipher Tool
=========================
Choose an option:
  1. Encrypt a message
  2. Decrypt a message
  3. Quit

Enter choice (1/2/3): 1
Enter text to encrypt: Hello World
Enter shift key (e.g. 3): 3

---------------------------------------------
Encrypted message: Khoor Zruog
(Save this shift key — you'll need it to decrypt later.)
---------------------------------------------
```

## Project Files

| File / Folder         | Description                                          |
| ---------------------- | ----------------------------------------------------- |
| 01-caesar_cipher.py    | Main Python program that encrypts and decrypts text   |
| 02-output.txt          | Sample output produced by the program                 |
| 03-screenshot.png      | Screenshot demonstrating the program running          |
| README.md              | Project documentation                                 |

## Tech Stack

* **Language:** Python
* **Concepts:** ASCII/character manipulation, modular arithmetic, string handling, conditional logic, functions, input validation

## Security Note

The Caesar cipher is not secure by modern standards, with only 25 possible keys, it can be brute-forced instantly, and it preserves letter-frequency patterns, making it vulnerable to frequency analysis. It's used here to learn the fundamentals of substitution ciphers and reversible logic, which form the conceptual foundation for stronger algorithms like AES.

## What I Learned

* How classic substitution ciphers work using ASCII character shifting
* Applying modular arithmetic to handle alphabet "wraparound"
* Writing reversible logic — decryption as the inverse of encryption, not separate code
* Structuring a simple, user-friendly CLI program

## Author

Built by Olamide as part of the [DecodeLabs](https://www.decodelabs.tech) Industrial Training Kit, 2026 Batch.