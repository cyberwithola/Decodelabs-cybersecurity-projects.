
# Password Strength Checker
# DecodeLabs Industrial Training Kit - Project 1


import string

# A small sample of extremely common leaked/weak passwords.
COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678", "qwerty",
    "letmein", "admin", "welcome", "iloveyou", "abc123",
    "111111", "123123", "monkey", "dragon", "football",
}

SPECIAL_CHARACTERS = set("!@#$%^&*()_+-=[]{}|;:,.<>?/~`")


def check_strength(password: str) -> dict:
    checks = {
        "length_ok (8+ chars)": len(password) >= 8,
        "has_uppercase": any(c.isupper() for c in password),
        "has_lowercase": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_symbol": any(c in SPECIAL_CHARACTERS for c in password),
    }

    is_common = password.lower() in COMMON_PASSWORDS
    score = sum(checks.values())


    if is_common:
        label = "Weak"
        reason = "This password appears in a list of commonly leaked passwords."
    elif not checks["length_ok (8+ chars)"]:
        label = "Weak"
        reason = "Password is shorter than 8 characters."
    elif score >= 5:
        label = "Strong"
        reason = "Meets all length and character variety requirements."
    elif score >= 3:
        label = "Medium"
        reason = "Meets some requirements, but could be improved."
    else:
        label = "Weak"
        reason = "Fails most character variety requirements."

    return {
        "checks": checks,
        "is_common": is_common,
        "score": score,
        "label": label,
        "reason": reason,
    }


def print_report(password: str) -> None:

    result = check_strength(password)

    print("\n" + "-" * 40)
    print(f"Password: {'*' * len(password)}  (length: {len(password)})")
    print("-" * 40)
    print(f"Score: {result['score']} / 5")
    print(f"Strength: {result['label']}")
    print(f"Reason: {result['reason']}")
    print("-" * 40)


def main():
    print("=" * 25)
    print("Password Strength Checker")
    print("=" * 25)
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        password = input("Enter a password to check: ").strip()

        if password.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        if password == "":
            print("Please enter a non-empty password.\n")
            continue

        print_report(password)
        print()


if __name__ == "__main__":
    main()