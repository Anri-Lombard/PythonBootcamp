with open("input/names/invited_names.txt") as names:
    name_list = names.readlines()

with open("input/letters/starting_letter.docx") as letter:
    letter_contents = letter.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name).replace("Angela", "Anri")
        with open(f"output/readytosend/{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)

# I learn to use variables to store my changes.
