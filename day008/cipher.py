alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted = []
    for letter in text:
        index = alphabet.index(letter) + shift
        encrypted.append(alphabet[index % len(alphabet)])
    print(f"The encoded text is {''.join(encrypted)}")

def decrypt(text, shift):
    decrypted = ""
    for letter in text:
        index = alphabet.index(letter) - shift
        decrypted += alphabet[index]
    print(f"The decoded text is {decrypted}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)