def make_car(manufacturer, model, **options):
	""" Build a dictionary containing everything we know about a car."""
	car_dict = {
		'manufacturer': manufacturer.title(),
		'model': model.title(),
	}
	for option, value in options.items():
		car_dict[option] = value

	return car_dict
	

my_rav4 = make_car('toyota', 'rav4', color='black')
print(my_rav4)	

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)
