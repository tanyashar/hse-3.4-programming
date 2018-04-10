class Person:
	def __init__(self, FIO, age):
		self.FIO = FIO
		self.age = age
	
	def __str__(self):
		return self.FIO + ' age' + str(self.age)
		

class Staff(Person):
	def __init__(self, FIO, age, experience, salary, timetable):
		self.experience = experience
		self.salary = salary
		self.timetable = timetable
		super(Staff, self).__init__(FIO, age)

		
		