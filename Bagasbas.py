# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    return caesar_encrypt(encrypted_message, -shift)

def main():
    message = "James Rymarc Bagasbas!"
    shift = 3
    encrypted_message = caesar_encrypt(message, shift)
    print("Encrypted:", encrypted_message)
    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print("Decrypted:", decrypted_message)

if __name__ == "__main__":
    main()

print("James Rymarc Bagasbas, IT36, BSIT, Information Assurance and Security")