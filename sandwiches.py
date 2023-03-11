def make_sandwiches(*fillings):
	print("Making a sandwich with the following fillings:")
	for filling in fillings:
		print(f"- {filling}")


make_sandwiches('Pastrami', 'Swiss Cheese', 'Sauerkraut', 'Yellow Mustard', 'Dill Pickles')
make_sandwiches('Turkey Breast', 'Bacon', 'Cheddar')
		