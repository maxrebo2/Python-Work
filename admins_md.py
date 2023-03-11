""" A collection of classes for modeling an admin user account."""

from users_md import User


class Admin(User):
	""" A user with administrative privileges."""

	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize the admin."""
		super().__init__(first_name, last_name, username, email, location)
		

		# Initialize an empty set of privileges.
		self.privileges = Privileges([])




class Privileges():
	"""A class to store admin's privileges."""



	def __init__(self, privileges):
		"""Initialize the privileges object."""
		self.privileges = privileges 


	def show_privileges(self):
		""" Display the privileges this administrator has."""
		for privilege in self.privileges:
			print("- " + privilege)
