responses = {}

polling_active = True

while polling_active:
    name = input("\What is your name? ")
    response = input("Where would you go on your dream vaction? ")

    responses[name] = response 

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would you like to go to {response} on their dream vacation.")        