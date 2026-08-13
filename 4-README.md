# Password Strength Checker 🔐

A Python command-line tool that evaluates password strength in real time. This project was built as **Project 1** of the DecodeLabs Cybersecurity Internship (2026 Batch).

## Overview

This tool analyzes a password and classifies it as **Weak**, **Medium**, or **Strong** based on its length, character variety, and whether it matches a list of commonly used weak passwords.

The project provides a practical introduction to password security concepts and demonstrates how basic validation and scoring logic can be used to evaluate password strength.

## Features

* ✅ Validates password length with a minimum requirement of 8 characters
* ✅ Checks for uppercase letters
* ✅ Checks for lowercase letters
* ✅ Checks for digits
* ✅ Checks for special characters
* ✅ Checks input against a list of commonly used weak passwords
* ✅ Provides a strength score out of 5
* ✅ Classifies passwords as Weak, Medium, or Strong
* ✅ Provides a reason explaining the result
* ✅ Interactive loop allows multiple passwords to be tested in one session
* ✅ Masks passwords when displaying results

## How It Works

The checker evaluates a password against five criteria:

| Check     | Requirement                    |
| --------- | ------------------------------ |
| Length    | 8 or more characters           |
| Uppercase | At least one A–Z character     |
| Lowercase | At least one a–z character     |
| Digit     | At least one 0–9 character     |
| Symbol    | At least one special character |

Each satisfied criterion contributes to the password's overall score.

The program also checks whether the password matches a commonly used weak password. This helps identify passwords that may be easy to guess even if they satisfy some of the character requirements.

The final score is used to classify the password as **Weak**, **Medium**, or **Strong**, while the program provides a reason for the classification.

## Getting Started

### Prerequisites

* Python 3.7 or higher

### Run the Program

From the project directory, run:

```bash
python 1-password_strength_checker.py
```

The program will prompt you to enter a password to check.

Type `quit` or `exit` to stop the program.

## Example

```text
Password Strength Checker
=========================

Type 'quit' or 'exit' to stop.

Enter a password to check: Str0ng!Pass99

----------------------------------------
Password: *************  (length: 13)
----------------------------------------
Score: 5 / 5
Strength: Strong
Reason: Meets all length and character variety requirements.
----------------------------------------
```

## Project Files

| File / Folder                    | Description                                          |
| -------------------------------- | ---------------------------------------------------- |
| `1-password_strength_checker.py` | Main Python program that evaluates password strength |
| `2-output.txt`                   | Sample output produced by the program                |
| `3-screenshots/`                 | Screenshots demonstrating the program running        |
| `4-README.md`                    | Project documentation                                |

## Tech Stack

* **Language:** Python
* **Standard Library:** `string`
* **Concepts:** String handling, conditional logic, sets, functions, boolean evaluation, input validation, and scoring

## What I Learned

* Applying Python string-handling and conditional logic to solve a practical cybersecurity problem
* Using boolean conditions to evaluate multiple password security requirements
* Understanding why password length and character variety contribute to password strength
* Implementing a simple scoring system to classify password strength
* Understanding why commonly used passwords can pose a security risk
* Building an interactive command-line security tool

## Author

Built by Olamide as part of the [DecodeLabs](https://www.decodelabs.tech) Industrial Training Kit, 2026 Batch.
