prompt = "How many people are in your dinner group?: "
people = input(prompt)
people = int(people)

if people > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")    