#importing the logo from art.py file
from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for the code to keep running I put it all inside a while loop
#this statement will make sure the loop keep running as long its True
keep_running = True
while keep_running:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))




    def cesar(original_text, shift_amount, encode_or_decode):
        final_text = ""



        if encode_or_decode == "decode":
            shift_amount *= -1


        for letter in original_text:

            #if user input is other values than inside the alphabet list, I will start it all over again.
            if letter not in alphabet:
                print("Error type only letters")
                #the value of this code will be None and contained in another variable "result"
                return None

            original_position = alphabet.index(letter)
            shifted_position = original_position + shift_amount
            shifted_position %= len(alphabet)
            final_text += alphabet[shifted_position]


        return final_text


    result = cesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    if result is None:
        continue
    else:
         print(f"here is the {direction}d result" +" " + cesar(original_text=text, shift_amount=shift, encode_or_decode=direction))

    continue_play = input("Do you want to keep playing type Yes or No").lower()

    if continue_play == "yes":
        continue
    else:
        keep_running = False








