prompt = "\nPlease enter a topping you want on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

pizza_topping = " "

while pizza_topping != 'quit':
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        break
    else:
        print(f"We'll add {pizza_topping} to your pizza.")