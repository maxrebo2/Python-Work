sandwich_orders = ['Rueben', 'Turkey Bacon Cheddar', 'Ham and Cheese', 'Italian Cold Cuts']

finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"{finished_sandwich} has been completed.")
    finished_sandwiches.append(finished_sandwich)

print("\nThe following sandwiches have been completed:")
for sandwich in finished_sandwiches:
    print(sandwich)    