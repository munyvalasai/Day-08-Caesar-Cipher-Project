
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
             'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#              't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encryption(plain_text, shift_key):
#     cipher_text = ""
#     for char in plain_text:
#         if char in alphabets:
#             position = alphabets.index(char)
#             new_position = (position + shift_key)
#             cipher_text += alphabets[new_position]
#         else:
#             cipher_text += char
#     print(f"Here is the text after encryption: {cipher_text}")
#
#
# def decryption(cipher_text, shift_key):
#     plain_text = " "
#     for char in cipher_text:
#         if char in alphabets:
#             position = alphabets.index(char)
#             new_position = (position - shift_key)
#             plain_text += alphabets[new_position]
#         else:
#             plain_text += char
#     print(f"Here is the text after decryption: {plain_text}")

def caesar(start_text, shift_amount,cipher_direction):
    end_text = " "
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_amount             # if you enter "You" => 24 + 5 = 29 issue here
            if new_position >= 52:
                new_position = new_position % 52
            end_text += alphabets[new_position]
        else:
            end_text += char
    print(f"Here is the {cipher_direction} result: {end_text}")


wanna_end = False

try:
    while not wanna_end:
        what_to_do = input("Type 'encode' for encryption, type 'decode' for decryption:\n").lower()
        # text = input("Type your message:\n").lower()
        text = input("Type your message:\n")
        shift = int(input("Enter shift key:\n"))
        shift = shift % 52

        # if what_to_do == "encrypt":
        #     encryption(plain_text=text, shift_key=shift)
        # elif what_to_do == "decrypt":
        #     decryption(text, shift)

        caesar(start_text=text, shift_amount=shift, cipher_direction=what_to_do)
        play_again = input("Type 'yes' to continue, 'no' to exit.\n")
        if play_again == 'no':
            wanna_end = True
            print("Have a nice day! Bye..")
except:
    print("Please enter valid text or key")
