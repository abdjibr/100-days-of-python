alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def cesar(original_text, shift_amount, encode_or_decode):
    final_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        original_position = alphabet.index(letter)
        shifted_position = original_position + shift_amount
        shifted_position %= len(alphabet)
        final_text += alphabet[shifted_position]

    return final_text

print(f"here is the {direction}d result" +" " + cesar(original_text=text, shift_amount=shift, encode_or_decode=direction))










