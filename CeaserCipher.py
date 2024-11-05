def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + (shift_amount if char.islower() else shift_amount)

            if char.islower() and char_code > ord('z'):
                char_code -= 26
            elif char.isupper() and char_code > ord('Z'):
                char_code -= 26

            result += chr(char_code)
        else:
            result += char

    return result
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))
encrypted_message = caesar_cipher(message, shift_value)
print("Encrypted message:", encrypted_message)
decrypted_message = caesar_cipher(encrypted_message, -shift_value)
print("Decrypted message:", decrypted_message)
