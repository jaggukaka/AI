class Person(object):

	population = 0
	"""myAge for Person"""
	def __init__(self, myAge):
		super(Person, self).__init__()
		self.age = myAge
		Person.population += 1

	def getPopulation(self):
		return Person.population

	def get_age(self):
		return self.age

		