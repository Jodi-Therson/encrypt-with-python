import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

# ENCRYPTION
plain_text = input("Enter Plain Text: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original text: {plain_text}")
print(f"encrypted text: {cipher_text}")

# DECRYPTION
cipher_text_text = input("Enter Encrypted Text: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted text: {cipher_text}")
print(f"original text: {plain_text}")
