with open("./Input/Letters/starting_letter.txt") as letter:
    body = letter.read()

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

for name in names:
    name = name.rstrip()
    new_letter = body.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", "w") as output:
        output.write(new_letter)