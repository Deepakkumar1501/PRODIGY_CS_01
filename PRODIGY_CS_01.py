# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:38:14 2024

@author: deepak kumar
"""

def encrypt(text, shift):
    result = ""
    
    # traverse text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Add unchanged non-alphabetic characters
        else:
            result += char
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'encrypt':
        print(f"Encrypted message: {encrypt(message, shift)}")
    elif choice == 'decrypt':
        print(f"Decrypted message: {decrypt(message, shift)}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
