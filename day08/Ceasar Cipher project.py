alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#creating a def function and inside it a for loop the letter=each letter in the text.
def encrypt (original_text, shift_amount):

    #having a variable str where all the data from the for loop will be placed.
    cipher_text = ""

    for letter in original_text:
        #starts with, finding the index nr. for the original letter
        original_position = alphabet.index(letter)

        #then creating a variable for the index nr. when the letter is shifted
        shifted_position = original_position + shift_amount

        #this code will  ensure that we always stays inside the length of the alphabet which is 26
        shifted_position %= len(alphabet)

        #the final letter will be added to the cipher_text outside the for loop.
        #cipher_text is  a str and the shifted_position is an int, it has to be the same operand
        cipher_text += alphabet[shifted_position]

        #finally  print the cipher_text outside the for loop.
    print(cipher_text)

#print the final results, and it works.
print(encrypt(original_text=text,shift_amount=shift))