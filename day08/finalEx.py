# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def ceaser(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     for letter in start_text:
#         position = alphabet.index(letter)
#         if cipher_direction == "decode":
#             shift_amount *= -1
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"the {cipher_direction}d text is {end_text}")

# ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print({cipher_text})

# def decrypt(chiper_text, shift_amount):
#     plain_text = ""
#     for letter in chiper_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print({plain_text})

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
            
    print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

def process_shift(shift_num):
    return shift_num % 26

def run_caesar_cipher():
    should_continue = True
    
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        
        shift = process_shift(shift)
        
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
        if restart != "yes":
            should_continue = False
            print("Goodbye!")

run_caesar_cipher()

#* --- CHANGES FROM ORIGINAL CODE ---
# *1. Fixed the decode issue - shift_amount is multiplied by -1 once before the loop, not inside it
# *2. Added handling for non-alphabet characters (spaces, numbers, symbols) with if-else check
# *3. Created process_shift() function to handle shift values greater than 26 using modulo
# *4. Implemented restart functionality with a while loop in run_caesar_cipher() function
# *5. Improved the output message formatting
# *6. Added a goodbye message when exiting the program