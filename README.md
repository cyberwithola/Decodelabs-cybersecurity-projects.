# Password Strength Checker 🔐

A Python command-line tool that evaluates password strength in real time, built as **Project 1** of the DecodeLabs Cybersecurity Internship (2026 Batch).

## Overview

This tool analyzes a password and classifies it as **Weak**, **Medium**, or **Strong** based on length, character variety, and a check against commonly leaked passwords. It's a hands-on introduction to the security logic that underpins real-world authentication systems, before moving on to hashing and encryption in later projects.

## Features

- ✅ Length validation (minimum 8 characters)
- ✅ Checks for uppercase letters, lowercase letters, digits, and special characters
- ✅ Cross-references input against a list of commonly leaked passwords
- ✅ Clear strength classification with a reason for the result
- ✅ Interactive loop — test multiple passwords in one session

## How It Works

The checker scores a password against 5 criteria:

| Check | Requirement |
|---|---|
| Length | 8+ characters |
| Uppercase | At least one A–Z |
| Lowercase | At least one a–z |
| Digit | At least one 0–9 |
| Symbol | At least one special character (`!@#$%^&*` etc.) |

A password that matches a known leaked/common password is automatically marked **Weak**, regardless of how many other checks it passes — complexity doesn't help if the password is already public knowledge.

## Getting Started

### Prerequisites
- Python 3.7 or higher

### Run it

```bash
python "Password strength checker.py"
```

Then enter a password when prompted. Type `quit` or `exit` to stop.

### Example

```
Enter a password to check: Str0ng!Pass99

----------------------------------------
Password: *************  (length: 13)
----------------------------------------
Score: 5 / 5
Strength: Strong
Reason: Meets all length and character variety requirements.
----------------------------------------
```

## Tech Stack

- **Language:** Python
- **Concepts:** String handling, conditional logic, boolean scoring

## What I Learned

- Applying string-handling and conditional logic to solve a real security problem
- Why password entropy and character variety matter for resisting brute-force attacks
- How basic input validation forms the foundation for more advanced security systems (hashing, encryption — covered in Project 2)

## Author

Built by Olamide as part of the [DecodeLabs](https://www.decodelabs.tech) Industrial Training Kit, 2026 Batch.
