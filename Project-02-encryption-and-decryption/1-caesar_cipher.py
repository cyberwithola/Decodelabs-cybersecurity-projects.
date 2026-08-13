
# Caesar Cipher - Basic Encryption & Decryption
# DecodeLabs Industrial Training Kit - Project 2


def main():
    print("=" * 25)
    print("    Caesar Cipher Tool")
    print("=" * 25)
    print("Choose an option:")
    print("  1. Encrypt a message")
    print("  2. Decrypt a message")
    print("  3. Quit")

    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = get_shift_key()
            encrypted = encrypt(text, shift)

            print("\n" + "-" * 45)
            print(f"Encrypted message: {encrypted}")
            print("(Save this shift key — you'll need it to decrypt later.)")
            print("-" * 45)

        elif choice == "2":
            cipher_text = input("Enter the encrypted message: ")
            shift = get_shift_key()
            original = decrypt(cipher_text, shift)

            print("\n" + "-" * 45)
            print(f"Decrypted message: {original}")
            print("-" * 45)

        elif choice in ("3", "quit", "exit"):
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")



def encrypt(text: str, shift: int) -> str:

    result = ""
    shift = shift % 26

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text: str, shift: int) -> str:

    return encrypt(text, -shift)


def get_shift_key() -> int:

    while True:
        raw = input("Enter shift key (e.g. 3): ").strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number (e.g. 3, -5, 13).")

if __name__ == "__main__":
    main()
