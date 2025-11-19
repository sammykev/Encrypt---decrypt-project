def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # leave spaces and punctuation unchanged

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Encryption Tool ===")
    message = input("Enter your message: ")
    shift = int(3)

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print(f"Encrypted: {encrypted}")
    print(f"Decrypted Back: {decrypted}")


if __name__ == "__main__":
    main()
# Caesar Cipher Implementation