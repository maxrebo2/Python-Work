prompt = "\nPlease enter a topping you want on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

active = True

while active:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        active = False
    else:
        print(f"We'll add {pizza_topping} to your pizza.")