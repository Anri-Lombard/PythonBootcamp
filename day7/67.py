import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"psst, the chosen word is {chosen_word}")

end_of_game = False

display = []

for letter in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("What letter is you guess?\n").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        print("You win.")
        end_of_game = True


