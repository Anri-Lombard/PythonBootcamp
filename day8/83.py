import caeser_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(caeser_art.logo)


def caesar(text, shift, direction):
    new_place = 0
    coded_list = []
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_place = position + shift
                times_more_than_25 = (new_place + 1) / 26
                if times_more_than_25 > 1:
                    new_place -= int(times_more_than_25) * 26
            elif direction == 'decode':
                new_place = position - shift
                times_smaller_than_0 = (new_place + 1) / -26
                if times_smaller_than_0 > 0:
                    new_place += int(times_smaller_than_0) * 26
            else:
                print("That is not a valid function.")
            coded_list += alphabet[new_place]
        elif letter not in alphabet:
            coded_list += letter
        else:
            coded_list += " "
    cipher_text = ''.join(coded_list)
    print(f"The {direction}d result: {cipher_text}")


continue_game = True
while continue_game:
    user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_text = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))

    caesar(text=user_text, shift=user_shift, direction=user_direction)

    answer = input("Type 'yes' to continue and 'no' to stop: ").lower()
    if answer == 'no':
        continue_game = False
        print("This relay server has self-destructed.")
