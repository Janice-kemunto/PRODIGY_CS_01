def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                base = ord('A')  # ASCII value for 'A'
            else:
                base = ord('a')  # ASCII value for 'a'
                
            # Shift the character and wrap around using modulo
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += new_char
        else:
            # If it's not a letter, just add it as is
            encrypted_text += char
    
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypting is just encrypting with a negative shift

def main():
    print("Caesar Cipher Program")
    action = input("Do you want to 'encrypt' or 'decrypt'? ").strip().lower()

    # Check if the user input is valid
    if action not in ['encrypt', 'decrypt']:
        print("Please enter 'encrypt' or 'decrypt'.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (0-25): "))

    # Validate the shift value
    if shift < 0 or shift > 25:
        print("Shift value must be between 0 and 25.")
        return

    if action == 'encrypt':
        result = encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
