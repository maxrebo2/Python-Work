sandwich_orders = ['Rueben', 'Pastrami', 'Turkey Bacon Cheddar', 'Ham and Cheese', 'Pastrami', 'Italian Cold Cuts', 'Pastrami']

finished_sandwiches = []



while 'Pastrami' in sandwich_orders:
    print("I am sorry but we are all out of Pastrami.")
    sandwich_orders.remove('Pastrami')
    

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"{finished_sandwich} has been completed.")
    finished_sandwiches.append(finished_sandwich)

print("\nThe following sandwiches have been completed:")
for sandwich in finished_sandwiches:
    print(sandwich)  